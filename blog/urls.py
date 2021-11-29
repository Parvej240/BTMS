from .views import BlogDelete, BlogDetailsView, BlogUpdate, BlogView, InsertBlog, OwnBlogView
from django.urls import path
from .views import like
urlpatterns = [
    path('add-blog/', InsertBlog.as_view(), name='addBlog'),
    path('blogs/', BlogView.as_view(), name='viewBlog'),
    path('own-blog/', OwnBlogView.as_view(), name='ownBlog'),
    path('blog-update/<pk>/', BlogUpdate.as_view(), name='blog-update'),
    path('blog-details/<pk>/', BlogDetailsView.as_view(), name='blog-details'),
    path('blog-delete/<pk>/', BlogDelete.as_view(), name='blog-delete'),
    path('like/', like, name='like'),
]
