from flask import Flask,render_template,request

#In flask forms is directly not import.so,first we can install the flask_wtf,
#after than we can import the forms

from flask_wtf import Form

#Compare to django flask field are different.after installed the flask_wtf,it will
#automatically give the wtforms.First import the fields we can use 

from wtforms import StringField,PasswordField,SubmitField,HiddenField

#DataRequired is used for,users don't give the information,it will show the error

from wtforms.validators import DataRequired


FAI=Flask(__name__)

#In flask automatically post method not activate.so,first we can import the request
#after that we can use the request

@FAI.route('/htmlform',methods=['GET','POST'])

def htmlform():
    if request.method=='POST':
        fn=request.form
        # display all the data we give (return fn)
        #return fn
        # display only any one.we give return fn['give id in html form']
        return fn['un']

    return render_template('htmlform.html')

#In flask form represent in Form class
class NameForm(Form):
    Sname=StringField(validators=[DataRequired()])
    Password=PasswordField(validators=[DataRequired()])
    Submit=SubmitField()

@FAI.route('/webforms',methods=['GET','POST'])

def webforms():
    ENDO=NameForm()
    if request.method=='POST':
        #In django dictionary key word name is request.method.but,in flask dictionary key 
        #word name is request.form

        EDNO=NameForm(request.form)

        #In flask,for valid the fdata we can use validate method
        if EDNO.validate():
            #we can get all the data so,we can write store the data.data
            return EDNO.data
        
    return render_template('webforms.html',ENDO=ENDO)

if __name__=='__main__':
    FAI.run(debug=True)