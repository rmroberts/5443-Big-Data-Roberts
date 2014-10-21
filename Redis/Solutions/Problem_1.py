import string
import json
import redis

def is_json(myjson):
	try:
		json_object = json.loads(myjson)
	except ValueError, e:
		return False
	return True

r = redis.StrictRedis(host='localhost', port=6379, db=0)

f = open('/var/www/html/BigData/Redis/nutrition.json', 'r')
count = 0
json_count = 0

for line in f:
	count += 1
	line = filter(lambda x: x in string.printable, line)
	line = line.strip()
	#remove the extra commas
	if len(line) != 0:
		if line[0] != '{' and line[-1] != '}':
			line = line[1:-1]
		elif line[-1] != '}':
			line = line[:-1]
	if is_json(line):
		line = json.loads(line)
		#unique items are assumed to be those with unique ids, 
		#so ids are added to a set
		id = line["_id"]
		#add to set of ids, will not have duplicates
		r.sadd('ids',id)
		json_count += 1
	
#print cardinality of set, which will be number of unique items
print "Unique items: ",r.scard('ids')
print "Lines loaded: ",json_count
print "Lines processed: ",count

r.flushdb()