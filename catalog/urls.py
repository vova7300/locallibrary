from django.urls import path, re_path
from . import views
#from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

