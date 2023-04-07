from django.contrib import admin
from django.urls import path
from . import views
app_name='web'

urlpatterns = [
    path('',views.index, name="index"),
    path('job-lists',views.job_lists, name="job_lists"),
    path('dash-post-job',views.dash_post_job, name="dash_post_job"),
    path('contact/', views.contact,name="contact" ),
    path('candidate_login',views.candidate_login, name='candidate_login'),
    path('employer_login',views.employer_login, name="employer_login"),
    
    
    path('employer_register',views.employer_register, name='employer_register'),
    path('candidate_logout',views.candidate_logout,name='candidate_logout'),
    path('candidate_register',views.candidate_register,name="candidate_register"),
    
]