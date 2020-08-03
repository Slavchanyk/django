from django.urls import path
from .views import UserView

app_name = "orders"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', UserView.as_view()),
    path('upload-csv/', UserView.upload_csv, name="users_upload"),
]