
# http://bottlepy.org/docs/dev/tutorial.html

from bottle import route, run, static_file

@route('/')
def index():
    return static_file("index.html", root='.')

run(host='localhost', port=8085, debug=True)