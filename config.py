from dotenv import load_dotenv
import os

load_dotenv()

class Config():
  SECRET_KEY = os.getenv("SECRET_KEY")
  DEBUG = True

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
  SQLALCHEMY_ECHO = True