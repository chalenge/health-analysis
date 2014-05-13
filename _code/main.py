'''
Created on April 26, 2014
@author: ramit

Decision Tree Classifier for Patient Disposition Prediction
'''

import csv
from sklearn import tree
import cPickle
from sklearn.metrics import classification_report
from sklearn import cross_validation

'''
Step1: Pre-processing
The preprocess function extracts the required fields from the .csv input file. 
Input: a file containing the records
Output: a list containing the records
'''
def preprocess(inputfile):
	inputlist = []
	with open(inputfile, 'rU') as fileData:
		fileReader = csv.reader(fileData, delimiter=',', quotechar='|')
		for line in fileReader:
			line[3] = int(line[3])
			#line[6] = int(line[6])
			line[9] = int(line[9])
			line[11] = int(line[11])
			inputlist.append(line)
	fileData.close()
	return inputlist

'''
Step2: Prepare Data
The prepare() function processes the inputlist from preprocess() function to separate the class labels and vectorizes the nominal features. 
'''			

def prepare_data(inputlist):
			
	dataSet =[]
	labels = []

	for record in inputlist:
		labels.append(labelTypes.index(record[2]))
		record.pop(2)
		illnessC = illnessCode.index(record[0])
		illness = illnessCategory.index(record[1])
		age = record[2]
		gender = sex.index(record[3])
		ethnicity = race.index(record[4])
		area = county.index(record[6])
		zipcode = zip.index(record[5]) 
		insure = insurer.index(record[7])
		insurance = record[8]
		day = date.index(record[9][:-3])
		year = record[10]
		dataSet.append([illnessC,zipcode,insurance])
		#dataSet.append([illness,age,gender,ethnicity,zipcode,insure,insurance,day,year])
	return dataSet, labels

'''
Step3: Train Model
Processed Data is passed to sklearns Decision Tree Classifier to train the model.
'''

def trainClassifier():
	trainingList = []
	trainingSet = []
	trainingList = preprocess(trainingfile)
	trainingSet = prepare_data(trainingList)
	labels = trainingSet[1]
	dataset = trainingSet[0]
	'''
	Fitting the training data into the Decision Tree
	'''

	DispClf = tree.DecisionTreeClassifier()
	DispClf.fit(dataset, labels)

	#Cross Validation of the results using 10% of the trainingSet as the testSet


	X_train, X_test, y_train, y_test = cross_validation.train_test_split(
	dataset, labels, test_size=0.1, random_state=0)
	print "Cross Validation Score"
	print DispClf.score(X_test, y_test)
	#print X_train, X_test, y_train, y_test
	
 	# Save the classifier
	with open('Disp_classifier.pkl', 'wb') as fid:
		cPickle.dump(DispClf, fid)

'''
Step4: Test Model
Pass the test dataset to the classifier to predict the Dispositions.
'''

def testClassifier():
	
	#Load the saved classifier
	with open('Disp_classifier.pkl', 'rb') as fid:
		DispClf = cPickle.load(fid)
	
	testingList = []
	testingSet = []
	testingList = preprocess(testingfile)
	testingSet = prepare_data(testingList)
	testData = testingSet[0]
	testLabels = testingSet[1]
	predictions = DispClf.predict_proba(testData)
	labelPredictions = DispClf.predict(testData)
	accuracy = DispClf.score(testData, testLabels)
	print "Mean Accuracy is: ", accuracy
	print "Classification Report: \n\n", classification_report(testLabels, labelPredictions)
	return predictions

'''
Formatting the output. Check output file: _data/results.txt
'''

def outputResults(predictions,testrows):
	dispositions = [0,1,2]
    	for row in testrows:
        	tData.append(row)
    	print "Test Prediction Results"
    	print "The top row is the actual record: ICD_9_CODE, DISEASE CATEGORY, DISPO, AGE, SEX, RACE, ZIP, COUNTY, INSURER, INSURANCE, DATE, YEAR."
    	print "The percentage-wise breakdown of the predicted disposition is below each of the actual records."
    	k=0
    	for each in predictions:
        	print "Record #"+str(k)+" : "+str(tData[k])
        	j=0
        	for i in each:
            		if(i!=0):
                		print [str(labelTypes[(dispositions[j])])+": "+str(round(i,3)*100)+"%"]
            		j+=1
        	k+=1
        	print "\n**************************"

if __name__ == '__main__':
    	#Input files required for classification
    	trainingfile = "../_data/HC_Reform_Train.csv"
    	testingfile = "../_data/HC_Reform_Test.csv"
	fullfile = "../_data/HC_Reform_Updated.csv"
	
	illnessCategory = []
	illnessCode = []
	race = []
	insurer = []
	date = []
	county = []
	zip = []
	tData = []
	labelTypes = []	
	with open(fullfile, 'rU') as fileData:
		fileR = csv.reader(fileData, delimiter=',', quotechar='|')
		headers = fileR.next()
		
		for line in fileR:
			illnessCode.append(line[0])
			illnessCategory.append(line[1])
			race.append(line[5])
			insurer.append(line[8])
			date.append(line[10][:-3])
			county.append(line[7])
			labelTypes.append(line[2])
			zip.append(line[6])
	fileData.close()
	
	illnessCode = list(set(illnessCode))
	illnessCategory = list(set(illnessCategory))
	sex = ['M', 'F']
	race = list(set(race))
	insurer = list(set(insurer))
	date = list(set(date))
	zip = list(set(zip))
	county = list(set(county))
	labelTypes = list(set(labelTypes))
	#print "Label types: ", labelTypes
	trainClassifier()
		
	predictions = testClassifier()
	#print "predictions:", predictions
	
	with open(testingfile, 'rU') as tf:
		outputResults(predictions, tf)
	tf.close()
