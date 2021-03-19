# Library Management system API


## Testing the API

There are two ways to test the API

1. Use the hosted api and make requests using an api client like postman
    https://libmanagementdeepakdpyqaz.herokuapp.com/

2. Install and run the backend system locally. Follow the steps to install the system locally.

    * Python-3.6 or greater is advised for proper functioning
    * Clone the Repository from the github link: 
     [Library Management](https://github.com/deepakdpyqaz/libmanage)
    * Create a python virtual environment using the shell command
    ```shell
        python -m venv env
    ``` 
    This will create a virtual environment.
    * Activate the environment using shell command
    ```shell
        env/Scripts/activate
    ```
    * Install the required dependencies by using the shell command
    ```shell
        pip install -r requirements.txt
    ```
    **_Note:_** Make sure that you are in the same directory in which requirements.txt exists and also the virtual environment is activated.

    * Start the local server using shell command 
    ```shell
        python manage.py runserver
    ```
    This will create a local server usually running on URL
    http://localhost:8000
3. Test the api with any api client like Postman

## API Guide

### Student's API's

* **/student/showavailable :** Returns a list of available books which a student can issue
   + Method: GET
   + Request parameters: None
   + Response-type: JSON  

   ![Showissued images](/mdimages/student_showall.png "Show issued")

* **/student/showaissued :** Returns a list of issued books for which student can make a request
   + Method: GET
   + Request parameters: None
   + Response-type: JSON  

   ![Showall images](/mdimages/student_showissued.png "Show issued")


**__NOTE__**: If your api-client shows error on making post request 
Error 403 request forbidden (CSRF verification failed). <br>
Then,
set the header X-CSRFToken as the cookie csrftoken
```js
"X-CSRFToken":getCookie(csrftoken)
/* getCookie is a user defined function to get the cookies send by server*/
```
* **/student/issue :** Issues a book for the student
   + Method: POST
   + Request-type: JSON
   + Request parameters: 
      1. username: Username of the student (use deepak for testing)
      2. book: Id of the book (use 0-106 for testing)
    + Response-type: JSON
    + Response: 
       * Success = Status code: 200 
       ```js
       {"Error":False}
       ```
       * Status Code 406 = A json is returned with error in error parameter
       ```js
       {"Error":"Book not found"}
       ```
    ![issuebook](/mdimages/student_issue.png "Issue book")
    ![issuebook](/mdimages/issue_error.png "Issue Error")

* **/student/return :** Returnss a book for the student
   + Method: POST
   + Request-type: JSON
   + Request parameters: 
      1. username: Username of the student (use deepak for testing)
      2. book: Id of the book (use 0-106 for testing)
    + Response-type: JSON
    + Response: 
       * Success = Status code: 200 
       ```js
       {"Error":False}
       ```
       * Status Code 406 = A json is returned with error in error parameter
       ```js
       {"Error":"Invalid book and student data"}
       ```
    ![returnbook](/mdimages/student_return.png "Return book")

* **/student/request :** Returnss a book for the student
   + Method: POST
   + Request-type: JSON
   + Request parameters: 
      1. username: Username of the student (use deepak for testing)
      2. book: Id of the book (use 0-106 for testing)
    + Response-type: JSON
    + Response: 
       * Success = Status code: 200 
       ```js
       {"Error":False}
       ```
       * Status Code 406 = A json is returned with error in error parameter
       ```js
       {"Error":"Book not found"}
       ```
    ![returnbook](/mdimages/student_request.png "Request book")

### Librarian's API's
* **/librarian/showall :** Returns a list of all books
   + Method: GET
   + Request parameters: None
   + Response-type: JSON  

   ![showall images](/mdimages/librarian_showall.png "Show all")

* **/librarian/showavailable :** Returns a list of all available books (Not issued)
   + Method: GET
   + Request parameters: None
   + Response-type: JSON  

   ![showavailable images](/mdimages/librarian_showavailable.png "Show available")

* **/librarian/showissued :** Returns a list of issued books along with student's info
   + Method: GET
   + Request parameters: None
   + Response-type: JSON 
   + Response-info: student property contains information about student who issued book (username, name) and book property contains information about book (book_id, name) 

   ![showissued images](/mdimages/librarian_showissued.png "Show issued")

* **/librarian/showrequest :** Returns a list of requested books along with student's info
   + Method: GET
   + Request parameters: None
   + Response-type: JSON  
   + Response-info: student property contains information about student who requested book (username, name) and book property contains information about book (book_id, name) 

   ![showrequest images](/mdimages/librarian_showrequest.png "Show request")


## Database
* Data inside the database would be different on the hosted api and locally installed api
* You can add, update, create data directly using the django-admin database on url "/admin" on your browser 
   + username:  admin
   + password: pass@admin