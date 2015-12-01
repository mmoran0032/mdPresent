Markdown Presenter
==================

To begin the presentation, run `./startPresentation.py` in directory. Opens
presentation within your default web browser and shows the server output
within the terminal.

Use the **arrow keys** on your keyboard to switch between slides.

You can edit and save `presentation.md` without interrupting the server. You
will need to reload (F5) the presentation tab to show the changes.

See the current `presentation.md` file for information on how to format your
slides, include images, etc. Markdown guides are also available online.


How it works
------------

The `Presenter.html` fetches the `presentation.md` from the server via Ajax,
uses [Showdown.js](https://github.com/coreyti/showdown) to transform it into
HTML, splits it on `<p>!</p>` into individual slides, and displays the
current slide.

