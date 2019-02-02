from django.urls import path,include
from . import views
urlpatterns = [
    path('web/', include("app1.urls") ),
]
