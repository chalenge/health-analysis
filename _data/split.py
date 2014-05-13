import csv

c = 0
train_list = []

train_file = open("HC_Reform_Test.csv", "wb")
test_file = open("HC_Reform_Train.csv", "wb")
data = []

with open("HC_Reform_Updated.csv", 'rU') as fileData:
                fileR = csv.reader(fileData, delimiter=',', quotechar='|')
                for line in fileR:
			data.append(line)
fileW1 = csv.writer(train_file, delimiter=',', quotechar='|')
fileW2 = csv.writer(test_file, delimiter=',', quotechar='|')
for item in data[:500]:
	fileW2.writerow(item)
for item in data[500:]:
	fileW1.writerow(item)


