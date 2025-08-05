"""
URL configuration for codetutor_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views  # Add this
from assistant import views as main_views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('core.urls')),
    
    # Auth routes
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    path('assistant/', include('assistant.urls')),
    path('chat/', main_views.chat_interface, name='chat_interface'),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path, include 
# from assistant import views as main_views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('core.urls')),
#     path('signup/', main_views.signup_view, name='signup'),
#     path('login/', main_views.login_view, name='login'),
#     path('logout/', main_views.logout_view, name='logout'),
#     path('assistant/', include('assistant.urls')),




