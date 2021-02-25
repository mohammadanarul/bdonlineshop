from django.urls import path
from category.views import (
    category_list_page_view,
)

app_name = 'category'
urlpatterns = [
    path('category-list/<slug>/', category_list_page_view, name='category_list')
]