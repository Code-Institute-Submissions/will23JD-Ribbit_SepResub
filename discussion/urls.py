from . import views
from django.urls import path


urlpatterns = [
    path('', views.DiscussionList.as_view(), name='home'),
    path('your_discussions', views.YourDiscussions.as_view(), name='yourDis'),
    path('add_discussion/', views.AddDiscussion.as_view(), name='addDis'),
    path('discussion/<int:pk>/', views.DiscussionOpen.as_view(), name='disOpen'),
    path('like/<int:pk>/', views.DiscussionLike, name='disLike'),
    path('downvote/<int:pk>/', views.DiscussionDownVote, name='downvote'),
    path('category/<str:cats>/', views.DiscussionCats, name='catsview'),
    path('discussion/<int:pk>/comments/', views.Comments.as_view(), name='comments'),
    path('category_list/', views.DiscussionCatsList, name='listCat'),
    path('discussion/edit/<int:pk>/', views.Edit.as_view(), name='editDis'),
    path('discussion/delete/<int:pk>/', views.Delete.as_view(), name='deleteDis'),
    path('discussion/edit/<int:pk>/comment/', views.EditComment.as_view(), name='editCom'),
    path('discussion/delete/<int:pk>/comment/', views.DeleteComment.as_view(), name='deleteCom'),

]