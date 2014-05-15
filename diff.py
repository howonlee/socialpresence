import csv, json, sys, string, unicodedata

first_list = csv.DictReader(open(sys.argv[1]))
second_list = csv.DictReader(open(sys.argv[2]))
titles1 = set()
titles2 = set()
for row in first_list:
	first_title = row["Title"].lower()
	first_title = first_title.replace("-", " ")
	first_title = first_title.replace("\n", "")
	first_title = first_title.decode('unicode_escape').encode('ascii', 'ignore')
	first_title = first_title.translate(string.maketrans("",""), string.punctuation)
	titles1.add(first_title)
for row in second_list:
	second_title = row["Title"].lower()
	second_title = second_title.replace("-", " ")
	second_title = second_title.replace("\n", "")
	second_title = second_title.decode('unicode_escape').encode('ascii', 'ignore')
	second_title = second_title.translate(string.maketrans("",""), string.punctuation)
	titles2.add(second_title)
print "in 1, but not in 2: "
print "count: ", len(list(titles1 - titles2))
print "=================="
print json.dumps(sorted(list(titles1 - titles2)), sort_keys=True, indent=4, separators=(',', ': ')) # in 1, not in 2
print "in 2, but not in 1: "
print "count: ", len(list(titles2 - titles1))
print "=================="
print json.dumps(sorted(list(titles2 - titles1)), sort_keys=True, indent=4, separators=(',', ': ')) # in 2, not in 1
print "in both:"
print "count: ", len(list(titles1 & titles2))
print "=================="
print json.dumps(sorted(list(titles1 & titles2)), sort_keys=True, indent=4, separators=(',', ': ')) # in both
