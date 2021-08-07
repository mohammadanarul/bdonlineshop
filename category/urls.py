from django.urls import path
from category.views import (
    CategoryListPageView,
)

app_name = 'category'
urlpatterns = [
    path('category-list/<slug>/', CategoryListPageView.as_view(), name='category_list')
]