"""
URL configuration for educator_site project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authorization_app.views import educator_registration, educator_profile, main_page, profile_page, login_view, logout_view, add_refresher_course, add_science_work, delete_science_work, delete_refresher_course, add_subject_to_educator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', main_page, name='main_page'),
    path('profile_page/', profile_page, name='profile_page'),
    path('educator/register/', educator_registration, name='educator_registration'),
    path('educator/profile/', educator_profile, name='educator_profile'),
    path('educator/login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path('add-course/', add_refresher_course, name='add_course'),
    path('add-science-work/', add_science_work, name='add_science_work'),
    path('delete-science-work/<int:pk>/', delete_science_work, name='delete_science_work'),
    path('delete-refresher-course/<int:pk>/', delete_refresher_course, name='delete_refresher_course'),
    path('add-subject/', add_subject_to_educator, name='add_subject'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
