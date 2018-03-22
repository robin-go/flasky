from flask import Flask
from flask import request, current_app
from flask import make_response, redirect, abort

from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s</h1>' % name


@app.route('/ua/')
def get_ua():
    ua = request.headers.get('User-Agent')
    return '<p>your browser is %s</p>' % ua


@app.route('/crtapp/')
def crtapp():
    return 'current_app is %s' % current_app.name


@app.route('/setcookie/<name>')
def setcookie(name):
    response = make_response('<h2>set your name in cookie</h2>')
    response.set_cookie('name', name)
    return response


@app.route('/baidu/')
def baidu():
    return redirect('http://baidu.com')


@app.route('/userid/<int:id>')
def userid(id):
    if id > 10:
        abort(404)
    return '</h2>This user is exest</h2>'


if __name__ == '__main__':
    manager.run()
