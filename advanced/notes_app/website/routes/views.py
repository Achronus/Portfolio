import json
from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_required, current_user, AnonymousUserMixin

from website.models import Note
from website.utils.form_validation import validate_note_form
from website.utils.data_handler import DataHandler

views = Blueprint('views', __name__)
data_handler = DataHandler()

@views.route('/')
def home():
  """Handles the homepage functionality."""
  if not isinstance(current_user, AnonymousUserMixin):
    return redirect(url_for('views.notes'))
  
  return render_template("index.html", user=current_user)

@views.route('/success')
def account_created() -> str:
  """Handles the account created page functionality."""
  return render_template("account_created.html", user=current_user)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
  """Handles the notes page functionality."""
  if request.method == 'POST':
    data = request.form.to_dict()
    valid_form = validate_note_form(data)

    if valid_form:
      data_handler.create_note(data, current_user)
      flash('Note created!', category="success")
      return redirect(url_for('views.notes'))
  
  return render_template("notes.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
  """Handles the deletion of a Note from the database."""
  query = json.loads(request.data)
  note_id = query['noteId']
  note = Note.query.get(note_id)

  # Check note exists
  if query:
    # Check user is signed in
    if note.user_id == current_user.id:
      data_handler.delete_item_from_db(note)
      flash("Note has successfully been deleted!", category="success")
  
  # Return an empty response
  return jsonify({})
