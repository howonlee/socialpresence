import csv, json, jsonschema, sys

"""
Always be passing around the whole data
everything is by ref in python-land and we would like the flexibility
"""

def getPaperInformation(dataFile):
	totalData = json.load(open(dataFile))
	for dat in totalData:
		jsonschema.validate(dat, schema)
	return totalData

if __name__ == '__main__':
	dataFile = "total_papers.json"
	schemaFile = "paper_schema.json"
	if sys.argv[1]:
		dataFile = sys.argv[1]
	if sys.argv[2]:
		schemaFile = sys.argv[2]
	schema = json.load(open(schemaFile))
	papers = getPaperInformation(dataFile)
	for paper in papers:
		do the metanalysis
