#!/usr/bin/env python


import time
import webbrowser
try:
    import SimpleHTTPServer
    import thread
except:
    import http.server as SimpleHTTPServer
    import _thread as thread


def launch():
    time.sleep(1)
    webbrowser.open("http://localhost:8000/PresenterFiles/Presenter.html")


thread.start_new_thread(launch, ())

# start mini HTTP daemon.
SimpleHTTPServer.test(HandlerClass=SimpleHTTPServer.SimpleHTTPRequestHandler)
