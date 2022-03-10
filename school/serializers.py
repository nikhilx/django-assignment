from rest_framework import serializers

from school.models import Course, Student, Teacher


class CourseSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    def get_duration(self, instance):
        if instance.start_date == instance.end_date:
            return '1 day'
        return f'{(instance.end_date - instance.start_date).days} days'

    class Meta:
        model = Course
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'roll_no', 'courses']


class TeacherSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'course']
