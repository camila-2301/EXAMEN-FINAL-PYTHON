import sys
import csv

if len(sys.argv) != 3:
	print("Usage: python dna.py data.csv sequence.txt ")
else:
	data = sys.argv[1]
	seqPath = sys.argv[2]

	sequence = None
	with open(seqPath, 'r') as f:
		sequence = f.readline()

	dataCSV = None
	with open(data, newline='') as csvfile:
		dataCSV = csv.DictReader(csvfile)
		strs = dataCSV.fieldnames[1:]

		cuenta = []	
		for cadena in strs:
			for i in range(100):
				if not cadena*i in sequence:
					break
			cuenta.append(i-1)
		for row in dataCSV:
			if int(row[strs[0]]) == cuenta[0] and int(row[strs[1]]) == cuenta[1] and int(row[strs[2]]) == cuenta[2]:
				print(row['name'])
				exit()
		print("No match")

