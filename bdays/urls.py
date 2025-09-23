from django.urls import path
from .views import (
    BdaysListView,
    BdaysCreateView,
    BdaysDetailView,
    BdaysUpdateView,
    BdaysDeleteView,
)

app_name = "bdays"
urlpatterns = [
    path('', BdaysListView.as_view(), name='bday-list'),
    path('<int:id>/', BdaysDetailView.as_view(), name='bday-detail'),
    path('<int:id>/delete/', BdaysDeleteView.as_view(), name='bday-delete'),
    path('create/', BdaysCreateView.as_view(), name='bday-create'),
    path('<int:id>/update/', BdaysUpdateView.as_view(), name='bday-update'),
]
