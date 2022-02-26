from . import views
from django.urls import path


urlpatterns = [
    path('', views.DiscussionList.as_view(), name='home'),
    path('add_discussion/', views.AddDiscussion.as_view(), name='addDis'),
    path('discussion/<int:pk>/', views.DiscussionOpen.as_view(), name='disOpen'),

]