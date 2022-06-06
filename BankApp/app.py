
from json import load
from flask import Flask,render_template,request
import pickle
import tensorflow as tf
from tensorflow import keras
import os
import numpy as np
import warnings
warnings.filterwarnings("ignore")




def run_model(array):
	array = array[None,:]
	scaler = pickle.load(open('model/scaler','rb'))
	location = os.getcwd() + '\\model'
	model = tf.keras.models.load_model(location)
	scaled_feat = scaler.transform(array)
	prediction = model.predict(scaled_feat)
	return np.where(prediction >=0.5,1,0)

scaler = pickle.load(open('model/scaler','rb'))
location = os.getcwd() + '\\model'
model = tf.keras.models.load_model(location)

app = Flask(__name__)

@app.route("/")
def index():
		return render_template('index.html')

@app.route("/",methods=['POST'])
def prediction():
		age = int(request.form['age'])
		job = int(request.form['job'])
		marital = int(request.form['marital'])
		education = int(request.form['education'])
		housing = int(request.form['housing'])
		loan = int(request.form['loan'])
		default = int(request.form['default'])
		contact = int(request.form['contact'])
		dow = int(request.form['dow'])
		duration = int(request.form['duration'])
		campaign = int(request.form['campaign'])
		previous = int(request.form['previous'])
		poutcome = int(request.form['poutcome'])
		cpi = float(request.form['cpi'])
		e3m = float(request.form['e3m'])
		noe = int(request.form['noe'])
		pdays = int(request.form['pdays'])
		evr = float(request.form['evr'])
		cci = float(request.form['cci'])
		month = int(request.form['month'])

		prediction = run_model(np.asarray([age,job,marital,education,default,housing,loan,contact,month,dow,duration,campaign,pdays,previous,poutcome,evr,cpi,cci,e3m,noe]))
		
		if prediction == 1:
			outcome = "SUBSCRIBE TO A TERM DEPOSIT"
		else:
			outcome = "NOT SUBSCRIBE TO A TERM DEPOSIT"

		return render_template('output.html',age = age,job = job,marital = marital,education = education,housing = housing,loan = loan,
											campaign = campaign, previous = previous,poutcome = poutcome,cpi = cpi, e3m = e3m, noe = noe , outcome = outcome,
											deafult = default,contact = contact,dow = dow,duration = duration,pdays = pdays,evr= evr,cci = cci,month = month)



		

if __name__ == '__main__':
	app.run()