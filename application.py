from flask import Flask,render_template,request

FAI=Flask(__name__)

#In flask automatically post method not activate.so,first we can import the request
@FAI.route('/htmlform',methods=['GET','POST'])

def htmlform():
    if request.method=='POST':
        un=request.form
        return un
    return render_template('htmlform.html')

if __name__=='__main__':
    FAI.run(debug=True)