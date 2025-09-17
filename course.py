from flask_restx import Namespace, Resource, fields
from flask import request
from models import Course

course_ns = Namespace('course', description='This is a course namespace')

#this is a database serializer
course_model = course_ns.model(
  "course",
  {
    "id" : fields.Integer(),
    "name" : fields.String(),
    "description" : fields.String(),
    "credits" : fields.Integer()
  }
)

@course_ns.route('/courses')
class CoursesResource(Resource):
  @course_ns.marshal_list_with(course_model)
  def get(self):
    all_course = Course.query.all()
    return all_course

  @course_ns.marshal_with(course_model)
  @course_ns.expect(course_model)
  def post(self):
    data = request.get_json()
    new_course = Course(
      name = data.get('name'), 
      description = data.get('description'), 
      credits = data.get('credits')
    )
    new_course.save()

    return new_course, 201
  
@course_ns.route('/courses/<int:id>')
class CourseResource(Resource):
  def delete(self, id):
    course_to_delete = Course.query.get_or_404(id)
    course_to_delete.delete()

    return {'message' : f'the course {course_to_delete.name} has been removed'}

  @course_ns.marshal_with(course_model)
  @course_ns.expect(course_model)
  def put(self, id):
    data = request.get_json()
    course_to_update = Course.query.get_or_404(id)
    course_to_update.update(data.get('name'), data.get('description'), data.get('credits'))

    return course_to_update