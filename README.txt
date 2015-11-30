By Simon Reiffen

This project contains GET, GET ALL, and POST methods for the fizzbuzz API. Note, that there are two ways of calling these methods.
I made two separate ways of calling these methods, because I have written code for various people who have different definitions of what an
API Endpoint was. (Just as some people use Big O of X to refer to the exact runtime of an algorithm, while others use Big O of X to refer to
worst case runtime of an algorithm, I have met several people with different definitions of API Endpoints). I was uncertain if you wanted multiple
methods, each corresponding to GET, GET ALL, and POST, or if you wanted one method, that, depending on the input and request method, would handle
each of those cases. So, I decided to make both. 


I used views to call different methods. For example, if you wanted to call GET ALL, type in


"localhost:8000/fizzbuzz/GET/"

If you wanted to get a specific fizzbuzz, type in

"localhost:8000/fizzbuzz/GET/ID/"

If you wanted to post a fizzbuzz, type

"localhost:8000/fizzbuzz/POST/message"

(NOTE: to allow most browsers to use the POST method as a view that can be accessed by URL, I needed to allow it to accept
both GET and POST methods (since most browsers make requests using GET), but, if you were planning on implementing this code
so that it would only be called in instances where the method could be set to POST (such as, when calling it using <form action>),
then you could get ride of the line allowing for the GET method)

In addition to these methods, I also made a function called "SWISS" (as in, Swiss Army Knife),  that allows for each of these three
methods to be called, depending on the input provided. Based on the amount of input provided, SWISS can tell if a GET request wants 
one specific fizzbuzz, or all of them (if there is no extra input provided beyond the GET request, SWISS gets all the fizzbuzzs).

So, to use SWISS to get a specific fizzbuzz

"localhost:8000/fizzbuzz/SWISS/ID/"

and to get all fizzbuzzs

"localhost:8000/fizzbuzz/SWISS/"
However, since most browsers default to a GET Request, it may be hard to test the POST feature. To deal with that problem, I created a
"demo" view, that takes user input from the URL, and then uses <from action> calls to call SWISS with the appropriate method(GET or POST).
To use this method, type in 


"localhost:8000/fizzbuzz/demo/STRING/"

And then press the button that corresponds to the function you wish to call. (GET, POST, and GET ALL)

The String that you input into demo will be passed to SWISS. So, if you wish to call GET through demo, make sure that String is an int.
If you intend on calling POST or GET ALL, it doesn't matter what String is.

Note: I didn't include any test cases in this package, as I figured you would have your own series of tests you would want to run 
on this. However, if you would like me to write up some test cases, just email me, and I'll send you some right away.

Much of the models, serializers, and views are based off of the tutorial at http://www.django-rest-framework.org/.

To Set Up, simple run 

python manage.py makemigrations models.py
then
python manage.py migrate
finally,
python manage.py runserver


If you have any questions or concerns about this project, feel free to email me at Simon.Reiffen@gmail.com