from django.urls import path
from . import views
from .views import AuthorListView, AuthorDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:primary_key>', views.book_detail_view, name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
