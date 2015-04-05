<!-- title: REST API Guidance -->

REST APIs are a very common topic nowadays; they are part of almost every web
application. A simple, consistent and pragmatic interface is mandatory and it
will be much easier for others to use your API. Even if these practices may look
common to you, I often see projects that don't really respect them. That's why I
compiled this list. Here are some best practices to keep in mind while designing
a RESTful API.

### Version your API

API versions are mandatory. This way, you will be futureproof as the API changes
through time. One way to do this is to pass the API version in the URL (_e.g._
`/api/v1/...`). Another neat trick is to use the `Accept` HTTP header to pass
the verison
desired. [Github does that](https://developer.github.com/v3/media/#request-specific-version).
Using versions will allow you to change the API structure without breaking
compatibility with older clients.

### Use nouns, not verbs

I see a lot of projects using verbs instead of nouns in their resource
names. Here are some bad examples:

- `/getProducts`
- `/listOrders`
- `/retreiveClientByOrder?orderId=1`

For a clean and conscice structure you should always use nouns. Moreover, a
good use of HTTP methods will allow you to remove actions from your resources
names. Here is a much cleaner example :

- `GET /products`: will return the list of all products
- `POST /products`: will add a product to the collection
- `GET /products/4`: will retreive product #4
- `PATCH/PUT /products/4`: will update product #4

### Use the plural form

It isn't a really good idea to mix singular and plural forms in a single
resource naming; it can quickly become confusing and non-consistent. Use
`/artists` instead of `/artist`, even for the show/delete/update actions

### GET and HEAD calls should always be safe

[RFC2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html) cleary states
that HEAD and GET methods should always be safe to call (in other words, the
state should not be altered). Here is a bad example:

    GET /deleteProduct?id=1

Imagine a search engine indexing that page?!?

### Use nested resources

If you want to get a sub collection (collection of another one), use nested
routing for a cleaner design. For instance, if you want to get a list of all
albums of a particular artist, you would want to use :

    GET /artists/8/albums

### Paging

Returning a very large resultset over HTTP is not a very good idea either. You
will eventually run into performance issues as serializing a large JSON may
quickly become expensive. An option to get around that would be to paginate your
results. Facebook, Twitter, Github, etc. do that. It's much more efficient to
make more calls that takes little time to complete, than a big one that is very
slow to execute.

Also, if you are using pagination, one good way to indicate the next and
previous pages links is through the Link HTTP
header. [Github does that too](https://developer.github.com/guides/traversing-with-pagination/).

### Use proper HTTP status codes

Always use proper HTTP status codes when returning content (for both successful
and error requests). Here a quick list of non common codes that you may want to
use in your application.

#### Success codes

- `201 Created` should be used when creating content (INSERT),
- `202 Accepted` should be used when a request is queued for background
  processing (async tasks),
- `204 No Content` should be used when the request was properly executed but no
  content was returned (a good example would be when you delete something).

#### Client error codes

- `400 Bad Request` should be used when there was an error while processing the
  request payload (malformed JSON, for instance).
- `401 Unauthorized` should be used when a request is not authenticiated (wrong
  access token, or username or password).
- `403 Forbidden` should be used when the request is successfully authenticiated
  (see 401), but the action was forbidden.
- `406 Not Acceptable` should be used when the requested format is not available
  (for instance, when requesting an XML resource from a JSON only server).
- `410 Gone` Should be returned when the requested resource is permenantely
  deleted and will never be available again.
- `422 Unprocesable entity` Could be used when there was a validation error
  while creating an object.

A more complete list of status codes can be found in
[RFC2616](https://www.ietf.org/rfc/rfc2616.txt).

### Always return a consistent error payload

When an exception is raised, you should always return a consistent payload
describing the error. This way it will be easier for others to parse the error
message (the structure will always be the same, whatever the error is).

Here's one I often use in my web applications. It is clear, simple and
self-descriptive.

    HTTP/1.1 401 Unauthorized
    {
        "status": "Unauthorized",
        "message": "No access token provided.",
        "request_id": "594600f4-7eec-47ca-8012-02e7b89859ce"
    }

----

### RESTful APIs with Flask

1. Use virtualenv for Managing Packages
2. Installing packages
    a. [Flask](http://flask.pocoo.org/)
    b. [Flask-Restless](https://flask-restless.readthedocs.org/en/latest/) (for building the RESTful API)
    c. [Flask-SQLAlchemy](http://pythonhosted.org/Flask-SQLAlchemy/) (for connecting to our database)
3. Running Flask's _Hello World_. Create a new Python file called `app.py` and
   copy/paste the _Hello world_ code from
   [Flask’s homepage](http://flask.pocoo.org/):

        from flask import Flask
        app = Flask(__name__)

        @app.route("/")
        def hello():
            return "Hello World!"

        if __name__ == "__main__":
            app.run()

4. Connect to your database. Use SQLAlchemy to create and connect to our SQLite
   database. Replace the previous route code with a few lines of configuration
   for your database code to make your Python script look like this:

        from flask import Flask
        from flask.ext.sqlalchemy import SQLAlchemy

        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
        db = SQLAlchemy(app)

        class Person(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            first_name = db.Column(db.Text)
            last_name = db.Column(db.Text)

        db.create_all()

        if __name__ == "__main__":
            app.run()

5. Creating the RESTful API. We'll use Flask-Restless to build the RESTful
   API. You only need to add three lines of code. Import the APIManager, then
   create the API using the APIManager as shown in the code below:

        from flask import Flask
        from flask.ext.restless import APIManager
        from flask.ext.sqlalchemy import SQLAlchemy

        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
        db = SQLAlchemy(app)

        class Person(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            first_name = db.Column(db.Text)
            last_name = db.Column(db.Text)

        db.create_all()

        api_manager = APIManager(app, flask_sqlalchemy_db=db)
        api_manager.create_api(Person, methods=['GET', 'POST', 'DELETE', 'PUT'])

        if __name__ == "__main__":
            app.run()

Open the browser to execute a GET request and see the results.  You can also
select a specific *Person* by id by appending the id to the url. Using these
APIs, you can now GET, POST, DELETE, and PUT data and you’ve laid the groundwork
for your application.
