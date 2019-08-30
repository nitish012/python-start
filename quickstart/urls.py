from django.conf.urls import url
from django.urls import path
# from rest_framework import routers
from quickstart import views


urlpatterns = [
    path('students/',views.StudentviewSet.as_view({'get':'list','post':'create'})),
    path('students/<int:pk>/',views.StudentviewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('teachers/',views.TeacherviewSet.as_view({'get':'list','post':'create'})),
    path('teachers/<int:pk>/',views.TeacherviewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
     
    path('departments/',views.DepartmentViewSet.as_view({'get':'list','post':'create'})),
    path('departments/<int:pk>/',views.DepartmentViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),

    path('reportcards/',views.ReportCardViewSet.as_view({'get':'list','post':'create'})),
    path('reportcards/<int:pk>/',views.ReportCardViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
             
]
