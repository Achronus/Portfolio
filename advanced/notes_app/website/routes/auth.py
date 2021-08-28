from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, AnonymousUserMixin

from website.utils.login_handler import LoginHandler
from website.utils.form_validation import FormValidation

auth = Blueprint('auth', __name__)
forms = FormValidation()
login_handler = LoginHandler()

@auth.route('/login', methods=['GET', 'POST'])
def login():
  """Handles the login pages functionality."""
  if not isinstance(current_user, AnonymousUserMixin):
    return redirect(url_for('views.home'))

  if request.method == "POST":
    data = request.form.to_dict()
    valid_form = forms.validate_login(data)

    if valid_form:
      login_handler.sign_in_user(data)
      return redirect(url_for('views.home'))

  return render_template('login.html', login_form=True, user=current_user)

@auth.route('/logout')
@login_required
def logout():
  """Handles logout functionality."""
  login_handler.logout_current_user()
  return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  """Handles the sign up pages functionality."""
  if not isinstance(current_user, AnonymousUserMixin):
    return redirect(url_for('views.home'))
  
  if request.method == "POST":
    data = request.form.to_dict()
    valid_form = forms.validate_signup(data)

    if valid_form:
      login_handler.create_and_sign_in_user(data)
      return redirect(url_for('views.account_created'))
  
  return render_template('sign_up.html', user=current_user)
