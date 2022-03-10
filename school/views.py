from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from school.models import Course, Student, StudentCourse, Teacher
from school.serializers import CourseSerializer, StudentSerializer, TeacherSerializer
from school.service import CourseService, StudentService, TeacherService


class CourseListCreateView(generics.ListCreateAPIView):
    name = 'Get/Create Course'
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

    def post(self, request, *args, **kwargs):
        CourseService.validate_request(request)
        return super().post(request, *args, **kwargs)


class CourseRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    name = 'Get/Create Course'
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()

        return Response(self.get_serializer(instance).data)


class TeacherListCreateView(generics.ListCreateAPIView):
    name = 'Get/Create Teacher'
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def post(self, request, *args, **kwargs):
        TeacherService.validate_request(request)
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(course_id=self.request.data['course_id'])


class TeacherRetrieveView(generics.RetrieveAPIView):
    name = 'Get/Create Teacher'
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentListCreateView(generics.ListCreateAPIView):
    name = 'Get/Create Student'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        StudentService.validate_request(request)
        return super().post(request, *args, **kwargs)


class StudentRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    name = 'Get/Create Student'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'roll_no'


class StudentCourseView(generics.ListCreateAPIView):
    name = 'Add Course to a Student'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        student = self.get_object()
        course = get_object_or_404(Course, id=request.data['course_id'])
        student.courses.add(course)

        return Response(self.get_serializer(student).data)

    def get(self, request, *args, **kwargs):
        student = self.get_object()
        course_id_list = StudentCourse.objects.filter(student_id=student.id,
                                                      course__is_active=True).values_list('course_id', flat=True)
        course_qs = Course.objects.filter(id__in=course_id_list)
        return Response(CourseSerializer(course_qs, many=True).data)
