from django.urls import path
from .views import *

urlpatterns = [
    path('List/', prof_list, name='prof_list'),
    path('/<str:name>', prof_details, name='prof_details'),
    path('Update/<int:id>/', prof_update, name='prof_update'),
    path('Add/', prof_add, name='prof_add'),
    path('Delete/<int:id>/', prof_delete, name='prof_delete'),
]
