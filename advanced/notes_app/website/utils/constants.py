"""
Contains all constant variables and flags.
"""

APP_SECRET_KEY = b'[SECRET_KEY]'

DB_NAME = "[DATABASE_NAME].db"

CONFIG_SETTINGS = {
  'SECRET_KEY': APP_SECRET_KEY,
  'SQLALCHEMY_DATABASE_URI': f'sqlite:///{DB_NAME}',
  'SQLALCHEMY_TRACK_MODIFICATIONS': False
}
