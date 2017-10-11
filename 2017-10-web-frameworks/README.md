class: center, middle

# Web frameworks shootout<br>&#x1F3AF;

## Python Frederick October 2017

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

## What is the right framework for my next web project?

---

# To ponder &#x1F914;

???

What is your web project?

Things to think about before you start.

--
* Are you doing server rendered HTML?

--
* Do you need an API to power a React, Angular, Ember, or Vue frontend?

--
* Do you enjoy connecting components or using a
  pre-integrated approach?

???

Think about your development style.

The answers to the questions are your personal context for this discussion.

---

# The Contenders

* API Star
* Django
* Falcon
* Flask
* Pyramid

There are many others, but time is limited.

???

Honorable mentions: Bottle, Twisted/Klein, aiohttp, web2py

---

class: center

# &#x26A0; Bias &#x26A0;
--

I work on Django daily for work and it heavily influences my views.

???

Storybird gets a lot done with a small team and Django.

--

# #sorrynotsorry

---

## The feature spectrum &#x1F308;

Each framework exists within a range of features.

???

Each framework has a range of included features,
designed to let you build your own patterns
or work from a set a of pre-selected constraints.
--
* Falcon &lArr; Small feature set

--
* API Star

--
* Flask

--
* Pyramid

--
* Django &lArr; Huge feature set

???

Let's see how the frameworks pitch themselves.

---

# Falcon<br>elevator pitch

> Falcon is a *bare-metal* Python web API framework for building very fast app backends and microservices.<br><br>*(emphasis added)*

???

Focus is on speed.

---

# API Star<br>elevator pitch

> A smart Web API framework, *designed for Python 3.*<br><br>*(emphasis added)*

???

Focus is on using new abilities of Python 3 (like typing).

---

# Flask<br>elevator pitch

> Flask is a *microframework* for Python based on Werkzeug, Jinja 2 and good intentions.<br><br>*(emphasis added)*

???

Focus is on brevity.

---

# Pyramid<br>elevator pitch

> Pyramid is a small, fast, *down-to-earth* Python web framework.<br><br>*(emphasis added)*

???

Focus on trying to fit in the goldilocks zone. Not too many abstractions, not too few.

---

# Django<br>elevator pitch

> Django is a *high-level* Python Web framework that encourages rapid development and clean, pragmatic design.<br><br>*(emphasis added)*

???

Focus on including *all* the concepts needed to build web apps.

The elevator pitches give a very rough sense of what the frameworks are about.
With that perspective...

---

class: center, middle

# Let&rsquo;s look at some code!

# &#x1F913;

???

The scenario: how do we make a "Hello World" HTML and JSON endpoint.

"endpoint" is a URL. /html or /json

---

# Feature Envy? &#x1F60D;

--
* Templates

???

All the frameworks *can* render HTML and do JSON so what do we need to care about?

* Falcon - nope, nope, nope, nope
* API Star - `render_template` J2, nope, Django ORM or SQL Alchemy, nope
* Flask - `render_template` J2, WTForms, SQL Alchemy, nope
* Pyramid - renderer arg in `view_config` J2 Chameleon Mako, Deform, SQL Alchemy ZODB, perms/principal
* Django - `render`, forms, Django ORM, lots of tools

Other topics: db migrations, caching, email, i18n, logging, background work

Do you want to add something when you need it
or ignore it when you don't need it?

--
* Form handling

--
* Database connectivity

--
* Security

---

class: center

# Performance

# Here be &#x1F409; &#x1F409; &#x1F409;

https://www.techempower.com/benchmarks/

---

class: center

# &#x1F511; Key question (revisited):

## What is the right framework for my next web project?

---

class: center, middle

# Thank you

Matt Layman [@mblayman](https://twitter.com/mblayman)

[https://www.mattlayman.com](https://www.mattlayman.com)
