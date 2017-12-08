from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/',views.NewqView.as_view(), name='addquestion'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/posts/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/likes/', views.vote, name='vote'),
    path('newq/success/', views.newq, name='newq'),
    path('<int:pk>/newpost/', views.NewcView.as_view(), name='addchoice'),
    path('<int:question_id>/newpost/add',views.newc, name='newc'),
    path("<int:question_id>/delete/", views.delete, name="delete")
    ]