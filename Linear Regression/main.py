import re
from flask import Flask,request,jsonify,render_template
from flask_cors import CORS,cross_origin  ## This is for deployment
import pickle 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


app=Flask(__name__,template_folder='templates')
CORS(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/visualize')
def visual():
    return render_template('admission.html')


def scale(n1,n2,n3,n4,n5,n6,n7):
    value = pickle.load(open('F:\Ineuron\Machine Learning\Live Class\Linear Regression\Scalar_Admission.pickle','rb'))
    return value.transform([[n1,n2,n3,n4,n5,n6,n7]])

def prediction(value):
    model = pickle.load(open('admission_model.pickle','rb'))
    return model.predict(value)




@app.route('/calculate' , methods = ['POST'])
def calci():
    if(request.method == "POST"):
         gre=int(request.form['gre'])
         tofl=int(request.form['tofl'])
         university=int(request.form['university'])
         sop = int(request.form['sop'])
         lor = int(request.form['lor'])
         cgpa = int(request.form['cgpa'])
         research = int(request.form['research'])
        
         value = scale(gre , tofl , university , sop , lor , cgpa , research)

         predict = prediction(value)[0]
         calculation = f"Based On Your Academic Scores the chance of getting this university : {predict*100} %"
    return render_template('index.html', chance = calculation)

if __name__ == '__main__':
    app.run(debug=True, port =8000)


