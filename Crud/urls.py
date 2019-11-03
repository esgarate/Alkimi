from django.urls import path
from . import views
from django.conf.urls import url
from .views import  pagelogout
urlpatterns = [
#    path('', views.Crud, name='Crud'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('post/', views.postview, name='post'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    url(r'^logout', pagelogout, name='logout'),

]
