from django.urls import path
from librarian import views
urlpatterns=[
    path('showall',views.showall,name="view_all_books"),
    path('showavailable',views.showavailable,name="available_books"),
    path('showissued',views.showissued,name="issued_books"),
    path('showrequest',views.showrequest,name="issued_books"),
]