Markdown Presenter
==================

Demo and usage
--------------
Check out a demo
[here](http://jsakamoto.github.com/MarkdownPresenter/Presenter.html).

#### Switching between slides
Use the **arrow keys** on your keyboard or **swipe horizontally** on touch screen to switch between slides.

#### Reloading
You can reload the presentation at any time - staying on the same
slide number - by pressing the spacebar.

Quick start for MacOS or Linux OS users
----------
Open a terminal and paste the text from below and press enter.

    python -c "exec('try:import urllib2 as m\nexcept:import urllib.request as m');exec(m.urlopen('http://goo.gl/ncwVU2').read())"

Then begin the download all files to needed into current directory.
And after complete all downloads, mini http server is start automatically and open "Markdown Presenter" view by default browser.

You can edit and save ```presentation.md``` by any text editor, and reloead presentation by hit space key.

### Linux OS
On Linux you have Python installed and can start its built-in web server in this directory by running the following:

    python -c "exec('try:import SimpleHTTPServer as m\nexcept:import http.server as m');m.test(HandlerClass=m.SimpleHTTPRequestHandler)"

Markdown File
-------------

The presentation.md file is where you put your presentation. All you need to do to separate slides is a paragraph with an exclamation mark, eg:

    This is a slide
    Blah blah blah

    !

    This is another slide
    Yada yada yada

Printing Support
-----

Markdown Presenter can print out the all slides to any printer from browser printing feature.

![printing](http://jsakamoto.github.io/MarkdownPresenter/printing.png)

The keys to get fine result is follow:

- Layout - Landscape
- Margins - No margin
- Options - Enable to printing background colors

And you can print out as a PDF file, so you can also upload and publish your slides to "slideshare.com".

How it works
------------
The `Presenter.html` fetches the `presentation.md` from the server via
Ajax, uses [Showdown.js](https://github.com/coreyti/showdown) to
transform it into HTML, splits it on `<p>!</p>` into individual
slides, and displays the current slide.
