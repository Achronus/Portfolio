from flask import Blueprint, render_template
from flask_login import current_user

err = Blueprint('err', __name__)

@err.errorhandler(404)
def page_not_found(e):
  """Handles pages that cannot be found (404 error)."""
  return render_template('404.html', user=current_user), 404
