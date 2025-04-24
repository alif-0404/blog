from django.urls import path 
from .views import BlogListView , BlogDetalViews

urlpatterns = [
    path('post/<int:pk>/', BlogDetalViews.as_view() , name = 'post_detail') ,
    
    path('' , BlogListView.as_view() , name="home")
]