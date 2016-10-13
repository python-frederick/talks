% Pygame
%
% Joe Naegele

## Pygame

<http://pygame.org>

## Pygame

- Background
- API
- Demo

## Pygame

Python library designed for writing games

- Written by Pete Shinners
- Can be used for more than just games
- Old and not very "Pythonic"

## Pygame

- Cross-platform
- Does not require OpenGL
- Runs on Android but not iOS

## Pygame

- Small codebase
- Easy to learn
- Simple to use

## Pygame

- Uses optimized C and assembly code for its core functions
- Significantly faster than pure Python code
- Relatively slower than most libraries/languages

## SDL

[Simple DirectMedia Layer](https://www.libsdl.org/)

- Well-established (since 1998)
- Cross-platform C library
- Provides low-level access to hardware:

    - audio
    - graphics
    - keyboard, mouse, joystick

## Alternatives

## Pyglet

<http://pyglet.org>

- Built on OpenGL
- More "Pythonic" API
- Smaller community

## Kivy

<http://kivy.org>

- Young, modern, well-designed
- Much larger UI library, more than just games
- Runs on iOS

## Recap

- Extensive but easy to use
- Slow but not too slow
- Great for prototyping!

## Powerful

You can make great games with Pygame!

<iframe width="640" height="360" src="https://www.youtube.com/embed/chZZpo85b-g?rel=0" frameborder="0" allowfullscreen></iframe>

## Documentation

- <http://pygame.org/docs/>
- Read the [Newbie Guide](http://www.pygame.org/docs/tut/newbieguide.html)
- "Learn" section of the website - books and tutorials

## Examples

Pygame ships with a number of small examples

```python
python -mpygame.examples.chimp
```

## Making games

At a *very* basic level, we need the ability to:

- draw on the screen
- handle user input
- maybe play sounds

## Game Loop

You must write the "main" loop

- manually process events
- update game logic
- render frame

## Game Loop

Simplest approach: do it all in one loop

```python
def main():
    while True:
        for event in events:
            handle(event)
        for entity in game:
            entity.update()
        for entity in game:
            entity.render()
```

## Pyglet

Contrast this with Pyglet:

```python
def main():
    win = pyglet.window.Window()

    @win.event
    def on_draw():
        win.clear()
        entity.render()

    def update(dt):
        entity.update()

    pyglet.clock.schedule_interval(update, 0.2)
    pyglet.app.run()
```

## API

- <http://pygame.org/docs>

## Initialize

- `pygame.init()`

## Display

- `pygame.display.init()`
- `pygame.display.set_mode(resolution, flags=0, ...)`
- flags: FULLSCREEN, OPENGL, RESIZABLE, etc.
- `pygame.display.update()`
- `python -mpygame.examples.glcube`

## Surface

- object for representing images, including display
- like a "blank piece of paper"
- `pygame.Surface.blit` - draw one image onto another
- `pygame.Surface.fill` - fill with solid color
- `pygame.Surface.set_alpha` - set transparency level
- `python -mpygame.examples.scroll`

## Events

- key presses
- mouse motion and clicks
- joystick manipulation
- window resize
- Event queue must be flushed continuously: `for event in pygame.event.get(): ...`
- `python -mpygame.examples.eventlist`

## Sprites

- `pygame.sprite.Sprite`
- `pygame.sprite.Group`
- `pygame.sprite.collide_{rect, circle, mask}`
- `python -mpygame.examples.testsprite`

## Fonts

- `pygame.font.init`
- `pygame.font.Font(filename)`
- `python -mpygame.examples.fonty`
- `python -mpygame.examples.freetype_misc`

## Images

- `pygame.image.load(filename) -> Surface`
- `pygame.image.load(fileobj) -> Surface`
- `pygame.image.save(Surface, filename)`
- `python -mpygame.examples.moveit`

## Mixer

- `pygame.mixer.init(frequency, size, channels, buffer)`
- `pygame.mixer.Channel`
- `pygame.mixer.Sound`
- `python -mpygame.examples.sound`

## Time

- `pygame.time.wait` (sleep)
- `pygame.time.Clock`

## Rect

- "Rects are your friends"
- Lowly rectangle object
- Used by much of Pygame's API
- `pygame.Rect(left, top, width, height)`
- `pygame.Rect((left, top), (width, height))`
- etc.

## Tips

(borrowed from the [Newbie Guide](http://www.pygame.org/docs/tut/newbieguide.html))

## Loading Images

Use `surface.convert()` after loading an image for up to 6x increase in blitting speed

```python
background = pygame.image.load("background.png")
background.convert()
```

This changes the surface's pixel format to match that of the display

## "Dirty" Rects

Only update "dirty" rects

`pygame.display.update()` updates the entire screen, which isn't always what you want

Pass a `Rect` or list of `Rects` to `pygame.display.update()`

- Not useful for things like side-scrollers
- Not needed for low-framerate games/apps

## Collision Detection

- Don't bother with per-pixel collision detection
- Python is too slow
- Just use "sub-rect" collision

## Input Handling

2 methods of determining state...

## Input Handling

1. Directly check state of the device:

    - `pygame.key.get_pressed()`
    - `pygame.mouse.get_pressed()`
    - `pygame.mouse.get_pos()`

## Input Handling

2. Monitor event queue:

    ```python
    for event in pygame.event.get():
        if event.type == ...
    ```

    - `KEYDOWN`, `KEYUP`
    - `MOUSEMOTION`, `MOUSEBUTTONDOWN`, `MOUSEBUTTONUP`

## Showcase

---

[QANAT](http://pygame.org/project/2075/) - Galaxians-like SHMUP

by Paul Patterson

<iframe width="640" height="360" src="https://www.youtube.com/embed/wxebbXCEQko?rel=0" frameborder="0" allowfullscreen></iframe>

---

[SubTerrex](http://pygame.org/project/2389/)

by Paul Patterson

<iframe width="640" height="360" src="https://www.youtube.com/embed/LwbVzT7aGAE?rel=0" frameborder="0" allowfullscreen></iframe>

---

[Barbie Seahorse Adventures](http://www.imitationpickles.org/barbie/)

by Phil Hassey

<iframe width="640" height="360" src="https://www.youtube.com/embed/chZZpo85b-g?rel=0" frameborder="0" allowfullscreen></iframe>

---

[Ardentryst](http://www.jordantrudgett.com/ardentryst/about-ardentryst/) - RPG

by Jordan Trudgett

<iframe width="640" height="360" src="https://www.youtube.com/embed/uBGtm_r6_mY?rel=0" frameborder="0" allowfullscreen></iframe>

---

[Frets on Fire](http://fretsonfire.sourceforge.net/) - Guitar Hero clone

by Sami Kyöstilä

<iframe width="640" height="360" src="https://www.youtube.com/embed/c5i6SxSAY4Q?rel=0" frameborder="0" allowfullscreen></iframe>

---

[Void Infinity](http://pygame.org/project-Void+Infinity-2195-.html) - Space RTS

by Jeremy Gagnier

<iframe width="640" height="360" src="https://www.youtube.com/embed/Pino_AhZI_Y?t=9m10s&rel=0" frameborder="0" allowfullscreen></iframe>

## Others

- [StarPusher](http://pygame.org/project-Star+Pusher+(Sokoban+clone)-1900-.html) - Puzzle game by Al Sweigart
- [Ulmo's Adventure](http://www.pygame.org/project-Ulmo's+Adventure-2042-.html) - Zelda-like adventure game by Sam Eldred
- [SolarWolf](http://www.pygame.org/project-SOLARWOLF-44-.html) - Arcade shooter
- [Albow](http://pygame.org/project/338/) - GUI library by Gregory Ewing

## Others

- [Doodle Jump](https://github.com/thefrolov/Doodle-Jump)
- [FlapPy Bird](https://github.com/sourabhv/FlapPyBird)
- [Star Pusher](https://github.com/silshack/starpusher.git)
- [The Stolen Crown](https://github.com/justinmeister/The-Stolen-Crown-RPG)
- [Pacman Python](https://github.com/greyblue9/pacman-python)
- [Space Shooter](https://github.com/prodicus/spaceShooter.git)

## Demo

1. Import/Initialize
2. Load resources
3. Main loop
    - event loop
    - update
    - draw

## Basics

## Snake
