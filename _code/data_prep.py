
try:
    data_file06_1 = open("HCReform_csv/HC_ReformFY06-1.csv", 'r')
    data_file06_2 = open("HCReform_csv/HC_ReformFY06-2.csv", 'r')
    data_file07_1 = open("HCReform_csv/HC_ReformFY07-1.csv", 'r')
    data_file07_2 = open("HCReform_csv/HC_ReformFY07-2.csv", 'r')
    data_file08_1 = open("HCReform_csv/HC_ReformFY08-1.csv", 'r')
    data_file08_2 = open("HCReform_csv/HC_ReformFY08-2.csv", 'r')
except IOError:
    print("Can't open input file")
    os.exit(1)

df06_1_list = data_file06_1.readlines()
data_file06_1.close() 


df06_2_list = data_file06_2.readlines()
data_file06_2.close() 


df07_1_list = data_file07_1.readlines()
data_file07_1.close() 


df07_2_list = data_file07_2.readlines()
data_file07_2.close() 


df08_1_list = data_file08_1.readlines()
data_file08_1.close() 


df08_2_list = data_file08_2.readlines()
data_file08_2.close() 

df_full_list = df06_1_list + df06_2_list + df07_1_list + df07_2_list + df08_1_list + df08_2_list

print "Total number of records: " + str(len(df_full_list))

icd9_categories = {
"infectious and parasitic diseases": range(001,140),
"neoplasms": range(140,240), 
"endocrine nutritional metabolic diseases and immunity disorders": range(240,280),
"diseases of the blood and blood-forming organs": range(280,290),
"mental disorders": range(290,320),
"nervous system disorders": range(320,360),
"sense organs disorders": range(360,390),
"circulatory system disorders": range(390,460),
"respiratory system disorders": range(460,520),
"digestive system disorders": range(520,580),
"genitourinary system disorders": range(580,630),
"complications of pregnancy childbirth and the puerperium": range(630,680),
"skin and subcutaneous tissue disorders": range(680,710),
"musculoskeletal system and connective tissue disorders": range(710,740),
"congenital anomalies": range(740,760),
"conditions originating in the perinatal period": range(760,780),
"symptoms signs and ill-defined conditions": range(780,800),
"injury and poisoning": range(800,1000),
"external causes of injury and supplemental classification": ['E','V']
}


for i in range(len(df_full_list)):
	df_full_list[i] = df_full_list[i].strip().split(",") 

for i in range(len(df_full_list)): 
	if df_full_list[i][1] == '0':
		df_full_list[i][1] = 'Sent Home'
	elif df_full_list[i][1] == '1':
		df_full_list[i][1] = 'Admitted'
	elif df_full_list[i][1] == '2':
		df_full_list[i][1] = 'Eloped'
	# df_full_list[i][2] = int(df_full_list[i][2])
	if df_full_list[i][9] == '1':
		df_full_list[i][9] = '2006'
	elif df_full_list[i][9] == '2':
		df_full_list[i][9] = '2007'
	elif df_full_list[i][9] == '3':
		df_full_list[i][9] = '2008'
	if df_full_list[i][0] != '':
		df_full_list[i][0] = df_full_list[i][0][0:3]
		if df_full_list[i][0][0:1] in ['E','V']:
			df_full_list[i].insert(1, "external causes of injury and supplemental classification")
		else:
			for key,value in icd9_categories.items():
				if int(df_full_list[i][0]) in value: 
					df_full_list[i].insert(1, key)
	else:
		df_full_list[i][0] = '000'
		df_full_list[i].insert(1, "None")
	if df_full_list[i][6] == 'Unknown':
		df_full_list[i][6] = '00000'
	df_full_list[i][6] = df_full_list[i][6][0:5]

# for i in range(50,60):
# 	print df_full_list[i]

out_file = open("HCReform_csv/HCReform_fullfile.csv", 'w')
for each in df_full_list:
	line_str = ""
	for item in each:
		line_str += str(item) + ","
	line_str = line_str.strip(",")
	print >>out_file, line_str
out_file.close()


