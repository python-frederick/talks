class: center, middle

# Django REST Framework

#### Python Frederick June 2016

Matt Layman [@mblayman](https://twitter.com/mblayman)

[mattlayman.com](http://www.mattlayman.com)

---

# Let's make an API

* The API will be JSON based.
* Our demo will be for a joke website.
* For simplicity, a joke will be a `question` with a `punchline`.
  It keeps track of `laughs` (a.k.a. *likes* on social media sites).

---

# Set up the environment

```bash
$ mkdir drf-demo && cd drf-demo
$ virtualenv venv
$ source venv/bin/activate
$ pip install Django djangorestframework httpie
```

A virtual environment helps to keep all Python code
in one location (a directory) to reduce conflicts
on the machine.

---

# Start the project

A *project* is Django's terminology for the top most level thing.

```bash
$ django-admin startproject lolz .
```

---

# Start an app

An *application* is Django's terminology for a subset of the project
for related things (e.g., models, views, shared URL namespace).

```bash
$ ./manage.py startapp jokes
```

---

# Do the Joke modeling

Django models are the Python abstraction for interfacing
with database tables.

1. Add `jokes` to `INSTALLED_APPS` via `jokes.apps.JokesConfig`.
2. Create a `Joke` model.
3. Register a `Joke` admin for adding data.

---

# Apply models to database

Run commands to populate the database
(i.e. auto-generate DDL and execute)

Django migrations align a database
with the model layer definitions.

```bash
$ ./manage.py makemigrations
$ ./manage.py migrate
```

---

# Create a user for the admin

This will grant access to the admin UI for data entry.

```bash
$ ./manage.py createsuperuser
```

---

# Add some data

```bash
$ ./manage.py runserver
```

Navigate to http://localhost:8000/admin/

???
How many software developers does it take to screw in a light bulb?
None. That's a hardware problem.

['hip', 'hip']
(hip hip array!)

---

class: center, middle

# Now for some<br>Django REST Framework

Let's call this DRF.

---

# Enable Django REST Framework

Put `rest_framework` in `INSTALLED_APPS`.

---

# Make a `JokeSerializer`

In DRF, a *serializer* transforms a model,
or set of models,
into a data structure.

That data structure can produce JSON, XML, HTML, etc.
(via renderers).

---

# Add a `JokeViewSet`

DRF can group views into a cohesive set.
Common view sets include:

* a CRUD set (`ModelViewSet`)
* a read only set (`ReadOnlyModelViewSet`)

---

# Wire it all together

The `router` (an instance of `routers.DefaultRouter`)
is the central thing
that view sets and views plug into.

For example:

```python
router.register(r'jokes', JokeViewSet)
```

---

# Features not covered
--

* Validation
--

* Authentication
--

* Permissions
--

* Throttling
--

* Filtering
--

* Pagination
--

* Versioning
--


Django REST Framework has a huge set of capabilities
***for things that you didn't even know you wanted.***

---

class: center, middle

# Questions?

Matt Layman [@mblayman](https://twitter.com/mblayman)

[mattlayman.com](http://www.mattlayman.com)
