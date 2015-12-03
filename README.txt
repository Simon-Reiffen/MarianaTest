By Simon Reiffen

This project contains GET, GET ALL, and POST methods for the fizzbuzz API. All three of these methods are contained in the same viewSet,
called "fizzbuzzViewset". To search for a specific fizzbuzz, call

request = Request('http://localhost:8000/fizzbuzz/ID')



To find all fizzbuzzs, call

request = Request('http://localhost:8000/fizzbuzz/')


To create a new fizzbuzz call

request = Request('http://127.0.0.1:8000/fizzbuzz/', data=values, headers=headers)

Where values is a tuple {"message" :"some string"}, and headers is 

headers = {
	  'Content-Type': 'application/json'
	}

To set up, first run

$python runserver.py makemigrations fizzbuzz

Then

$python runserver.py migrate

If you have any questions or concerns about this project, feel free to email me at Simon.Reiffen@gmail.com