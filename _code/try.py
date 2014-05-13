import csv
from collections import Counter
from collections import OrderedDict
from datetime import datetime
import json

file = "../_data/HC_Reform.csv"
date = []
race = []
with open(file, 'rU') as fileData:
	fileR = csv.reader(fileData, delimiter=',', quotechar='|')
        headers = fileR.next()

        for line in fileR:
        	date.append(line[8])
                race.append(line[4])
fileData.close()

dates = Counter(date)
ordered_dates = OrderedDict((datetime.strptime(k, '%d-%b-%y'), v)
                       for k, v in sorted(dates.iteritems()))
ordered_dates = OrderedDict((datetime.strftime(k,'%d-%b-%y'),v) for k, v in sorted(ordered_dates.iteritems()))
#ordered_dates = dict(ordered_dates)

#dates_json = json.dumps(ordered_dates,ensure_ascii=False)

writer = csv.writer(open('dict.csv', 'wb'))
for key, value in ordered_dates.items():
   writer.writerow([key, value])
