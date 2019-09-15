from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_book',views.new_book),
    path('books/<int:num>/',views.show_book),
    path('add_author/<int:num>/',views.add_author),
    path('authors',views.show_authors),
    path('authors/<int:num>',views.author_info),
    path('new_author',views.new_author),
    path('add_book/<int:num>',views.add_book),
]