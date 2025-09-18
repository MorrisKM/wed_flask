from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from config import DevConfig
from models import Course
from flask_cors import CORS
from exts import db
from course import course_ns

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

api = Api(app, doc="/docs")
api.add_namespace(course_ns)
CORS(app)

migrate = Migrate(app, db)



if __name__ == '__main__':
  app.run(port=5005)