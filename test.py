from flask import Flask
from flask import request
app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
