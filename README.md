Markdown Presenter
==================

#### Switching between slides
Use the **arrow keys** on your keyboard to switch between slides.

Quick start for MacOS or Linux OS users
----------

You can edit and save ```presentation.md``` with any editor and reloead presentation by hitting F5 or Spacebar.

Markdown File
-------------

The presentation.md file is where you put your presentation. All you need to do to separate slides is a paragraph with an exclamation mark, eg:

    This is a slide
    Blah blah blah

    !

    This is another slide
    Yada yada yada

How it works
------------
The `Presenter.html` fetches the `presentation.md` from the server via
Ajax, uses [Showdown.js](https://github.com/coreyti/showdown) to
transform it into HTML, splits it on `<p>!</p>` into individual
slides, and displays the current slide.
