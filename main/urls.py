from django.urls import path
from main import views

urlpatterns= [
    path('', views.index, name='index'),
    path('college/<int:pk>', views.CollegeDetail.as_view(), name='college'),
    path('student/<int:pk>', views.StudentDetail.as_view(), name='student'),
    path('college/', views.CollegeList.as_view(), name='college_list'),
    path('college_create/', views.CollegeCreate.as_view(), name="college_create"),
    path('college_update/<int:pk>', views.CollegeUpdate.as_view(), name='college_update'),
    path('student_create/', views.StudentCreate.as_view(),name="student_create"),
    path('student_delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
    path('college_delete/<int:pk>', views.CollegeDelete.as_view(), name='college_delete'),
    path('student_update/<int:pk>', views.StudentUpdate.as_view(), name='student_update')
]