from flask_login import login_user, logout_user

from website.utils.data_handler import DataHandler
from website.models import User

class LoginHandler:
  """Handles the login and logout functionality for each user."""
  def __init__(self):
    self.data_handler = DataHandler()
  
  def create_and_sign_in_user(self, data: dict) -> None:
    """Creates and logs the user into the application and remembers them until they logout or the server resets."""
    user = self.data_handler.create_user(data)
    login_user(user, remember=True)
  
  @staticmethod
  def sign_in_user(data: dict) -> None:
    """Logs the user into the application and remembers them until they logout or the server resets."""
    user = User.query.filter_by(email=data['email']).first()
    login_user(user, remember=True)

  @staticmethod
  def logout_current_user():
    """Log the current user out of the website."""
    logout_user()
