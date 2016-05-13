# Big Data - Python, Spark, Pandas

Set up a small Amazon EMR cluster for testing Spark, Pandas, and Jupyter. 

By default, 3 m3.xlarge instances are started.
Check the associated costs before running this and make sure to shutdown the cluster when done. 

## Access the Amazon EC2 EMR console

Navigate to EMR in the Amazon console or go to https://console.aws.amazon.com/elasticmapreduce/

You can terminate and check the status of the cluster from there.

## Install the required libraries boto3 and awscli
``` 
pip install -r requirements.txt 
```

## Start the cluster

Modify Ec2KeyName in the [create_cluster.py](create_cluster.py) to a keyname you have available.

```
python create_cluster.py
```

You should see output like 
```
{'ResponseMetadata': {'HTTPStatusCode': 200, 'RequestId': '269d012a-18a6-11e6-8e6e-d96048f3cb64'}, u'JobFlowId': u'j-154L00L3FUEPP'}
```

The JobFlowId will be used for uniquely identifying the cluster.


## View existing clusters

```
aws emr list-clusters --active
```

The state of a cluster will show up as 

```
"State": "STARTING" 
```

while it is being provisioned. When it has finished provisioing, the status will be 

```
"State": "WAITING"
```

It may take some time to provision.


## View cluster instances
```
aws emr list-instances --cluster-id {{Id}}
```

## View cluster instance master

```
aws emr list-instances --instance-group-types MASTER --cluster-id {{Id}} 
```

{{Id}} is the same as JobFlowId


Extract the PublicIpAddress of the last command to get the remote instance

"PublicIpAddress": "54.160.109.220"


## Set up ssh agent and add the named key

```
eval `ssh-agent`
ssh-add ~/.ssh/demo-work.pem
```


## Ssh into the cluster instance master 

```
ssh -A hadoop@{{PublicIpAddress}}
```



## Install anaconda to the master node 

Check the license agreement before installing.

```
wget http://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh
bash Anaconda2-4.0.0-Linux-x86_64.sh -b 
echo >> .bashrc
echo export JAVA_HOME=/usr/lib/java/java >> .bashrc
echo export SPARK_HOME=/usr/lib/spark >> .bashrc
echo export PATH="/home/hadoop/anaconda2/bin:$PATH" >> .bashrc
```

## Install anaconda to all of the nodes 
```
for i in `hdfs dfsadmin -report | grep ^Name | cut -f2 -d: | cut -f2 -d' '`; do 
  ssh -oStrictHostKeyChecking=no $i "wget http://repo.continuum.io/archive/Anaconda2-4.0.0-Linux-x86_64.sh"
  ssh -oStrictHostKeyChecking=no $i "bash Anaconda2-4.0.0-Linux-x86_64.sh -b" 
  ssh -oStrictHostKeyChecking=no $i "echo >> .bashrc"
  ssh -oStrictHostKeyChecking=no $i "echo export JAVA_HOME=/usr/lib/jvm/java >> .bashrc"
  ssh -oStrictHostKeyChecking=no $i "echo export SPARK_HOME=/usr/lib/spark >> .bashrc"
  ssh -oStrictHostKeyChecking=no $i "echo export PATH=\"/home/hadoop/anaconda2/bin:$PATH\" >> .bashrc"
done 
```

Log out of the node and log back in with port-forwarding enabled for 8888

```
ssh -L 8888:127.0.0.1:8888 -A hadoop@{{PublicIpAddress}}
```

 
Test that conda is on the path
```
conda
```

Install the findspark library
```
pip install findspark
```

## Start jupyter notebook 
```
jupyter notebook --no-browser
```

Browse to http://127.0.0.1:8888 on your desktop to access the Jupyter console.

Leave this terminal running in the background



## Run examples 

Download the Complete Works of Shakespeare at 

https://www.gutenberg.org/cache/epub/100/pg100.txt

Upload pg100.txt using Jupyter by clicking the Upload button and choosing the file.
Next click the blue Upload button again.

Go to New -> Terminal 

A web terminal should appear. In the terminal type 

```
hadoop fs -put pg100.txt
```

to upload the file to hdfs

Click on the Jupyter logo to go back to main screen.

Go to New -> Notebooks : Python 2

This will create a new notebook.

In the cell, paste the code and click play to set up the context
```python
import findspark
findspark.init()

import pyspark
sc = pyspark.SparkContext()
```

An asterisk will appear indicating the cell is still running. Wait for it to finish to run the next cell.

In the next cell, run a word count 


```python
text_file = sc.textFile("pg100.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda x, y: x + y)
counts.saveAsTextFile("counts")
```

This will run a spark job to perform the word count

In a terminal connected to the server, run 

```
hadoop fs -ls 
```

Verify that 'counts' are generated 

To see the results run 

```
hadoop fs -cat counts/*
```

### Use Spark Sql Context

Go back to the running notebook. In the next cell paste the following and run

```python
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
counts.toDF().registerTempTable("counts")
top10 = sqlContext.sql("SELECT * FROM counts order by _2 desc limit 10")

x = []
y = [] 

for row in top10.collect():
    y.append(row['_1'])
    x.append(row['_2'])
    print(row['_1'], row['_2'])


```                                           

### Graphing 

Graph the previous results 

```python
%matplotlib inline

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

# ignore empty entry
y = y[1:]
x = x[1:]

y_pos = np.arange(len(y))
plt.bar(y_pos, x, align='center', alpha=0.5)
plt.xticks(y_pos, y)
plt.ylabel('Counts')
plt.title('Most commonly used words')
 
plt.show()
```

### List the active clusters

```
aws emr list-clusters --active
```


# Stop the cluster

```
aws emr terminate-clusters --cluster-ids {{Id}}
```

Check the Amazon console to make sure everything is stopped. Clusters can also be stopped in the console


