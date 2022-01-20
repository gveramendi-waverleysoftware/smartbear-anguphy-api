from django.urls import path

from apps.users.views import CurrentUserView, RegisterView, ChangePasswordView, UserDetailView, UserListView, UpdateUserView, DeleteUserView

urlpatterns = [
	path('/register', RegisterView.as_view()),
    path('/change_password/<int:pk>', ChangePasswordView.as_view()),
    path('', UserListView.as_view()),
    path('/<int:pk>', UserDetailView.as_view()),
    path('/update/<int:pk>', UpdateUserView.as_view()),
    path('/delete/<int:pk>', DeleteUserView.as_view()),
    path('/current_user', CurrentUserView.as_view()),
]