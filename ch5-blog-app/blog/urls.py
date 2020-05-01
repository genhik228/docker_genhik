from django.urls import path

from . import views


urlpatterns = [
    # path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    # path('', BlogListView.as_view(), name='home'),

    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
]
