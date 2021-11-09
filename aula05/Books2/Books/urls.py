"""Books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.books_page),
    path('books/<int:i>', views.book_details),
    path('booksearch/', views.booksearch),
    path('authorsearch/', views.authorsearch),
    path('authors/', views.authors_page),
    path('authors/<int:i>', views.author_details),
    path('authors/<int:i>/edit', views.author_edit),
    path('authors/add', views.author_insert),
    path('publishers', views.publishers_page),
    path('publishers/<int:i>', views.publisher_details),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
