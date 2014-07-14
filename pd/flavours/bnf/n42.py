
import RDF

import json
import sys
from dateutil import parser 
from dateutil.relativedelta import relativedelta
import datetime

def evaluate_question(model, *args, **kwargs):
	
	#return True
	q = """
	prefix bio: <http://vocab.org/bio/0.1/> 
	SELECT  ?x 
	WHERE {
		?c bio:Death ?x.
	}
	"""
	#print model
	que = RDF.Query(q, query_language="sparql")
	result = que.execute(model)
	#print >> sys.stderr, "PORCODIO", result
	#print result
	for row in result:
		date = str(row['x'])
	d = parser.parse(date)
	
	return d < datetime.datetime.now() - relativedelta(years=70)

