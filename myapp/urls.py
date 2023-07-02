from django.urls import path
from .views import index, pass_page

urlpatterns = [
    path('', index, name='password_reset'),
    path('reset/', pass_page, name='pass_page'),

]
