from flask import Flask, render_template, request, escape
from flask_bootstrap import Bootstrap

from DBcm import UseDatabase

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/index')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('index.html')

@app.route('/admin')
def adminpage() -> 'html':
    return render_template('admin.html',)

@app.route('/signin')
def signin() -> 'html':
    return render_template('signin.html',)

@app.route('/signup')
def signup() -> 'html':
    return render_template('signup.html',)

@app.route('/single')
def index() -> 'html':
    return render_template('single.html',)

@app.route('/admin')
def adminpage() -> 'html':
    return render_template('admin.html',)

@app.route('/p_velo')
def page_velo() -> 'html':
    return render_template('p_velo.html',)

@app.route('/p_travel')
def page_travel() -> 'html':
    return render_template('p_travel.html',)


@app.route('/index')
def backhome() -> 'html':
    return render_template('index.html',)



if __name__ == '__main__':
    app.run(debug=True)
