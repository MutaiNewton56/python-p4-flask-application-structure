from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
   return redirect(url_for('user', username='Newton'))

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
