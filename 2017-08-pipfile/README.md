class: center, middle

# Pipfile and pipenv

<br>
## Python Frederick August 2017

Matt Layman [@mblayman](https://twitter.com/mblayman)

[https://www.mattlayman.com](https://www.mattlayman.com)

???

You, yeah, you reading the presenter notes.
You can run this presentation by running:

```bash
$ python3 -m http.server
```

from this directory in a terminal.

---

class: center

# &#x1F511; Key question:

## How can I run my Python application in a consistent<br>(and safe) environment?
--

## Claim: With a Pipfile

???

Key question to answer. But first...

* Who are you?
* What's a bit of your background?
* Where are people at with their Python experience?
* Any project you're currently fascinated with? I can start.

Why should we care?

Define terms...

---

How can I run my ***Python application*** in a consistent (and safe) environment?

# &#x1F40D; Python application

???

What kind of application are we talking about? Name some types...

--
* Not GUI apps (e.g., Dropbox)

???

GUI apps often bundle everything into a big executable/installer.
That's out of scope.
--
* Maybe CLI apps (e.g., HTTPie)

???

HTTPie is an awesome cURL replacement. It uses requests under the covers.
--
* Yes! Web apps (e.g., a Django-based blog)

???

Sweet spot because these can be huge and complicated systems.

---

How can I run my Python application in a consistent (and safe) ***environment?***

# &#x1F30E; Environment

???

Another broad term...

--
* Physical data center? Nope.

--
* Operating system? Nope.

--
* Shell environment variables? Not really.

--
* Python and other Python software. &#x1F604;

---

How can I run my Python application in a ***consistent (and safe)*** environment?

# Consistent<br>(and safe)

--
&hellip; is the heart of the problem.

???

Why is this the main problem? We need to look at how things are currently done.

---

class: center, middle

# Dependencies

# &#x1F525; &#x1F608; &#x1F525;

???

Dependency hell

---

## Current state of the art:

# requirements.txt

--
```python
BeautifulSoup==3.2.1
boto==2.41.0
bottle==0.12.7

# Or without version specifiers

BeautifulSoup
boto
bottle
```

???

Feed `requirements.txt` to `pip`.

Show demo.

---

# To list versions or not&hellip;

--
1. With versions is *pinning*.<br>
   This ***attempts*** to provide consistency.

--
2. Without versions is *unpinned*.<br>
   Common for developers tools like `flake8`.

---

class: center

## What do you mean by &ldquo;*attempts* to provide consistency?&rdquo;

--

<br>
## Transitivity and `install_requires`

# A &#x1F449; B &#x1F449; C

???

The crux of the problem is transitivity.

Your app, A, depends on B, which depends on C.

Did you remember to pin C? Should you have to?

---

class: center

## And about those developer tools&hellip;

--
# &#x1F629;

## requirements-dev.txt

???

We don't want them on the final/production environment.

The community falls apart about the best way to deal with this extra code.

---

class: center, middle

# Problem defined.

# &#x2705;

---

class: center, middle

# Pipfile

# >

# requirements.txt

???

Here comes the claim. A Pipfile addresses these problems.

Not a new idea. See also: Bundler, Cargo, Composer, Yarn

1. Split logical dependencies and a dependency manifest into separate files.
2. Separate the sections for user and developer dependencies.


---

# `Pipefile` anatomy

--
```toml
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true

[dev-packages]
flake8 = "*"
tox = "*"
twine = "*"

[packages]
pytest = "*"
"tap.py" = "*"
```

???

Immediate diff: dev vs required packages.

---

class: center, middle

# Where is the consistency?

---

# `Pipfile.lock`

```json
{
    "_meta": { ...  },
    "default": {
        "tap.py": { "version": "==2.1" },
        ...
    },
    "develop": {
        "flake8": { "version": "==3.3.0" },
        "pyflakes": { "version": "==1.5.0" },
        ...
    }
}
```

???

Heavily trimmed to fit on a slide.

JSON format meant for computers.

*Pins dependencies and transitive dependencies.*

Specifies *all* packages.

So... how do you use these files?

---

class: center, middle

# pipenv:<br>A tool for Pipfiles

???

* History: Pipfile proposed by PyPA.
* Kenneth Reitz ran with it to flesh out the format.
* Kennneth created the pipenv tool.

---

# pipenv features

--
1. Create virtual environments.

???

`pipenv --three`
--
2. Add packages to `Pipfile`.

???

`pipenv install requests`
--
3. Generate and manage `Pipfile.lock`.

???

`pipenv lock`

* Run through the demo. Use https://httpbin.org/get and pprint some json
* Add an extra line and flake8 as a dev tool. Run flake8.
* Recreate virtual env to show use of lock file.

---

class: center

# &#x1F511; Key question (revisited):

## How can I run my Python application in a consistent<br>(and safe) environment?

???

* A consistent env means fewer bugs and wasted time.
* We looked at what it mean to have a consistent env.
* Remember my claim. Pipfile adds consistency.
* Demo showed the consistency.

---

class: center, middle

# Thank you

Matt Layman [@mblayman](https://twitter.com/mblayman)

[https://www.mattlayman.com](https://www.mattlayman.com)
