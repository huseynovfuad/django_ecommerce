from django.urls import path
from . import views

app_name = "products-api"

urlpatterns = [
    path("list/", views.ProductListView.as_view(), name="list"),
    path("create/", views.ProductCreateView.as_view(), name="create"),
    path("detail/<slug>/", views.ProductRetrieveUpdateDestroyView.as_view(), name="detail"),
    # path("update/<slug>/", views.ProductUpdateView.as_view(), name="update"),
    # path("delete/<slug>/", views.ProductDeleteView.as_view(), name="delete"),
]
