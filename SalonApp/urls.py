from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('payrollapp/', include('payrollapp.urls')),
    path('admin/', admin.site.urls),
]