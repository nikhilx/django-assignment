from django.urls import path

from school import views

urlpatterns = [
    path('course', views.CourseListCreateView.as_view(), name=views.CourseListCreateView.name),
    path('course/<uuid:pk>', views.CourseRetrieveDestroyView.as_view(), name=views.CourseRetrieveDestroyView.name),

    path('teacher', views.TeacherListCreateView.as_view(), name=views.TeacherListCreateView.name),
    path('teacher/<uuid:pk>', views.TeacherRetrieveView.as_view(), name=views.TeacherRetrieveView.name),

    path('student', views.StudentListCreateView.as_view(), name=views.StudentListCreateView.name),
    path('student/<int:roll_no>', views.StudentRetrieveDestroyView.as_view(), name=views.StudentRetrieveDestroyView.name),
    path('student/<uuid:pk>/course', views.StudentCourseView.as_view(), name=views.StudentCourseView.name),

]
