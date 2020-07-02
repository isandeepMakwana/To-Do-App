from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add_todo',views.add_todo, name='add_todo'),
    path('delete_todo/<int:todo_id>',views.delete_todo, name='delete_todo'),
    
]