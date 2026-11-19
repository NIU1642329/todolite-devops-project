import os
from flask import Flask
from dotenv import load_dotenv
from models import db

load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///todo.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if test_config:
        app.config.update(test_config)
    db.init_app(app)

    from auth import auth_bp
    from todos import todos_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(todos_bp)
    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    create_app().run()
