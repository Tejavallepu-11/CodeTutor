from django.urls import path
from . import views


urlpatterns = [
    path('chat/', views.chat_interface, name='chat_interface'),
    path('ask/', views.ask_gpt, name='ask_gpt'),
    # path('', main_views.home_view, name='home'),
    # path('signup/', main_views.signup_view, name='signup'),
    # path('login/', main_views.login_view, name='login'),
    # path('logout/', main_views.logout_view, name='logout'),

]
