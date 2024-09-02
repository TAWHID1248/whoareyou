from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('myapp.urls')),  # Include the app's URLs
    path('', lambda request: redirect('search_phone_number')),  # Redirect to search page
]
