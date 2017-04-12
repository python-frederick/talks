class: center, middle

# Pythonic code

<br>
## Python Frederick April 2017

Matt Layman [@mblayman](https://twitter.com/mblayman)

[mattlayman.com](http://www.mattlayman.com)

???

You, yeah, you reading the presenter notes.
You can run this presentation by running:

```bash
$ python -m SimpleHTTPServer
```

from this directory in a terminal.

---

class: center, middle

# What is <br>Pythonic code?

???
Topics we'll cover

* specific style guidance (list comprehension, with statement, property decorator)
* general guidance (built-ins, standard library, pep8)

Key question to answer. But first...

* Who are you?
* What's a bit of your background?
* Where are people at with their Python experience?
* What are you hoping to learn?

---
background-image: url(santa.jpeg)

???

Let's talk about lists.

---

class: center, middle

# []

???

Python has a few core data types: tuple, list, dictionary

---

## List crash course

```python
empty = []
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Add to a list
len(numbers)  # How many are in the list?
# Lists can mix types.
mixed = [1, 2, 'foo', 'bar']
three = numbers[2]
```

???

Describe the operations.

How would you created a doubled list of numbers?

---

## Double a list of numbers <br>(C++)

```cpp
int size = 5;
int numbers[size] = {1, 2, 3, 4, 5};
int doubled[size];
for (int i = 0; i < size; i++) {
    doubled[i] = 2 * numbers[i];
}
```

---

## Double a list of numbers <br>(1st attempt)

```python
numbers = [1, 2, 3, 4, 5]
doubled = []
size = len(numbers)
i = 0
while i < size:
    doubled.append(2 * numbers[i])
    i += 1
```

---
background-image: url(rage.png)

---

## Double a list of numbers <br>(2nd attempt)

```python
numbers = [1, 2, 3, 4, 5]
doubled = []
for number in numbers:
    doubled.append(2 * number)
```

???

This is a reasonable solution.

---

## Double a list of numbers <br>(3rd attempt)

```python
numbers = [1, 2, 3, 4, 5]
doubled = [2 * number for number in numbers]
```

???

7 lines down to 2. Theme of Pythonic code being short code too.

--

## This is a list comprehension.

???
`doubled` is created with a list comprehension.

---

## List comprehension anatomy

```python
result_list = [
    expression for value in original_list]
```

--
* List constructor - square brackets

--
* An expression - lambda function that receives a value

--
* An iterator over a list

---

## Other cool list comprehensions

### Filtering

```python
numbers = [1, 2, 3, 4, 5]
odds = [number for number in numbers
               if number % 2 != 0]
```

### Nested iteration

```python
xs = [1, 2, 3, 4, 5]
ys = [1, 2, 3, 4, 5]
pairs = [(x, y) for x in xs
                for y in ys]
```

---

class: center, middle

# Open a file

???

* Of course, we're going to look at... cat pics.

---
background-image: url(kitteh.jpeg)

---

## Open a file <br>(1st attempt)

```python
f = open('kitteh.jpg', 'rb')
cat_pic = f.read()
# Do other stuff with the cat picture.
```

???

* Missing the critical `close`
* `IOError` "too many files open"

---

## Open a file <br>(2nd attempt)

```python
f = open('kitteh.jpg', 'rb')
cat_pic = f.read()
# Do other stuff with the cat picture.
f.close()
```

---

## Open a file <br>(3rd attempt)

```python
try:
    f = open('kitteh.jpg', 'rb')
    cat_pic = f.read()
    # Do other stuff with the cat picture.
    f.close()
except:
    print('oops, something went wrong.')
```

???

* Who can spot the bug?
* Yuck, please don't catch all exceptions like this.

---

## Open a file <br>(4th attempt)

```python
try:
    f = open('kitteh.jpg', 'rb')
    cat_pic = f.read()
    # Do other stuff with the cat picture.
except:
    print('oops, something went wrong.')
finally:
    f.close()
```

---

## Open a file <br>(5th attempt)

```python
with open('kitteh.jpg', 'rb') as f:
    cat_pic = f.read()
try:
    # Do other stuff with the cat picture.
except:
    print('oops, something went wrong.')
```

???

Notice that something is absent, where is `close`?

---

class: center, middle

# with

---

## The with statement
--

* When using `with`, `open` automatically closes files.
--

* Work is passed to a "context manager."
--

* A context manager defines `__enter__` and `__exit__`.
--

* Examples: files, locks, timers
--

* Write your own with `contextlib`.

---
background-image: url(classroom.jpeg)

???

Do your classes look like this?

---

## Clean up a class
--

```python
class OhMyJava:
    def __init__(self):
        self._foo = ''
    def get_foo(self):
        return self._foo
    def set_foo(self, foo):
        self._foo = foo
```

```python
oh_my = OhMyJava()
oh_my.set_foo('This is painful.')
```

---

## Clean up a class (1st attempt)

```python
class AwwYeah:
    def __init__(self):
        self.foo = ''
```
--

If you aren't doing anything special,
it is safe to set the attribute directly.

---

class: center, middle

# But, encapsulation!

???

* Setting attributes directly seems to violate encapsulation.
* Encapsulation is supposed to be a core benefit
  of object oriented design.

---

## Clean up a class (2nd attempt)

```python
class AwwYeah:
    def __init__(self):
        self._bar = ''
    @property
    def foo(self):
        return 'Wow: {}'.format(self._bar)
    @foo.setter
    def foo(self, value):
        self._bar = '{}!'.format(value)

>>> a = AwwYeah()
>>> a.foo = 'Python'
>>> a.foo
'Wow: Python!'
```

---

## The property decorator

???

* Fewer parenthesis means less to comprehend.
* Excluding a setter makes ready only properties. Handy.
* Properties are super useful for computed/derived values.
--

* `@property` transforms `obj.foo()` to `obj.foo`
--

* Use of `property` make another decorator available:
  `@foo.setter`
--

* Computed/derived values.

---
background-image: url(core.jpeg)

---

## Use the core
--

* Google search: `python built in functions`
--

* Always globally available functions
--

* Some favorites:
  * `any`
  * `enumerate`
  * `print`
  * `range`
  * `sorted`

---

# any

```python
>>> checks = [False, False, True, False]
>>> status = any(checks)
>>> status
True
```

---

# enumerate

```python
# Bad variable name. Short for slides.
>>> f = ['apple', 'orange', 'kiwi', 'pear']
>>> for idx, fruit in enumerate(f, start=1):
...     print(idx, fruit)
...
(1, 'apple')
(2, 'orange')
(3, 'kiwi')
(4, 'pear')
```

???

* Default start is 0.

---

# print

```python
>>> print('Hello World')
Hello World
>>> import sys
>>> print('An error!', file=sys.stderr)
An error!
```

???

* This is one of the big difference between Python 2 and 3.
* In Python 2, print was a keyword.
* Now, it's much easier to use keyword arguments
  and pass to different streams.

---

# range

```python
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(5, 10)
[5, 6, 7, 8, 9]
>>> range(0, 10, 2)
[0, 2, 4, 6, 8]
```

???

* Step is very infrequently used.

---

# sorted

```python
>>> numbers = [5, 2, 3, 1, 4]
>>> ordered = sorted(numbers)
>>> ordered
[1, 2, 3, 4, 5]
>>> numbers
[5, 2, 3, 1, 4]
>>> numbers.sort()
>>> numbers
[1, 2, 3, 4, 5]
```

???

* Sorted in *new* list.
* In place sorting

---
background-image: url(energizer.png)

---

## Batteries included

???

* The language wants to enable you
  by including the things you'll probably need anyway.
--

* Python has a huge standard library.
--

* There are tools for:
  * Manipulating files (`os.path`)
--

  * Matching patterns (`re`)
--

  * Handling dates and times (`datetime`)
--

  * Creating CLIs (`argparse`)
--

  * Working with CSV (`csv`)
--

  * and tons more!


---

## What did we cover?

* list comprehensions
* the `with` statement
* the `property` decorator
* built-ins
* the standard library

---

# What is <br>Pythonic code?
--

> *Pythonic code is code that takes advantage
> of the features of the Python language
> and feels more natural
> than implementing language X in Python.*

---

# Resources

* https://docs.python.org/3/tutorial/datastructures.html
* https://docs.python.org/3/library/functions.html
* https://docs.python.org/3/library/index.html

---

class: center, middle

# Thank you

Matt Layman [@mblayman](https://twitter.com/mblayman)

[mattlayman.com](http://www.mattlayman.com)
