from flask import Flask, render_template, request, escape
from flask_bootstrap import Bootstrap

from DBcm import UseDatabase

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
@app.route('/index')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('index.html',
                           the_title='Welcome to search4letters on the web!')

@app.route('/single')
def index() -> 'html':
    return render_template('single.html',)

@app.route('/index')
def backhome() -> 'html':
    return render_template('index.html',)



if __name__ == '__main__':
    app.run(debug=True)
