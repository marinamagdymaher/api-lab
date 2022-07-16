from django.urls import path
from .views import *

urlpatterns = [
    path('overview',overview),
    path('list',list),
    path('list/<id>',list),
    path('GET-COURSE/<id>',getCourse),
    path('insert/',insert),
    path('update/',update),
    path('delete/',delete),
]
