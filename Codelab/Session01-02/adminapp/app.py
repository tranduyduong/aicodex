from flask import Flask
from flask_migrate import Migrate
from config import Config
from extensions import db
from users.controllers import users_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(users_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run()