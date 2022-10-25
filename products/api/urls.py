from django.urls import path
from . import views

app_name = "products-api"

urlpatterns = [
    path("list/", views.ProductListView.as_view(), name="list"),
    path("detail/<slug>/", views.ProductRetrieveView.as_view(), name="detail"),
]
