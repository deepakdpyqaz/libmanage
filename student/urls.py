from django.urls import path
from student import views
urlpatterns=[
    path("showavailable",views.showavailable,name="available_books"),
    path("showissued",views.showissued,name="issued_books"),
    path("issue",views.issueBook,name="issue_book"),
    path("return",views.returnBook,name="return_book"),
    path("request",views.requestBook,name="request_book")
]