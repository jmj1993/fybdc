from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def home():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
