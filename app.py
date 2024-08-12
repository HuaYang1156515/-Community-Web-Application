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
from models.event import Event
from models.category import Category   

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    events = Event.query.all()  # Fetch all events to display on the homepage
    return render_template('home.html', events=events)

"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
         
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(login=username).first()
        if user and user.check_password(password):  # Assuming you have a check_password method
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(login=username).first()
        if user and user.password == password:  # Directly compare the plain text password
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']  # Assuming role selection during registration
        existing_user = User.query.filter_by(login=username).first()
        if existing_user:
            flash('Username already exists')
            return redirect(url_for('register'))

        user = User(name=username, login=username, role=role)
        user.set_password(password)  # Hash and set the password
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.name = request.form['name']
        current_user.pic = request.form['pic']
        current_user.desc = request.form['desc']
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('profile'))
    return render_template('profile.html')

@app.route('/event/<int:event_id>')
def event_detail(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event_detail.html', event=event)

@app.route('/event/create', methods=['GET', 'POST'])
@login_required
def create_event():
    if current_user.role != 'admin':
        flash('You are not authorized to create events.')
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        location = request.form['location']
        date = request.form['date']
        category_id = request.form['category_id']
        event = Event(name=name, description=description, location=location, date=date, created_by=current_user.id, category_id=category_id)
        db.session.add(event)
        db.session.commit()
        flash('Event created successfully!')
        return redirect(url_for('home'))
    categories = Category.query.all()
    return render_template('create_event.html', categories=categories)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
