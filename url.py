from django.contrib import admin
from django.urls import path, include
from accounts import views as account_views
from forum import views as forum_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', account_views.register, name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('dashboard/', forum_views.dashboard, name="dashboard"),
    path('like/<int:post_id>/', forum_views.like_post, name="like_post"),
    path('profile/update/', account_views.profile_update, name="profile_update"),
]
