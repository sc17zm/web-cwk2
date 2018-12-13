from flask_wtf import Form
from wtforms import TextField,validators,PasswordField,StringField,SelectField

from wtforms.validators import DataRequired

from .models import User, Books
class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20),validators.DataRequired()])
    email = TextField('Email Address', [validators.Length(min=6, max=50),validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.Required()])
    
    confirm = PasswordField('Repeat Password')
 
class LoginForm(Form):
    loginusername = TextField('Username', [validators.DataRequired()])
    loginpassword = PasswordField('Password', [validators.DataRequired()])

class AddBookForm(Form):
    bookname = TextField('Username', [validators.DataRequired()])
    bookgenre =SelectField(u'Book Genre',choices = [('Action','Action'),('Adventure','Adventure')
    ,('Drama','Drama'),('Fantasy','Fantasy'),('Horror','Horror'),('Mystery','Mystery'),('Mythology','Mythology')
    ,('Romance','Romance'),('Science fiction','Science fiction'),('Other','Other'),],validators=[DataRequired()])
    author = TextField('Author', validators=[DataRequired()])
    
class SearchForm(Form):
    search=StringField('')
    
class EditForm(Form):
    current = PasswordField('Password', [validators.DataRequired()])
    new= PasswordField('Password', [validators.DataRequired()])
    renew = PasswordField('Password', [validators.DataRequired()])