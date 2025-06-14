
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('excercise_execution/', include('excercise_execution.urls', namespace='excercise_execution')),
    path('', include('excercise_execution.urls', namespace='excercise_execution')),
    
]