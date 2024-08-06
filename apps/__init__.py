from flask import Flask

from apps.company.routes import blueprint as company_blueprint
from apps.users.routes import blueprint as users_blueprint

app = Flask(__name__)

# config
app.config.from_object('base.config.DevelopmentConfig')


# routes
def register_blueprints(app_flask):
    app_flask.register_blueprint(users_blueprint)
    app_flask.register_blueprint(company_blueprint)


register_blueprints(app)
