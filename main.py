from flask import Flask, render_template
from forms import RegistrationForm, LoginForm

### Sentry Error Reporting ###
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://7b59c20e80184d648a756f0444332f25@sentry.io/1334947",
    integrations=[FlaskIntegration()]
)

### Main Application Declaration ###
app = Flask(__name__)

app.config['SECRET_KEY'] = '4484756E83B1142B34B6AFDE84586'

### Application Routes ###
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='The Ultimate Nightlife Experience, Providing Direct Connection to the DJ, Without Barriers.')
    
@app.route("/Community")
def community():
    return render_template('community.html', title='Community')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Create An Account')

app.route("/login")
def register():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)

### Server Reload ###
if __name__ == '__main__':
    app.run(debug=True)