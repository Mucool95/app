from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///IOT.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

A=['a@gmail.com','b@yahoo.com','c@rediff.com','mukul@cekaty.in','abcd@gmail.com']
B=['a','b','c','d','e']
class Iot(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),nullable=False)
    ename=db.Column(db.String(50),nullable=False)

def __repr__(self)-> str:
    return f"{self.sno}-{self.email}"

'''@app.route('/')
def live():
    for i in range(0,4):
        mail=A[i]
        name=B[i]
        iot=Iot(email=mail, ename=name)
        db.session.add(iot)
        db.session.commit()
    alldata=Iot.query.all()
    return render_template('home.html',alldata=alldata)'''


@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        mail=request.form['mail']
        name=request.form['name']
        iot=Iot(email=mail, ename=name)
        db.session.add(iot)
        db.session.commit()
    alldata=Iot.query.all()
    return render_template('home.html',alldata=alldata)

@app.route('/delete/<int:sno>')
def delete(sno):
    dat=Iot.query.filter_by(sno=sno).first()
    db.session.delete(dat)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        mail=request.form['mail']
        name=request.form['name']
        dat=Iot.query.filter_by(sno=sno).first()
        dat.email=mail
        dat.ename=name
        db.session.add(dat)
        db.session.commit()
        return redirect('/')
    alldata=Iot.query.filter_by(sno=sno).first()
    return render_template('update.html',alldata=alldata)
if __name__=="__main__":
    app.run(debug=True,port =8080)