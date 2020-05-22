from flask import Flask, render_template, request, redirect, url_for, flash, session
from model import Users
from fy import fy
from bdc import bdc
from exts import db
import config
from flask_login import \
    login_user, login_required,\
    LoginManager, current_user,\
    logout_user

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(fy)
app.register_blueprint(bdc)
# app.register_blueprint(app)

loginmanager = LoginManager()
loginmanager.session_protection = 'strong'
loginmanager.login_view = 'login'
loginmanager.init_app(app)

@loginmanager.user_loader
def load_user(id):
    return Users.query.get(id)

@app.route('/')
def home():
    try:
        uid = current_user.name
        if uid:
            print(uid)
            return redirect(url_for(uid + '.hello'))
    except:
        return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        uid = request.form['username']
        upwd = request.form['password']
        user = Users.query.filter_by(name = uid).first()
        if user and user.check_password(upwd):
            login_user(user)
            #法院0
            if user.userid == 0:
                return redirect(url_for('fy.hello'))
            if user.userid == 1:
                return redirect(url_for('bdc.hello'))
        else:
            flash('账号或者密码错误')
            return render_template('login.html')
    if request.method == 'GET':
        return redirect(url_for('home'))




@app.route('/logout',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash('已退出')
    return  render_template('login.html')

if __name__ == '__main__':
    app.run()
