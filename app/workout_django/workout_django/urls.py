from django.contrib import admin
from django.urls import include, path
# from django.utils.encoding import escape_uri_path

from .views import CompositeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('excercise_execute/', include('excercise_execution.urls', namespace='excercise_execution')),
    # path('', include('excercise_execution.urls', namespace='excercise_execution')),
    path('composite/', CompositeView.as_view(), name='composite'),
    
]