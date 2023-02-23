from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


# Q1. Explain GET and POST methods.
'''
GET and POST are HTTP methods used in web applications to retrieve or send data to a server.

GET method:
The GET method is used to retrieve data from a server.
It sends a request to the server asking for a specific resource (a web page, an image, a file, etc.).
The parameters of the request (if any) are encoded in the URL of the request.
GET requests are usually cacheable, meaning that the response can be stored in the browser's cache to improve performance.

GET /api/users?id=123 HTTP/1.1
Host: example.com


POST method:
The POST method is used to submit data to a server.
It sends a request to the server with data in the body of the request (instead of the URL).
POST requests are not cacheable because they usually change the state of the server.
The data in a POST request is usually sent in a format such as JSON or XML.


POST /api/users HTTP/1.1
Host: example.com
Content-Type: application/json

{"name": "Chandan", "email": "Chandan@example.com"}
In summary, GET and POST methods are used in web applications to retrieve or send data to a server, with GET used to retrieve data and POST used to submit data.

'''
# Q3. Why is redirect() used in Flask?
'''
This function returns a response object with a status code of 302 (redirect) and a Location header set to the target URL. When the client receives this response, it will automatically issue a new request to the target URL.

Here are some common use cases for the redirect() function in Flask:

Redirecting after a form submission: After a user submits a form, you may want to redirect them to a "success" page or back to the original page with a success message. You can use the redirect() function to send them to the desired page.

Implementing authentication: If a user tries to access a protected page without being logged in, you can redirect them to the login page using the redirect() function. After the user logs in successfully, you can redirect them back to the original page they were trying to access.

Redirecting from an old URL to a new URL: If you've changed the structure of your website or moved a page to a new URL, you can use the redirect() function to send users who visit the old URL to the new one.


from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Redirect to the 'about' page
    return redirect(url_for('about'))

@app.route('/about')
def about():
    return "This is the about page"

if __name__ == '__main__':
    app.run()
'''
# Q4. What are templates in Flask? Why is the render_template() function used?
'''
In Flask, templates are used to separate the presentation logic from the business logic of the application. Templates are essentially HTML files with placeholders for dynamic content. They allow developers to generate HTML pages dynamically by inserting data into the placeholders based on the user's request.

Flask uses a template engine called Jinja2, which allows for a wide range of template customization options. With Jinja2, developers can create reusable components and macros, inherit templates from other templates, and use control structures like loops and conditionals to dynamically generate HTML.

To render a template in Flask, the render_template() function is used. This function takes the name of the template as its first argument, followed by any additional arguments to be passed to the template. It returns a string containing the rendered HTML.

Here's an example of how to use the render_template() function in Flask:



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Render the 'home.html' template
    return render_template('home.html', title='Home', message='Welcome to my website!')

if __name__ == '__main__':
    app.run()


In this example, the home() function renders the home.html template using the render_template() function. 
The title and message variables are passed to the template as keyword arguments and can be accessed in the template using Jinja2 syntax like {{ title }} and {{ message }}.

Overall, templates in Flask provide a flexible and modular way to generate dynamic HTML pages, while the render_template() function allows developers to easily render these templates with the necessary data.

'''

# Create a simple API. Use Postman to test it. Attach the screenshot of the output in the Jupyter Notebook.
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)

URL: http://localhost:5000/

'''


if __name__=="__main__":
    app.run(host="0.0.0.0")
