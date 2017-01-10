class: center, middle

# Python packaging

<br>
## Python Frederick January 2017

Matt Layman [@mblayman](https://twitter.com/mblayman)

[mattlayman.com](http://www.mattlayman.com)

---

class: center, middle

# How do I share my Python code?

???
Topics: We'll cover

* What's going on with packaging
* How you can make a package of your own
* What are some helpful tools to aide your journey

Key question to answer. But first...

gauge ideas. Find out what people are doing.

---

# Initial thoughts

???
* Not everything needs to be installable from a package manager.
* GitHub can be a perfectly adequate alternative.

--

* Maybe you don&rsquo;t need to

--

* GitHub, Bitbucket are perfectly viable alternatives

---

class: center, middle

```bash
$ pip install Django
```

## What&rsquo;s going on here?

???
1. pip checks to see if the package is already installed in `site-packages`.
2. checks your local cache of packages *cough* npm *cough*.
3. Connects to PyPI to find the package
4. Downloads the package to the cache.
5. Unpacks the package in the appropriate `site-packages` directory.

But how does all that happen?

---

class: center, middle

![Spin!](whirlygig.jpeg)

???
This is a whirlygig. And it is our project.

---

class: middle

```bash
$ tree .
.
├── README.rst
├── setup.py
└── whirlygig
    ├── __init__.py
    ├── spinner.py
    └── tests
        ├── __init__.py
        └── test_spinner.py
```

```python
>>> from whirlygig.spinner import Spinner
>>> s = Spinner()
>>> s.spin()
'Weee!'
```

???

* All projects deserve a README.
* `whirlygig` is our package.
* We've got tests. Do you?

---

class: center, middle

`setup.py` has the magic.

---

class: middle

```python
from setuptools import setup, find_packages

setup(
    name='whirlygig',
    version='0.1',
    packages=find_packages(),
    author='Matt Layman',
    author_email='matthewlayman@gmail.com',
    url='<some URL here>'
)
```

???

History lesson:

* `distutils` is in the standard library, but it wasn't powerful enough.
* `setuptools` took the crown.

The `setup` function is all you need to build a distribution.
Loads of options, but `name` and `version` are the only strictly
required ones.

---

## And we&rsquo;re done&hellip;

```bash
$ python setup.py sdist
$ tar tzf dist/whirlygig-0.1.tar.gz
whirlygig-0.1/
whirlygig-0.1/PKG-INFO
whirlygig-0.1/README.rst
whirlygig-0.1/setup.cfg
whirlygig-0.1/setup.py
whirlygig-0.1/whirlygig/
whirlygig-0.1/whirlygig/__init__.py
whirlygig-0.1/whirlygig/spinner.py
whirlygig-0.1/whirlygig/tests/
<snip>
```

---

## &hellip;with the first part. What&rsquo;s left?

* Make it roll as a `wheel`.
* Test your distribution!
* Upload it.

---

## Wheels

* The wheel format is Python's binary format.

???

* Compiled extensions can be built in separate wheels.

--

```bash
$ cat setup.cfg
[bdist_wheel]
universal = 1
$ python setup.py sdist bdist_wheel
$ ls -1 dist
whirlygig-0.1-py2.py3-none-any.whl
whirlygig-0.1.tar.gz
```

---

## Testing it all with tox

???

`tox` tests the distribution in its *installed* format.
It can catch bugs that you don't expect.

--

```bash
$ pip install tox
$ cat tox.ini
[tox]
envlist = py35
[testenv]
commands = python -m unittest discover \
    -s {envsitepackagesdir}/whirlygig
$ tox -e py35
.
-------------------------------------------
Ran 1 test in 0.000s

OK
```

---

## Upload your creation

Make a PyPI account

--

Don&rsquo;t do this:

```bash
$ python setup.py sdist upload
```

???

The upload command uses HTTP and is not secure.
`twine` offers a secure upload so your credentials are not compromised.

--

Instead, do:

```bash
$ pip install twine
$ twine upload dist/*
```

---

## What did we cover?

* How do packages (or, more pedantically, *distributions*) get installed?
* How can I take my code and make a package out of it?
* What are some tools that can help me make this easier?

---

# Resources

* https://setuptools.readthedocs.io/en/latest/setuptools.html
* https://packaging.python.org/

---

class: center, middle

# Thank you

Matt Layman [@mblayman](https://twitter.com/mblayman)

[mattlayman.com](http://www.mattlayman.com)
