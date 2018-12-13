from app import db


class User(db.Model):
    username= db.Column(db.String,primary_key=True)
    email= db.Column(db.String(40),primary_key=True)
    password= db.Column(db.String(),index=True)
    book=db.relationship('Books',backref='user',lazy='dynamic')

    def __repr__(self):

        return 'user %r' % (self.username,self.email,self.password)

class Books(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    bookname= db.Column(db.String(30))
    bookgenre= db.Column(db.String(30),index=True)
    author=db.Column(db.String(40),index=True)
    user_name = db.Column(db.String,db.ForeignKey('user.username'))


    def __repr__(self):
        return 'books %r' % (self.bookname,self.bookgenre,self.author)

    

