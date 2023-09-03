
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Company Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome Admins"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workflow.urls')),]