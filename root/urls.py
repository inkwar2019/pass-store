from django.urls import path
from .views import home, password_generate, PasswordList, PasswordDetails, PasswordCreate, PasswordUpdate

urlpatterns = [
    path('', home, name="home"),
    path('generate-password', password_generate, name="password-generate"),
    path('password-list/', PasswordList.as_view(), name="password-list"),
    path('password-create/', PasswordCreate.as_view(), name="password-create"),
    path('<pk>/password-update', PasswordUpdate.as_view(), name="password-update"),
    path('<pk>/password-details', PasswordDetails.as_view(),
         name="password-details"),
]
