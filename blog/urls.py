from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('blog/', views.BlogListView.as_view(), name="blog"),
    path('create/', views.BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', views.BlogDetailView.as_view(), name="details"),
    path('<int:pk>/update/', views.BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name="delete")
]