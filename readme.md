url patterns

login page is the navbar
table of students  on homepage www.badbehavior.com

leads to list of students who recently got in trouble www.badbehavior.com/home
might want to be able to save using json web token

on the dashboard you should be able to click on the student edit button or add new student button
to edit button www.badbehavior.com/studentform/studentid 
to add student button www.badbehavior.com/student_form/studentid where if no id the thing is blank

add offense button leads to www.badbehavior.com/offense_form/studentid

clicking on student name to see profile of students.
    will show the offenses and an add action button 
    www.badbehavior.com/student_profile/studentid

add action button will lead to action form www.badbehavior.com/action_form/id



Problem: Connecting Django Forms to Django Rest Framework API
How forms and api are two separate things so I had to add the word external
1. Form was redirecting to the browsable api and not to login
    *Code not running
    *form action attribute value changed to register form url
2. Where do I put the post request in the register_form class?
    *put form request if form is valid
3. Post request throwing error 'QueryDict' object is not callable
    *Changed data attribute in the post request to a json attribute
    Django REST Framework by default accepts application/json as a content-type, while data parameter sends the body as application/x-www-form-urlencoded
4. Import requests module







