from django.urls import path

from . import views


urlpatterns = [
    path('', views.course_list),
    path('(?P<pk>\d+)/$', views.course_detail),
]