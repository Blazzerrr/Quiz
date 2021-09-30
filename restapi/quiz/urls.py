from django.urls import path
from . import views


urlpatterns = [
    path('quizes/', views.QuizView.as_view(), name='quizes'),
    path('questions/', views.QuestionView.as_view(), name='questions'),
    path('get_answers/', views.UserView.as_view(), name='answers'),
    path('send_answer/', views.AnswerView.as_view(), name='send_answer'),
]
