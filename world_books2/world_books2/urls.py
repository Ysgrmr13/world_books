from django.contrib import admin
from django.urls import path, re_path, include
from catalog import views
from catalog.views import BookDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    re_path(r'^books/$', views.Logo, name='books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    # re_path(r'^book/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.author_list, name='authors'),
    path('accounts/', include('django.contrib.auth.urls')),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]
