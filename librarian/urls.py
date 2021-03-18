from django.urls import path
from librarian import views
urlpatterns=[
    path('all',views.showall,name="view_all_books"),
    path('available',views.showavailable,name="available_books"),
    path('issued',views.showissued,name="issued_books"),
]