from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('blog/', views.BlogListView.as_view(), name="blog"),
    path('create/', views.BlogCreateView.as_view(), name="create"),
]