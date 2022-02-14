from django.urls import path
from . import views
from .views import SignUpView, ChangePasswordResetDoneSuccessView, ChangePasswordResetDoneView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('password_change/', ChangePasswordResetDoneView.as_view(), name='password_change'),
    path('password_change/done/', ChangePasswordResetDoneSuccessView.as_view(), name='password_change_done'),
]
