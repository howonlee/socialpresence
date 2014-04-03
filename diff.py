import csv, json

howon = csv.DictReader(open("howon.csv"))
roberto = csv.DictReader(open("roberto.csv"))
titles1 = set()
titles2 = set()
for row in howon:
	titles1.add(row["Title"].lower())
for row in roberto:
	titles2.add(row["Title"].lower())
print "in 1, but not in 2: "
print "=================="
print json.dumps(sorted(list(titles1 - titles2)), sort_keys=True, indent=4, separators=(',', ': ')) # in 1, not in 2
print "in 2, but not in 1: "
print "=================="
print json.dumps(sorted(list(titles2 - titles1)), sort_keys=True, indent=4, separators=(',', ': ')) # in 2, not in 1
print "in both:"
print "=================="
print json.dumps(sorted(list(titles1 & titles2)), sort_keys=True, indent=4, separators=(',', ': ')) # in both
