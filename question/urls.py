from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('subject/<int:subject_id>', subject_view, name='subject'),
    path('add', add_question, name='add'),
    path('add_subject', add_subject, name='add_subject'),
    path('edit/<int:question_id>', edit_question, name='edit'),
]
