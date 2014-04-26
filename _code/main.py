import csv
# from sklearn import svm

dataSet =[]
labels = []
with open('../_data/sample_HC_ReformFY06.csv', 'rb') as fileData:
	fileReader = csv.reader(fileData, delimiter=',', quotechar='|')
	headers = next(fileData, None)
	for line in fileReader:
		labels.append(line[1])
		line.pop(1)
		line[1] = int(line[1])
		line[8]= int(line[8])
		dataSet.append(line)
		
