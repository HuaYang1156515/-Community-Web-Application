from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
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


@app.route('/')
def home():
    return 'Hello, Flask!'



from models.user import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
