from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from rest_framework.exceptions import ParseError


class ValidationUtils:

    @classmethod
    def validate_email(cls, email):
        """
        Validates if the input is an email. If not, raises ParseError (400)
        """
        try:
            validate_email(email)
        except ValidationError:
            raise ParseError(detail=f'{email} is not a valid email')