from flask import flash
from werkzeug.security import check_password_hash

from website.models import User, Note

class FormValidation:
  """Handles the form validation logic."""
  def validate_signup(self, data: dict) -> bool:
    """Checks for validation errors on the sign up page. Flashes a message on the page."""
    errors: list = []
    
    errors.append(self._email_duplicate_check(data['email'], 'An account with that email address already exists!'))
    errors.append(self._first_name_valid(data['firstName']))
    errors.append(self._email_valid(data['email']))
    errors.append(self._password_valid(data['password'], data['confirmPassword']))

    if not any(errors):
      return True
    return False

  def validate_login(self, data: dict) -> bool:
    """Checks for validation errors on the login page. Flashes a message on the page."""
    user = User.query.filter_by(email=data['email']).first()

    if user:
      if check_password_hash(user.password, data['password']):
        flash(f'Welcome back {user.first_name.capitalize()}!', category='info')
        return True
      else:
        flash('Incorrect password, try again.', category='error')        
    else:
      flash('Email does not exist!', category='error')
    
    return False

  def _first_name_valid(self, first_name: str) -> bool:
    """Helper function used to handle the first name validation logic."""
    message = 'First name must be greater than 1 character.'
    return self._check_condition(len(first_name) < 2, message)

  def _email_valid(self, email: str) -> bool:
    """Helper function used to handle the email validation logic."""
    return self._check_condition("@" not in email, 'Invalid email address!')

  def _password_valid(self, password: str, confirm_password: str) -> bool:
    """Helper function used to handle the password validation logic"""
    status = self._check_condition(
              len(password) < 6, 
              'Password must be at least 6 characters long.'
            )
    status = self._check_condition(
              password != confirm_password, 
              "'Password' and 'Confirm Password' must match."
            )
    return status

  def _email_duplicate_check(self, email: str, message: str) -> bool:
    """Helper function used to check the User database for a duplicate entry."""
    condition = User.query.filter_by(email=email).first()
    return self._check_condition(condition, message)

  def _note_duplicate_check(self, title: str, message: str) -> bool:
    """Helper function used to check the Note database for a duplicate entry."""
    condition = Note.query.filter_by(title=title).first()
    return self._check_condition(condition, message)

  @staticmethod
  def _check_condition(condition: bool, message: str, category: str = 'error') -> bool:
    """Helper function used to check a condition. If the condition is true, the function displays a given flash message to the screen and returns the value True. Otherwise, it returns False."""
    if condition:
      flash(message, category=category)
      return True
    else:
      return False

def validate_note_form(data: dict) -> bool:
  """Used to validate the search box on the Post Search page. Returns a flash message and True if the length of the query is too small. Else, returns False."""
  fv = FormValidation()
  errors: list = []

  errors.append(fv._note_duplicate_check(data['title'], "A note with that title already exists!"))
  errors.append(fv._check_condition(len(data['title']) < 1, "Title is too short!"))
  errors.append(fv._check_condition(len(data['note']) < 1, "Note content is too short!"))

  if not any(errors):
    return True
  return False
