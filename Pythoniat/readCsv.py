import csv 

file = open("countries.csv" , 'r')

rd = csv.reader(file)

for item in rd :
	print(item)