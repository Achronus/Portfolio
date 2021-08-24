from werkzeug.security import generate_password_hash

from website.extensions import db
from website.models import User, Note

class DataHandler:
  """Handles the functionality for creating users, notes, and search history."""
  def create_user(self, data: dict) -> User:
    """Creates and returns a new user that is stored within the database."""
    new_user = User(
      email = data['email'], 
      first_name = data['firstName'],
      password = generate_password_hash(data['password'], method='sha256')
    )
    self._add_item_to_db(new_user)
    return new_user
  
  def create_note(self, data: dict, current_user: User) -> None:
    """Creates a new note and stores it within the database."""
    new_note = Note(
      title = data['title'],
      text = data['note'],
      user_id = current_user.id
    )
    self._add_item_to_db(new_note)

  @staticmethod
  def _add_item_to_db(item: db.Model) -> None:
    """Helper function that adds a given db.Model to the database."""
    print(f'Created {item}')
    db.session.add(item)
    db.session.commit()

  @staticmethod
  def delete_item_from_db(item: db.Model) -> None:
    """Deletes an a given db.Model from the database."""
    db.session.delete(item)
    db.session.commit()
