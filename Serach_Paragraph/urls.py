"""
URL configuration for Serach_Paragraph project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from Search_paragraph_logic.views import (create_user,get_user,
                                           create_paragraph, get_paragraph,
                                            search_word_in_paragraph,)


urlpatterns = [

    path('users/', create_user, name='create_user'),
    path('users/<int:user_id>/', get_user, name='get_user'),
    path('paragraphs/<int:paragraph_id>/', get_paragraph, name='get_paragraph'),
    path('paragraphs/create/', create_paragraph, name='create_paragraph'),
    path('search-word/', search_word_in_paragraph, name='search_word_in_paragraph'),
]