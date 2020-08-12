import numpy as np 
import pandas as pd 
from flask_cors import cross_origin 
from flask import Flask, request, render_template 
import pickle
import joblib

app = Flask(__name__,template_folder='templates')

@cross_origin()
@app.route('/')
def home():
	return render_template('indexx.html')
@cross_origin()
@app.route('/predict',methods=['POST'])
def predict():
	Age = int(request.form['Age'])
	WBC = float(request.form['WBC (Leukocyte Count)'])
	Neutrophils = float(request.form['Neutrophils'])
	Lymphocytes = float(request.form['Lymphocytes'])
	Monocytes = float(request.form['Monocytes'])
	Eosinophils = float(request.form['Eosinophils'])
	Basophils = float(request.form['Basophils'])
	Platelets = float(request.form['Platelets'])
	ALT = float(request.form['ALT (Alanine Amino Transferase)'])
	AST= float(request.form['AST (Aspartate Aminotransferase)'])
	Proteina_C = float(request.form['Proteina C reativa mg/dL'])
	LDH = float(request.form['LDH (Lactate Dehydrogenase)'])
	GGT = float(request.form['GGT (Gamma-Glutamyl Transferase)'])

	mymodel = open('atlest_now.pkl', 'rb')

	model = pickle.load(mymodel)
	data = np.array([Age, WBC , Neutrophils , Lymphocytes, Monocytes, Eosinophils, Basophils, Platelets,ALT ,AST ,Proteina_C,LDH ,GGT])
	data = data.reshape(1,-1)
	# loading the model file from the storage
    # predictions using the loaded model file
	prediction = model.predict(data)
	if prediction == [1]:
		prediction = "corona"
	else:
		prediction = "Normal"
    # showing the prediction results in a UI
	if prediction =="corona":
		return render_template('corona.html', prediction=prediction)
	else:
		return render_template('normal.html',prediction=prediction)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5021, debug=True)
	#app.run(debug=True)