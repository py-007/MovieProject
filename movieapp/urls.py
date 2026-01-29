from django.urls import path
from movieapp import views

urlpatterns = [
    path('form/',views.movie_form,name = 'form'),
    path('all/',views.all_movies,name = 'movies'),
    path('delete/<int:id>',views.delete_view,name = 'delete'),
    path('update/<int:id>',views.update_view,name = 'update'),
]