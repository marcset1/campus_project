from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
	path('admin/', admin.site.urls),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login_view, name='login'),
]


