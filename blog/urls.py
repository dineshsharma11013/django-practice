from django.urls import path
from .views import *


urlpatterns = [
    path('', Home),
    path('contact', Contact.as_view()),
    path('contact/contact-edit/<id>', ContactEdit.as_view())
]






