Team Name: Segmentation_faulters

Team Members:

: Dishank Aggarwal (21q05r003)
: Vivek Raj (213050053)
: Ashish Verma (213050058)





1. Problem Statement or Motivation:
    1.  Fulfilling all the student's and IITB resident's needs at one place 
        will help students and residents of IITB to save their precious time.       
        They just need to use our platform in order to use the services.This
        will also helps vendor to bring in more costumers.

2. Sell your product/service (One sentence).
    1. Connecting all the offline services to online to make life easy for the students and the residents of IITB.

3. List of features
    1. Login
    2. Signup
    3. Signout
    4. My Orders
    5. Place order
    6. Mail confirmation
    7. Gulmohar
    8. Grocery
    9. Hair Salon
    10. about page
    11. Vendor side pages for all the vendors: Gulmohar, Hairsalon and Grocery.

4. Technology Stack (highlight ones learnt in CS699)
    1. Pyhton
    2. Sphinx
    3. HTML, CSS, JavaScript
    4. Sqlite3
    5. MailTrap

5. List of deliverables (tick mark those which are complete).
    1. Secure Login and Register functionality(HOME PAGE).(DONE)
    2. Interface for student: In order to use the services available.(DONE)
    3. Interface for Gulmohar: We will provide a cart option, where
        student can select item present at Gulmohar and then order from
        the interface.(DONE)
    4. Interface for Hair Salon: We will provide a google form like
        functionality , on filling the form a mail will be sent to the Hair
        Cutting shop manager and he will call according to availability of
        slot.(DONE)
    5. Interface for grocery Shop: We will again provide a cart thing
        where student or residents can order the daily needs then confirm
        the order.(DONE)
    6. We are also going to link some services which are already present
        online like aroma , badminton court facilities.(DONE)

6. Hardware/Software Requirements.
    1. Hardware:
        Any Pc with Windows or Linux
    2. Software:
        Python, Django and web Browser

7. Well explained, “how to operate”.

    1. To get started with the project you should first run the virtual environment that is "venv" with the command source venv/bin/activate
    2. Then start the server with the command python3 IITB_Services/manage.py runserver
    3. First page is the login and sign up page on which user has to login or register
    4. After login the user has to choose the services from the list of services.
    5. Gulmohar : user can order the dishes that are available at that time and when user click on purchase button a mail will be sent       to both the user and the gulmohar email about the order detals.
    6. HairSalon : user can select the services provided by the salon and has to enter their mobile no and when user click on submit button a mail will be sent to both the user and the hair salon  email about the order detals.
    7. Grocery: user can order the items that are available at that time and when user click on purchase button a mail will be sent to both the user and the grocery vendor email about the order detals.
    8. User can view their order by visiting the myorders section in the navbar.
    9. Gulmohar admin , hairsalon admin  , Grocery admin has special usernames respectively which will take them to admin functionality 
    10. Gulmohar can change the item available in the restaurant and can also change the order completion status .
    11. Haisalon can  change the order completion status .
    12. Grocery can change the order completion status .
    13. We have also linked the existing functionalities like badminton court booking , aroma , gymkhana booking portal
    14. username and password of gulmohar vendor is "gulmohar" and "Gulmohar" repectively.
    15. username and password of grocery vendor is "groceryadmin" and "Grocery" repectively.
    16. username and password of gulmohar vendor is "hairsalon" and "1234" repectively.

    

8. Primary stakeholders of the product/service built
    1. The residence IITB and the students living in the hostels of IITB.

9. Team details along with the contribution.
    Team Members:
        : Dishank Aggarwal (21q05r003)
        : Vivek Raj (213050053)
        : Ashish Verma (213050058)
    
    Contribution
        1. Gulmohar Interface is completed by Dishank
        2. Grocery Interface is completed by Vivek
        3. HairSalon Interface is completed by Ashish
        4. Homepage is completed by Dishank, Ashish , Vivek
        5. login and authentication is done by Dishank
        6. Email feature is done by Vivek
        7. Database is manage by Dishank
        8. Vendor side page is manage by Ashish
        9. About page is completed by Vivek


10. Path to Code Documentation (index.html).
    Sphinx:
        Segmentation_faulters\documentation_Sphinx\_build\html\index.html
    JSDoc:
        Segmentation_faulters\documentation_JSDoc\docs\index.html
