Flask Boilerplate
=================

Initial idea for a boilerplate

Basic Requirements
-----------------
* Flask
* Flask-SQlalchemy
* Flask-WTF
* MySQL-python==1.2.4
* Bootstrap

Create MakeFile
---------------
* Python
* virtualenv
* heroku tool belt

[Reference](https://github.com/mjhea0/flask-boilerplate)

Project Structure
--------

    ├── Procfile
    ├── Procfile.dev
    ├── app.py
    ├── config.py
    ├── error.log
    ├── forms.py
    ├── models.py
    ├── requirements.txt
    ├── static
    │   ├── css
    │   │   ├── boostrap-responsive.css
    │   │   └── bootstrap.css
    │   ├── img
    │   │   ├── glyphicons-halflings-white.png
    │   │   └── glyphicons-halflings.png
    │   └── js
    │       ├── libs
    │       │   ├── bootstrap.min.js
    │       │   ├── jquery.min.js
    │       │   └── modernizr-2.0.6.min.js
    │       ├── plugins.js
    │       └── script.js
    └── templates
        ├── 404.html
        ├── 500.html
        ├── index.html
        ├── login.html
        ├── register.html
        └── template.html

Quick Start
----------

1. Clone the repo

        $ git clone git@github.com:DreamsofPy/flask-boilerplate.git
        $ cd flask-boilerplate

2. Initialize and activate a virtualenv:

        $ virtualenv --no-site-packages env
        $ source env/bin/activate

4. Install the dependencies:

        $ pip install -r requirements.txt

5. Run the development server:

        $ python app.py

6. Navigate to [http://localhost:5000](http://localhost:5000)

Deploying to Heroku
------

1. Signup for [Heroku](https://api.heroku.com/signup)
2. Login to Heroku and download the [Heroku Toolbelt](https://toolbelt.heroku.com/)
3. Once installed, open your command-line and run the following command - `heroku login`. Then follow the prompts:

        Enter your Heroku credentials.
        Email: your@email.org
        Password (typing will be hidden):
        Could not find an existing public key.
        Would you like to generate one? [Yn]
        Generating new SSH public key.
        Uploading ssh public key /Users/yourusername/.ssh/id_rsa.pub

1. Activate your virtualenv
2. Heroku recognizes the dependencies needed through a *requirements.txt* file. Create one using the following command: `pip freeze > requirements.txt`. Now, this will only create the dependencies from the libraries you installed using pip. If you used easy_install, you will need to add them directly to the file.
3. Create a Procfile. Open up a text editor and save the following text in it:

        web: python run.py

   Then save the file in your applications root or main directory as *Procfile* (no extension). The word "web" indicates to Heroku that the application will be attached to the HTTP routing stack once deployed.
4. Update your *run.py* file. On your local machine, the application runs on port 5000 by default. On Heroku, the application **must** run on a random port number specified by Heroku. We will identify this port number by reading the environment variable 'PORT' and passing it to `app.run`:

        # run.py


        import os

        from flasktaskr import app

        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=False)

1. Create a local Git repository:

        $ git init
        $ git add .
        $ git commit -m "initial files"

1. Create your app on Heroku:

        $ heroku create <name_it_if_you_want>

1. Deploy your code to Heroku:

        $ git push heroku master
        $ heroku ps:scale web=1

1. Check to make sure your app is running:

        $ heroku ps

1. View the app in your browser:

        $ heroku open

1. You app should look similar to this - [http://www.flaskboilerplate.com/](http://www.flaskboilerplate.com/)

1. Having problems? Look at the Heroku error log:

        $ heroku logs

Learn More
---------

1. [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/python)
1. [Flask Documentation](http://flask.pocoo.org/docs/)
2. [Flask Extensions](http://flask.pocoo.org/extensions/)
