from os import path
from flask import Flask

from website.routes.auth import auth
from website.routes.views import views
from website.routes.errors import err, page_not_found
from website.extensions import db, login_manager
from website.models import User, Note
from website.utils import constants

app = Flask(__name__)

class SNLTool:
  """A basic representation of the Social News Lookup Tool Flask app."""
  def __init__(self) -> None:
    self.app = app
    self.configure_app()
    self.register_extensions()
    self.register_blueprints()
    self.register_errors()
    self.create_database()
    self.enable_login()
  
  def configure_app(self) -> None:
    """Configures the flask applications settings."""
    self.app.config.update(constants.CONFIG_SETTINGS)

  def register_extensions(self) -> None:
    """Registers the flask applications extensions."""
    db.init_app(self.app)

  def register_blueprints(self) -> None:
    """Registers page blueprints to the app."""
    self.app.register_blueprint(views, url_prefix='/')
    self.app.register_blueprint(auth, url_prefix='/')
    self.app.register_blueprint(err, url_prefix='/')

  def create_database(self) -> None:
    """Creates the SQL databases if they do not exist."""
    if not path.exists(f'website/{constants.DB_NAME}'):
      db.create_all(app=self.app)
      print('Created Database!')

  def enable_login(self) -> None:
    """Provides the ability for users to login and logout of the app."""
    login_manager.login_view = 'auth.login'
    login_manager.init_app(self.app)

    @login_manager.user_loader
    def load_user(user_id: int) -> int:
      """Loads a user based on its user_id in the database."""
      return User.query.get(user_id)

  def register_errors(self):
    """Registers error pages into the app."""
    self.app.register_error_handler(404, page_not_found)
