#------------------------------------------------------------------------------#
# Imports
#------------------------------------------------------------------------------#

from flask import * # do not use '*'; actually input the dependencies
from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler

#------------------------------------------------------------------------------#
# App Config
#------------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#------------------------------------------------------------------------------#
# Controllers
#------------------------------------------------------------------------------#

@app.route("/")
def index():
    return render_template("index.html")
'''
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")
'''

# Error Handlers

@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('500.html'), 500

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#------------------------------------------------------------------------------#
# Launch
#------------------------------------------------------------------------------#

# default  port
if __name__ == '__main__':
    app.run()

# or specify port
'''
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
'''
