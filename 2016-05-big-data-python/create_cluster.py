import boto3 

emr = boto3.client('emr')

response = emr.run_job_flow(
    Name='databig',
    ReleaseLabel="emr-4.6.0",
    Instances={
        'Ec2KeyName': 'demo-work',
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Placement': {
            'AvailabilityZone': 'us-east-1a'
        },
        'InstanceGroups': [
            {
                'InstanceCount': 1,
                'InstanceRole': 'MASTER',
                'InstanceType': 'm3.xlarge',
                'Name': 'Master'
            },
            {
                'InstanceCount': 2,
                'InstanceRole': 'CORE',
                'InstanceType': 'm3.xlarge',
                'Name': 'Core'
            },
        ]
    },
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    VisibleToAllUsers=True,
    Applications=[
        {'Name': 'Hadoop'},
        {'Name': 'Hive'},
        {'Name': 'Spark'},
    ])

print(response)
