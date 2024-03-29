from flask import Flask, session, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from views import main, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.auth_bp)
    #app.register_blueprint(product_bp)
    #app.register_blueprint(cart_bp)
    #app.register_blueprint(funding_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)