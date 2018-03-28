from datetime import datetime

from flask import Flask
from flask import request, current_app
from flask import make_response, redirect, abort, render_template

from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Robin is so handsome'
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    params = {
        'form': form,
        'name': name,
        'current_time': datetime.utcnow()
    }
    return render_template('index.html', **params)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


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
