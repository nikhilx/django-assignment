from rest_framework.exceptions import ParseError

from school.utils import ValidationUtils


class TeacherService:
    @staticmethod
    def validate_request(request):
        valid_keys = ['name', 'email']
        if not all(key in request.data for key in valid_keys):
            raise ParseError(detail='Required fields are missing from the request')

        ValidationUtils.validate_email(request.data['email'])


class StudentService:
    @staticmethod
    def validate_request(request):
        valid_keys = ['name', 'roll_no', 'email']
        if not all(key in request.data for key in valid_keys):
            raise ParseError(detail='Required fields are missing from the request body')

        if not 1000 < int(request.data['roll_no']) < 9999:
            raise ParseError(detail='Roll no should be between 1000 and 9999')

        ValidationUtils.validate_email(request.data['email'])


class CourseService:
    @staticmethod
    def validate_request(request):
        valid_keys = ['name', 'start_date', 'end_date']
        if not all(key in request.data for key in valid_keys):
            raise ParseError(detail='Required fields are missing from the request body')

        if request.data['end_date'] < request.data['start_date']:
            raise ParseError(detail='End date cannot be earlier than start date')