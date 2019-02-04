import ijson
import sys
# incrementally parse a json file for required content

gcurrent = dict()
def save(prefix, value):
    global gcurrent
    key = prefix.split('.')[-1]
    gcurrent[key] = value

def emit(ignored1, ignored2):
    global gcurrent
    if len(gcurrent) == 3:
        print '"{LotUrl}","{_type}","{name}"'.format(**gcurrent)
    gcurrent = {}

table = [('.LotUrl', 'string', save),#http://catalogues.lesliehindman.com/asp/fullCatalogue.asp?salelot=1++++++494+
	 ('._type', 'string', save), #Position
	 ('.name', 'string', save),  # Aaron Bohrod
	 ('CalaisRawRes', 'start_map', emit)]

with open(sys.argv[1]) as f:
     for prefix, event, value in ijson.parse(f):
	#print "\t\t(%s, %s, %s)" % (prefix.split('.')[-1], event, value)
	for p, e, f in table:
	    if prefix.endswith(p) and e == event:
		f(prefix, value)	

emit(None, None) # for the last record
