from django.urls import path
from .views import *

urlpatterns = [
    path('List/', student_list, name='student_list'),
    path('/<str:name>', student_details, name='student_details'),
    path('Add/', student_add, name='student_add'),
    path('Update/<int:id>/', student_update, name='student_update'),
    path('Delete/<int:id>/', student_delete, name='student_delete'),
]
