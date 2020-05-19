from flask import Flask,render_template
from exts import db
import config

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app = Flask(__name__)

    app.run()
