from .models import Book, Author, BookInstance, Genre
from django.shortcuts import render

from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Book

from django.shortcuts import render
from .models import Author, BookInstance

def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Get the number of visits to this page
    num_visits = request.session.get('num_visits', 0)  # Default is 0 if not set
    num_visits += 1
    request.session['num_visits'] = num_visits  # Save updated count in session

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  # Your own name for the list as a template variable
    queryset = Book.objects.all()  # Fetch all books
    template_name = 'book_list.html'  # Specify your own template name/location



def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'book_detail.html', {'book': book})



from django.views import generic
from .models import Author

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'



