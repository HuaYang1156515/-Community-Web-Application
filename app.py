from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config.setting import Config



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


from controllers.user_controller import user_bp
from controllers.admin_controller import admin_bp
from controllers.guest_controller import guest_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(guest_bp)

from models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from models.event import Event
@app.route('/')
def home():
    events = Event.query.all()  # Fetch all events to display on the homepage
    return render_template('home.html', events=events)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic here
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(login=username).first()
        if user and user.check_password(password):  # Assuming you have a check_password method
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
