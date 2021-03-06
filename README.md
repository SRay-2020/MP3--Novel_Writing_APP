

# Milestone project 3: Novel Writing App

### Using: HTML, CSS, JavaScript, Python, Flask, MongoDB and Materialize

#### Purpose - To build a full stack site that allows users to manage a common dataset about a particular domain. 
---

## Project Summary:
### The goal of this project will be to design and create a novel writing web based application using Python, JavaScript, HTML and CSS. The main goal for the user will be to create, read, update, delete files relating to their novels. The main goal of the site owner will be to have an application that assists their users in writing, and will have enough functionality that the users will spend time on the side and return. By using MONGODB this project will store and access user data and will quickly retrieve this data for viewing or modification.

### Link to Live Site - "https://mp3-novel-writing-app.herokuapp.com/"



<img src="static/img/mp3amiresponsive.png">


A digital render of how the site would look on different devices and screen sizes 


### Contents - 

* [**STRATEGY**](#strategy)

* [**USER STORIES**](#user-stories)

* [**SCOPE**](#scope)

* [**STRUCTURE**](#structure)

* [**SKELETON**](#skeleton)

* [**SURFACE**](surface)

* [**FEATURES**](#features)

* [**FUTURE FEATURES**](#future-features)

* [**TECHNOLOGIES USED**](#technologies-used)

* [**TESTING**](#testing)

* [**BUG FIXES**](#bug-fixes)

* [**IMPLEMENTATION ISSUES**](#implementation-issues)

* [**DEPLOYMENT**](#deployment)

* [**CREDITS**](#credits)

* [**CONTENT**](#content)

* [**MEDIA**](#media)

* [**ACKNOWLEDGEMENTS**](#acknowledgements)


### **STRATEGY**

#### SITE OWNER GOALS:
The main goal of this project is to create a full stack site which allows users the ability to create and access a dataset relating to their novels. This App will allow users to create book and chapter objects which they can read, edit and delete and will help give a more visual conceptualisation of what they are writing. By creating an application that has useful and practical functionality the site owner would benefit from return use which in the future could be monetised through subscription or advertisements. 

Target Audience:

- Writers 

### **User stories**

Website user -

1. As a user I want a visually appealing and smooth website experience
2. As a user I want to be given visual feedback about my actions 
3. As a website user I want to be able to navigate the website easily and intuitively
4. As a user I want a consistent experience, that is the same every time I come back to the website and on any device
5. As a user I want to have my information protected by a password

Writer - 

6. As a writer I want to be able to create new books which I can read, edit and delete
7. As a writer I want to be able to create new chapters which I can read, edit and delete
8. As a writer I want to be able to get information about how many books and chapters I have created
9. As a writer I want to write quick notes which I can store and see later
10. As a writer I want an application that is visually clean and simple to user so I can focus on my writing
11. As a writer I want an app that I can use on desktop, tablet or mobile

Website Owner - 

12. As the website owner I want the users to enjoy using my application
13. As the website owner I want users to stay on my site for as long as possible
14. As the website owner I want the users to return to my website
15. As the website owner I want users to be able to trust the security features that I have implemented

### **SCOPE**

This project will be a minimal viable product containing the aspects that are vital to functionality and an acceptable standard of aesthetic value, but with lots of opportunity to develop further in the future.

Functional specifications: 
- Navigation (Top Navbar and Sidebar)
- Create Book, Chapter and Notes features
- Display Book, Chapter and Notes features
- Edit Book, Chapter and Notes features
- Delete Book and Chatpter Features
- Card Flip mechanism (for Book page)
- Notepad modal display
- Login/Logout features
- Password protected user accounts


Content specifications:
- Data retrieval display (from MONGO DB using Flask)
- Custom artwork

### **STRUCTURE**

The website is laid out over 12 pages which can be broken down into 6 seperate areas. 
These areas are:

1. Registration Page ( for new users)
2. Login/Logout Pages (for existing users to login in using a username and password)
3. Book Pages - which includes  
     - Book Library: where all existing books can be viewed as flippable card objects, edited or deleted
     - Create New Book: which takes user to a page where they can add a new instance of a book object using a form
     - Edit Book: which takes user to a page where they can edit an existing book
4. Chapter Pages - which includes  
     - Chapters List: where all existing chapters can be viewed in a collapsible list, edited or deleted
     - Create New Chapter: which takes user to a page where they can create a new chapter using a form
     - Edit Chapter: which takes user to a page where they can edit an existing chapter
5. Notes - which includes
      -Add and Edit
      -Popup modal to display notes
6. User Profile Page - which includes information about their existing files

The relational logic of the Database being used were considered before the creation of the project and are outlined in the logic chart below which helps to visualise the how the database can be accessed. 

<img src="static/img/mp3logicchart.png"> 


### **SKELETON**

Differences between final design and wireframes:

There was some difference between the final design and the wireframes. By adding in a 'flip' function on the 'Books page' more information could be displayed to the user about their existng books and it gives a better feeling of a library. The user 'Profile page' was also enhanced to give users more feedback about their existing files including a return of how many individual chapters and books each author incldued. 

<img src="static/img/mp3wireframe.png"> 

##### Created at the outset of the project to direct the stylistic development. 

### **SURFACE**

Typography -
Two fonts were chosen for this project - 

The first of which is 'Grenze & Gotisch'  - This font was chosen for it's old world gothic printing aesthetic,  it is reminiscent of the font a type setter would have used and git in perfectly with the desired affect.

<img src="static/img/mp3samplefont.png"> 

The second font used is 'Sora' ??? This font was chosen because it's a simple non distracting font and one that a writer may be used to.

<img src="static/img/mp3sampletext2.png"> 

Colour scheme -

The author used Coolers.com to create a consistent and visually appealing colour palette for this project. Accessibility was also a concern so the author ensured that all colours of text used were done in a highly contrasting and visually pleasing manner .

<img src="static/img/mp3colourscheme.png"> 

Images -

The book covers were designed and created by the author to give the impression and feeling of an old library to enhance user expereience. 


### **FEATURES**

- Media responsiveness on all device sizes
- Navigation buttons that link to all pages
- Navigation buttons includes user feedback for click
- User can create unique login name and password to protect projects
- User can create, read, update and delete 'Book' objects
- User can create, read, update and delete 'Chapter' objects
- User can create and save quick notes
- Profile page with database query feedback (number of Books and Chatpers created)

### **FUTURE FEATURES**

- 'Character' creation objects to be included  
- Darkmode for night time use
- Further customisation of user 'Profile page' including user profile picture and more feedback
- Allow users create custom forms or inputs to database to recall (scenes etc.)
- Give users more control over notes, includng delete and edit


### **TECHNOLOGIES USED**

Python - For creating main application and majority of functionality

MongoDB - For storing and accessing Database

Flask - For wrapping functions and tools (Jinja and Werkzeug)

HTML ??? For creating pages

Css ??? For styling pages

Materialze ??? For design components and front end elements

JavaScript ??? For creating additional functions and interactive elements on project

JQuery - For initialising Materiaze components 

Heroku - For application deployment

Adobe XD ??? For creating wireframes

Adobe Photoshop ??? For editing images to consistent sizes and adjusting styles

Git ??? Used for Version control

Gitpod ??? For code editing and testing

GitHub ??? For storing repository

Chrome Dev Tools ??? For editing changes in real time and checking styles in different media sizes

Chrome Lighthouse ??? For checking page performance

W3C CSS - For validating CSS code

W3C HTML ??? For validating and ensuring HTML code was correct/valid.

Coolers (website) - For creating a custom colour palette for project

FreeFormatter (website) - For validating HTML code

AutoPrefixer Online ??? For CSS parsing and adding vendor prefixes

AmIResponsive (website) - To ensure site is responsive and create mockup

### **TESTING**

#### **Code tests -**

The CSS code was passed through W3C CSS Validator and final version contained no errors. It was also passed through AutoPrefixer Online to parse CSS and add vendor prefixes to ensure validity.

<img src="static/img/mp3cssvalidation.png">

The HTML code was passed through W3C HTML Validator and FreeFormatter.com to ensure final version contained no errors.

The JavaScript was tested using JSHint to ensure no errors included in final version. 

The Python code was tested using 'Python Tutor' and 'Extends Class - Python Syntax Checker'

#### **Dev tests -**

(i)Chrome Developer Tools -

Chrome Developer Tools were used throughout this project and were greatly relied on to make all manner of adjustments and changes to project.

(ii)Chrome Lighthouse -

Chrome Lighthouse was used to ensure that the website has been deployed in the most efficient way possible ??? the screen shots below reflect the score of this project under four headings 
    ??? Performance
    ??? Accessibility
    ??? Best Practices
    ??? SEO

To bring this project to score this high some changes were made in some of the categories to raise the score to be all registering at the highest score possible. 

These changes included - 
1. Performance: 
    ??? Removing ???unnecessary CSS??? 

This change increased score in Performance from 92% to 100%. 

2. Accessibility:
    ??? Changed colour contrast of site to improve Accessibility

 This change increased score in Accessibility from 90% to 95%.

3. Best Practices:

Could not change aspect ratio of image overlay to improve this score without losing the desired visual effect .

4. SEO:
    ??? Added meta description to document 
This change increased score from 80% to 82%. 

Remaining issue was to do with the 'robot.txt' score for search engine results, unfortunately this issue is beyond my own knowledge at the current time of writing this but I strive to gain an understanding and include these changes in future versions for full SEO optimisation.

<img src="static/img/mp3lighthouse.png">

#### **Function tests -**

This site was tested many times manually throughout the development process by the author and friends and family to ensure that it's functions behave exactly as they are intended to. This process was again repeated when hosted to ensure that there were no changes to functionality. 

Below are a list of the 
- Test cases
- Expected behaviour
- Observed Results
- Summary of expected behaviour and results 

Tests will be applied to all the pages included in the project, these pages will be referred to as:

 1. Book Page
 2. Chapter Page
 3. Book Add Page/Chapter Add Page
 4. Book Edit Page/Chapter Edit Page
 5. Profile Page
 6. Note Editor Page
 7. Login/Register

**Test Case I:** Initial Page Load and display

1. Book Page - 
- Expected Behaviour: Page will load correctly and promptly, with all elements in place where they should be.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

2. Chapter Page - 
- Expected Behaviour: Page will load correctly and promptly, with all elements in place where they should be.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

3. Book Add Page/Chapter Add Page - 
- Expected Behaviour: Page will load correctly and promptly, with all elements in place where they should be.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

4. Book Edit Page/Chapter Edit Page - 
- Expected Behaviour: Page will load correctly and promptly, with all elements in place where they should be.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

5. Profile - 
- Expected Behaviour: Page will load correctly and promptly, with all elements in place where they should be.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

6. Note Editor - 
- Expected Behaviour: Page will load correctly and promptly, with all elements in place where they should be.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

7. Login/Register - 

- Expected Behaviour: Page will load correctly and promptly, with all elements in place where they should be.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

**Test Case II:** Ensure all navigation links are displayed and work correctly for (a) - 'Logged Out' and (b) - 'Logged In' users

1. (a) Book Page - Logged out User
- Expected Behaviour: Links to 'Home', 'Login' and 'Register' all to appear on top navbar and links to 'Books' and 'Chapters' to appear on side navbar. 
  All should redirect to respective pages except Chapters which should redirect to 'Login' page and force login request.
- Observed Results: All links worked as intended and were satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

1. (b) Book Page - Logged In User
- Expected Behaviour: Links to 'Home', 'Note Editor' and 'Logout' all to appear on top navbar and links to 'Books', 'Chapters', 'Notepad' and 'Profile' to appear on side navbar. 
  All should redirect to respective pages except 'Notepad which should initiate notepad popup modal.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

2. (a) Chapter Page - Logged out User
- Expected Behaviour: Page will not display for logged out user.
- Observed Results: This page does not display for logged out users.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

2. (b) Chapter Page - Logged In User
- Expected Behaviour: Links to 'Home', 'Note Editor' and 'Logout' all to appear on top navbar and links to 'Books', 'Chapters', 'Notepad' and 'Profile' to appear on side navbar. 
  All should redirect to respective pages except 'Notepad which should initiate notepad popup modal.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

3. (a) Book Add Page/Chapter Add Page - Logged out User
- Expected Behaviour: Page will not display for logged out user.
- Observed Results: This page does not display for logged out users.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

3. (b) Book Add Page/Chapter Add Page - Logged In User
- Expected Behaviour: Links to 'Home', 'Note Editor' and 'Logout' all to appear on top navbar and links to 'Books', 'Chapters', 'Notepad' and 'Profile' to appear on side navbar. 
  All should redirect to respective pages except 'Notepad which should initiate notepad popup modal.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

4. (a) Book Edit Page/Chapter Edit Page - Logged out User
- Expected Behaviour: Page will not display for logged out user.
- Observed Results: This page does not display for logged out users.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

4. (b) Book Edit Page/Chapter Edit Page - Logged In User
- Expected Behaviour: Links to 'Home', 'Note Editor' and 'Logout' all to appear on top navbar and links to 'Books', 'Chapters', 'Notepad' and 'Profile' to appear on side navbar. 
  All should redirect to respective pages except 'Notepad which should initiate notepad popup modal.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

5. (a) Profile - Logged out User
- Expected Behaviour: Page will not display for logged out user.
- Observed Results: This page does not display for logged out users.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

5. (b) Profile - Logged In User
- Expected Behaviour: Links to 'Home', 'Note Editor' and 'Logout' all to appear on top navbar and links to 'Books', 'Chapters', 'Notepad' and 'Profile' to appear on side navbar. 
  All should redirect to respective pages except 'Notepad which should initiate notepad popup modal.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results.

6. (a) Note Editor - Logged out User
- Expected Behaviour: Page will not display for logged out user.
- Observed Results: This page does not display for logged out users.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

6. (b) Note Editor - Logged In User
- Expected Behaviour: Links to 'Home', 'Note Editor' and 'Logout' all to appear on top navbar and links to 'Books', 'Chapters', 'Notepad' and 'Profile' to appear on side navbar. 
  All should redirect to respective pages except 'Notepad which should initiate notepad popup modal.
- Observed Results: When loaded this page loaded without any issue and in a time that was satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

7. Login/Register - 

- Expected Behaviour: Links to 'Home', 'Login' and 'Register' all to appear on top navbar and links to 'Books' and 'Chapters' to appear on side navbar. 
  All should redirect to respective pages except Chapters which should redirect to 'Login' page and force login request.
- Observed Results: All links worked as intended and were satisfactory.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

**Test Case III:** Ensure all clickable elements/buttons and forms on page function correctly

1. (a) Book Page - Logged out User
- Expected Behaviour: When 'Book' is clicked it should flip to display content details of book and when 'Create new Book' is clicked it should direct user to 'Login' page.
- Observed Results: When 'Book' was clicked it flipped and when 'Create New Book' button was clicked it redirected user to login page.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

1. (b) Book Page - Logged In User
- Expected Behaviour: When 'Book' is clicked it should flip to display content details of book and when 'Create new Book' is clicked it should direct user to 'Add Book' page.
    If current user is also the creator of this item, the additional option of 'Edit' and 'Delete' should appear on flipside of the book item. The 'Edit' button should redirect user to 'Edit Book' page and
    the 'Delete' button should prompt user to confirm the want to delete the book via a popup button.
- Observed Results: When 'Book' was clicked it flipped and when 'Create New Book' button was clicked it redirected user to 'Add Book' page. 'Edit' book button redirected to 'Edit Book' page and the 'Delete' button returned 
    a popup to user to make sure they want to delete object. When 'Ok' was selected here the object was deleted and when 'Cancel' was selected the object was not deleted.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

2. Chapter Page - 
- Expected Behaviour: When 'Chapter' is clicked in collapsible list it should extend to display content details of chapter and when 'Add New Chapter' is clicked it should direct user to 'Add Chapter' page.
    If the current user is the creator of the object the additional option of 'Edit' and 'Delete' should appear on the displayed chapter item. The 'Edit' button should redirect user to 'Edit Chapter' page and
    the 'Delete' button should prompt user to confirm the want to delete the chapter via a popup button.
- Observed Results: When 'Chapter' was clicked it extended down to display content and when 'Add New Chapter' button was clicked it redirected user to 'Add Chapter' page. The 'Edit' chapter button redirected to 'Edit Chapter' page and the 'Delete' button returned 
    a popup to user to make sure they want to delete object. When 'Ok' was selected here the object was deleted and when 'Cancel' was selected the object was not deleted.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

3. Book Add Page/Chapter Add Page - 
- Expected Behaviour: When form is clicked it should request a minimum value input from user and all fields should be required, the save button should store data and redirect user back to 
    'Books' and 'Chapter' page (respective to what is being added). The add 'Chapter' form shoudl require user to select a corresponding 'Book' from dropdown before creating.
- Observed Results: Form requested a required and minimum value input to create new object, 'Chapter' page required user select a 'Book' from dropdown.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

4. Book Edit Page/Chapter Edit Page - 
- Expected Behaviour: When form is clicked it should display the existing values for all fields and if edited it should still request a minimum value input from user and all fields should be required, the save button should store data and redirect user back to 
    'Books' and 'Chapter' page (respective to what is being added). The add 'Chapter' form should require user to select a corresponding 'Book' from dropdown before creating.
- Observed Results: The form displayed the existing information and when edited it requested a required and minimum value input to create new object, the 'Chapter' page still required user select a 'Book' from dropdown.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

5. Profile - 
    There are no clickable buttons or forms on this page.

6. Note Editor - 
- Expected Behaviour: When form is clicked it should request a minimum value input from user and is a required field. The 'Save Note' button should store data. (Which can be seen by user when 'Notepad' button on sidebar is selected.)
- Observed Results: The form had a minimum and required value and when 'Save Note' was clicked the note was stored and visible in 'Notepad' popup modal. 
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

7. Login/Register - 

- Expected Behaviour: When form is clicked it should request a minimum value input from user and all fields should be required, the Login/Register button should submit data and redirect user back to 
    'Books'home page.
- Observed Results: The form requested a required and minimum value input to Login/Register. When login/registration was successful the page flashed image to user to confirm and when unsuccessful this was also reflected to user. 
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 


**Test Case IV:** Flash message display 

1. Book Page - 
- Expected Behaviour: Flash messages will display on top of page in bright banner when initiated.
- Observed Results: Feedback messages were flashed to user when they were required and had been correctly triggered.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

2. Chapter Page - 
- Expected Behaviour: Flash messages will display on top of page in bright banner when initiated.
- Observed Results: Feedback messages were flashed to user when they were required and had been correctly triggered.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 


3. Book Add Page/Chapter Add Page - 
- Expected Behaviour: Flash messages will display on top of page in bright banner when initiated.
- Observed Results: Feedback messages were flashed to user when they were required and had been correctly triggered.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 


4. Book Edit Page/Chapter Edit Page - 
- Expected Behaviour: Flash messages will display on top of page in bright banner when initiated.
- Observed Results: Feedback messages were flashed to user when they were required and had been correctly triggered.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 


5. Profile - 
- Expected Behaviour: Flash messages will display on top of page in bright banner when initiated.
- Observed Results: Feedback messages were flashed to user when they were required and had been correctly triggered.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 


6. Note Editor - 
- Expected Behaviour: Flash messages will display on top of page in bright banner when initiated.
- Observed Results: Feedback messages were flashed to user when they were required and had been correctly triggered.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 

7. Login/Register -
- Expected Behaviour: Flash messages will display on top of page in bright banner when initiated.
- Observed Results: Feedback messages were flashed to user when they were required and had been correctly triggered.
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 


**Test Case V:** Error 404 Page

Error 404 Page - 
- Expected Behaviour: If a user inputs an incorrect HTML the custom 'Error 404' HTML page should be displayed, including navigation back to other pages of website. 
- Observed Results: When an incorrect HTML was entered the user was redirected to custom Error 404 page, which had buttons on top to re-direct back to all other pages of website.  
- Test Summary: There was no outstanding differences between the expected behaviour of this test and the observed results. 


#### **Response tests -**

The site was tested across all media query sizes and at all possible breaking points to ensure that a consistent and responsive experience was ensured for the user on any device. 

The author also used AmIResponsive.com to ensure that this was confirmed through an outside, objective source.


#### **Browser tests -**

Though the sote was developed through Google Chrome, after it had been deployed online it was tested across all other major browsers to make sure that it was fully operational. These browsers included 
- Chrome
- Safari
- Firefox
- Opera


#### **User story tests:**

**Website user -**

1. As a user I want a visually appealing and smooth website experience
- Website is clean and crisp and doesn't distract user from writing planning work

2. As a user I want to be given visual feedback about my actions 
- Website contains many visual feedbacks to user on navbar, sidebar, buttons and clickable cursor elements over all pages

3. As a website user I want to be able to navigate the website easily and intuitively
- Website has a navbar and a sidebar with clear labels to giver user an intuitive navigating expereience.

4. As a user I want a consistent experience, that is the same every time I come back to the website and on any device
- This website was developed with all media screen size requirements and is responsive across all frequently used sizes

5. As a user I want to have my information protected by a password
- This website uses password hashing to verify that a user has entered correct password before allowing them access to any data on site

**Writer -**

6. As a writer I want to be able to create new books which I can read, edit and delete
- This website allows users to create, read, edit and delete objects which are displayed and behave like books to the user

7. As a writer I want to be able to create new chapters which I can read, edit and delete
- This website allows users to create, read, edit and delete objects which are displayed and behave like chapters to the user

8. As a writer I want to be able to get information about how many books and chapters I have created
- On the user profile page, feed back is given about how many books and chapters they have created which actively updates as more are created

9. As a writer I want to write quick notes which I can store and see later
- The notepad feature allows users to create quick notes and view them easily as a popup modal over any screen

10. As a writer I want an application that is visually clean and simple to user so I can focus on my writing
- The aesthetic of this website is clean and minimalist to allow user to focus on their writing

11. As a writer I want an app that I can use on desktop, tablet or mobile
- This application is deployed to the internet and can be accessed from and device on the internet

**Website Owner -** 

12. As the website owner I want the users to enjoy using my application
- This website offers users a novel way to create, read, edit and delete files in a way which can assist in the visual conceptualisation of planning a novel

13. As the website owner I want users to stay on my site for as long as possible
- This website has enough varied functionality that users could spend considerable time using this application

14. As the website owner I want the users to return to my website
- This website is simple, clean and functional and hopefully users would want top return

15. As the website owner I want users to be able to trust the security features that I have implemented
- Security features have been implemented to protect users, including user account password protection

### **BUG FIXES**

This project contained no major bug issues.

### **IMPLEMENTATION ISSUES**

There were no outstanding implementation issues with this project.

### **DEPLOYMENT**

**Git Hub Pages**

This project was developed in the Gitpod development environment. I initialised the project by creating a new repository for the project in GitHub and used this as a storing point to push the project to at various points through out the development process. Using the git add function I staged my code at many times and used the Git Commit command to save all changes. Finally, I used the Git Push command to send all the changes back to my repository on GitHub.

After initial deployment this site could no longer be access through GitHub pages without re-adding the 'env.py' file due to the sensitive information contained within. From this point onwards I accessed the site directly through Gitpod pages or from Heroku. 

**Deployment -**

In the early stages of development I deployed the site live to Heroku - this allowed me to check the site was working across multiple devices and also that I was no longer relying on the 'env.py' file to access this project.

**Creating clone of project -**

To create a clone of this project you can access it through the link on the Git Hub Repository, click the clipboard to copy the url, this can then be brought to the terminal when a new working directory can be set up and the clone saved. Once this is done you can type ???git clone??? and paste the url and press enter and a new clone will be created.

**Running Clone on local machine -**

If you want to run this clone on a local machine you would go to the 'Clone' section on GitHub and click the url link in the HTTPS section. When you download and unzip these files to your desktop you can then open them in your own IDE shell and save them as a new directory. 

Requirements needed to initialise project -

- pip3 install Flask
- pip3 install PyMongo
- pip3 install dnspython
- pip3 install flask-pymongo

All additional requirements can be found i the 'requirements.txt' file. 

### **CREDITS**

#### **General Elements -** 

- Code Institute (Course content & Slack Community)
- 2021 Complete Python Bootcamp From Zero to Hero in Python - Jose Portilla (Udemy)
- Python Crash Course: A Hands-On, Project-Based Introduction to Programming - Eric Matthes (Book)
- Python Tutorials for Beginners - Programming with Mosh (YouTube)

#### **Specific Elements -** 

**Adding Favicons to Website**
- Dani Krossing: (https://www.youtube.com/watch?v=kEf1xSwX5D8)

**Book Card flip JavaScript Functionality** 
- Tyler Potts: (https://www.youtube.com/watch?v=QGVXmoZWZuw)

**Buttons** 
- FDossena: (https://fdossena.com/?p=html5cool/buttons/i.frag)
- W3Schools: (https://www.w3schools.com/css/css3_buttons.asp)
- Materiaze Docs: (https://materializecss.com/buttons.html)

**CSS Animations/Transformation**
-Web Dev Simplified: (https://www.youtube.com/watch?v=YszONjKpgg4)

**CSS Flexbox** 
- Web Dev Simplified: (https://www.youtube.com/watch?v=fYq5PXgSsbE)
- Free Code Camp: (https://www.freecodecamp.org/news/learn-css-flexbox-in-5-minutes-b941f0affc34/)
- CSS Tricks: (https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

**Flask** 
-Flask Documentation: (https://flask.palletsprojects.com/en/2.0.x/patterns/viewdecorators/#login-required-decorator)

**Image Overlay Issues**
-Stack Overflow: (https://stackoverflow.com/questions/36927140/cant-click-the-button-because-of-the-overlay)

**Lighthouse Issues**
- Web.dev: (https://web.dev/image-aspect-ratio/?utm_source=lighthouse&utm_medium=devtools)

**Media Queries**
??? CSS Tricks: (https://css-tricks.com/snippets/css/media-queries-for-standard-devices/)
- W3Schools: (https://www.w3schools.com/css/css_rwd_mediaqueries.asp)
- Code Grepper: (https://www.codegrepper.com/code-examples/delphi/bootstrap+hide+image+on+mobile)

**MongoDB**
- MongoDB Documentation: (https://docs.mongodb.com/manual/reference/method/db.collection.distinct/?fbclid=IwAR1bzHDCQwV0t_x2VAYfLOJb9X0Sy_Lvg5_4vs0DE5gBGpXp4ututGT04PI)
- Tutorials Point: (https://www.tutorialspoint.com/mongodb/mongodb_sort_record.htm?fbclid=IwAR0UYkyl4zG_r4a7phaatoSmqkGZSZi41frbj3cbozDqOJp4APY1YKSc7WY)
- Joe Karlsson: (https://www.youtube.com/watch?v=leNCfU5SYR8)
- Frank Kane: (https://www.youtube.com/watch?v=UFVFIKduXpos)
- Hitesh Choudhary: (https://www.youtube.com/watch?v=HEXHy4JyDFc)

**README Editing**
- Adam Pritchard: (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Github Support: (https://github.community/t/link-to-a-section-in-another-readme-md-file/1130)
- Next Day Video: (https://www.youtube.com/watch?v=2dAK42B7qtw/)

**Side Navigation bar**
-CodingLab: (https://www.youtube.com/watch?v=wEfaoAa99XY)

#### **Other Elements -**

- Cooler.com - Colour scheme generator: (https://www.coolors.co/)

### **CONTENT**

All text content was written by author 

### **MEDIA**

All images were custom designed and created specifically for this project.

### **ACKNOWLEDGEMENTS**

- Code institute
- Mentor (Spencer Shelton)
- Slack Community
- Friends and Family (for testing)
    

