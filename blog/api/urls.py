from django.urls import path

from .views import EntryList, EntryDetail

urlpatterns = [
    path('entries/', EntryList.as_view(), name='entry_list'),
    path('entries/<int:pk>', EntryDetail.as_view(), name='entry_detail')
]
