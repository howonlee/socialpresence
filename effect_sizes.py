import csv, json

paperCsv = csv.DictReader(open("total_papers.csv"))
papers = {}

def getPaperInformation(row):
	pass

if __name__ == '__main__':
	for row in paperCsv:
		papers[row["Title"]] = getPaperInformation(row)
	for stuff in metanalysis:
		do the metanalysis
