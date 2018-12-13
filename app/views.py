from flask import render_template,request,flash,redirect,session,url_for

from app import app,db,admin
from flask_admin.contrib.sqla import ModelView
from app.models import User, Books
from .forms import RegistrationForm
from .forms import LoginForm
from .forms import AddBookForm
from .forms import SearchForm
from .forms import EditForm

from datetime import timedelta

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Books, db.session))

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=20)

    
@app.route('/', methods=['GET', 'POST'])
def registration():
        form=RegistrationForm(request.form)
        
        if request.method=="POST":
            username=request.form['username']
            email=request.form['email']
            password=request.form['password']
            confirm=request.form['confirm']
            
              
            if((db.session.query(User.username).filter_by(username=username).first()) or (db.session.query(User.email).filter_by(email=email).first()) or (password!=confirm)):           
                if (db.session.query(User.username).filter_by(username=username).first()):
                    flash("Error:Username is already taken! Please choose another")
                    return render_template('register.html', form=form)
            
                if (db.session.query(User.email).filter_by(email=email).first()):
                    flash("Error:Email is already taken!")
                    return render_template('register.html', title='Register', form=form)
            
                if(password!=confirm):
                    flash("Error:Passwords must match!")
                    return render_template('register.html', title='Register', form=form)
                
                if(username=='' or password=='' or email=='' or confirm==''):
                    flash("Error:You must fill all the form!")
                    return render_template('register.html', title='Register', form=form)
                    
            
            else:
                x=User()
                x.username=username
                x.email=email
                x.password=password
                db.session.add(x)
                db.session.commit()
                flash("Thanks for registering! You can now login.")

                              
        return render_template("register.html",title='Register',form=form)
                
        
@app.route('/login', methods=['GET', 'POST'])
def login():
        form=LoginForm()
        
        if request.method=="POST" :
            x=db.session.query(User.username,User.password).filter_by(username=form.loginusername.data).first()
            if (x):
                if (x.password==form.loginpassword.data):
                    session['user'] = form.loginusername.data
              
                    return redirect(url_for('addbook', title='Read a Book',username=x.username))

                    
                else:
                    flash("Error:Invalid Username or Password")
                    
        return render_template('login.html', title='Login',form=form)
    
        



@app.route('/addbook/<username>', methods=['GET', 'POST'])
def addbook(username):
        form=AddBookForm()
        
        if request.method=='POST':
            x=Books()
            x.bookname=form.bookname.data
            x.bookgenre=form.bookgenre.data
            x.author=form.author.data
            x.user_name=username
            db.session.add(x)
            db.session.commit()
            flash("Book Added Succesfully")

 
        return render_template("addbook.html", title='Read a Book',form=form,username=username)


@app.route('/editpassword/<username>', methods=['GET', 'POST'])
def editpassword(username):
        form=EditForm()
        
        if request.method=='POST':
            x=db.session.query(User.username,User.password).filter_by(username=username).first()
            if(x):
                if((x.password==form.current.data) and (form.new.data==form.renew.data)):
                    
                    u=User.query.filter_by(username=username).first()
                    u.password=form.new.data
                    db.session.commit()
                    flash("Password Changed")
                    return render_template("edit.html", title='Edit Password',form=form,username=username)
                else:
                    flash("Error: Passwords not match")
            else:
                flash("Error:Not Found!")
        return render_template("edit.html", title='Edit Password',form=form,username=username)


@app.route('/allthebooks/<username>')
def allthebooks(username):
    allbooks=Books.query.filter_by(user_name=username).all()

    return render_template('allthebooks.html',title='All books',theBook=allbooks,username=username)

@app.route('/searchbook/<username>',methods=['GET', 'POST'])
def searchbook(username):
    i=0
    j=0
    form=SearchForm()
    rows=db.session.query(Books.id,Books.bookname,Books.bookgenre,Books.author).all()
    foundbooks=[]
    foundid=[]
    if request.method == 'POST':
        for row in rows:
            searchstr=str(row[1])
            if form.search.data in searchstr:
                j=j+1
                foundbooks.append(row[1])
                foundid.append(row[0])
    return render_template('searchbook.html', title='Search Books',form=form,i=i,j=j,foundbooks=foundbooks,username=username)


@app.route('/logout')
def logout():
    flash("You have logged out")
    session.pop('user', None)
    return redirect(url_for('login'))
