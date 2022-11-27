from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/hello/')
def hello():
    name = request.args.get('name')
    message = request.args.get('message')
    return f"Hello {name}! {message.replace('_', ' ')}!"


if __name__ == '__main__':
    app.run()
