from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config.setting import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.route('/')
def home():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
