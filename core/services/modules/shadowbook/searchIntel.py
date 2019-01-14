#!/usr/bin/env python
# -*- coding: utf8 -*-

import os, sys
app_dir = os.path.dirname(os.path.abspath(__file__)) + '/../../../'
getESpath = app_dir + 'services/common'
sys.path.insert(0, getESpath)
from ES import getES
from getConf import getHippoConf

import logging
logger = logging.getLogger(__name__)

def littleMsearch(coreIntelligence, typeNameES, listParsedData):
	logger.info('searchIntel.littleMsearch launched')
	cfg = getHippoConf()
	indexNameES = cfg.get('elasticsearch', 'indexNameES')
	es = getES()

	#forging littleMsearch request
	#request to be sent to ES for littleMsearch
	req = list()
	#request header
	req_head = {'index': indexNameES, 'type': typeNameES}
	
	coreIntelligence = coreIntelligence
	#in the previous example, coreIntelligence is 'domain'
	for element in listParsedData:
	        req_body = {
	                'query' : {
	                        'bool' : {
	                                'must' : [
	                                        {
	                                                'match' : {
	                                                        coreIntelligence : element[coreIntelligence]
	                                                }
	                                        }
	                                ]
	                        }
	                }
	        }
	        req.extend([req_head, req_body])
	#req will look like
	#[{
	#        'index': 'hippocampe',
	#        'type': u 'malwaredomainsFree_dnsbhDOMAIN'
	#}, {
	#        'query': {
	#                'bool': {
	#                        'must': [{
	#                                'match': {
	#                                        u 'domain': 'skandastech.com'
	#                                }
	#                        }]
	#                }
	#        }
	#}, {
	#        'index': 'hippocampe',
	#        'type': u 'malwaredomainsFree_dnsbhDOMAIN'
	#}, {
	#        'query': {
	#                'bool': {
	#                        'must': [{
	#                                'match': {
	#                                        u 'domain': 'stie.pbsoedirman.com'
	#                                }
	#                        }]
	#                }
	#        }
	#}]

	res = es.msearch(body = req, max_concurrent_searches = 16)
	# res will look like
#{u'responses': [{u'_shards': {u'failed': 0, u'successful': 5, u'total': 5},
#                 u'hits': {u'hits': [{u'_id': u'AVOuC41q6EIAXcyxAFz0',
#                                      u'_index': u'hippocampe',
#                                      u'_score': 7.470799,
#                                      u'_source': {u'firstAppearance': u'20160325T145146+0100',
#                                                   u'idSource': u'AVOuCsBt6EIAXcyxAEn3',
#                                                   u'lastAppearance': u'20160325T145146+0100',
#                                                   u'source': u'https://openphish.com/feed.txt',
#                                                   u'url': u'https://www.myfridaygoodies.ch/sandbox/1/'},
#                                      u'_type': u'openphishFree_feedURL'}],
#                           u'max_score': 7.470799,
#                           u'total': 1},
#                 u'timed_out': False,
#                 u'took': 124},

#                {u'_shards': {u'failed': 0, u'successful': 5, u'total': 5},
#                 u'hits': {u'hits': [], u'max_score': None, u'total': 0},
#                 u'timed_out': False,
#                 u'took': 107},

#                {u'_shards': {u'failed': 0, u'successful': 5, u'total': 5},
#                 u'hits': {u'hits': [{u'_id': u'AVOuCxyD6EIAXcyxAFA0',
#                                      u'_index': u'hippocampe',
#                                      u'_score': 7.4480977,
#                                      u'_source': {u'firstAppearance': u'20160325T145117+0100',
#                                                   u'idSource': u'AVOuCsBt6EIAXcyxAEn3',
#                                                   u'lastAppearance': u'20160325T145117+0100',
#                                                   u'source': u'https://openphish.com/feed.txt',
#                                                   u'url': u'http://www.rutzcellars.com/dd-dd/art/'},
#                                      u'_type': u'openphishFree_feedURL'}],
#                           u'max_score': 7.4480977,
#                           u'total': 1},
#                 u'timed_out': False,
#                 u'took': 117}]}
	logger.info('searchIntel.littleMsearch end')
	return res

def bigMsearch(coreIntelligence, listParsedData):
	logger.info('searchIntel.bigMsearch launched')
	es = getES()

	cfg = getHippoConf()
	indexNameES = cfg.get('elasticsearch', 'indexNameES')

	req = list()
	req_head = {'index': indexNameES}
	
	coreIntelligence = coreIntelligence
	for element in listParsedData:
	        req_body = {
	                'query' : {
	                        'bool' : {
	                                'must' : [
	                                        {
	                                                'match' : {
	                                                        coreIntelligence : element[coreIntelligence]
	                                                }
	                                        }
	                                ]
	                        }
	                }
	        }
	        req.extend([req_head, req_body])

	res = es.msearch(body = req)
	logger.info('searchIntel.bigMsearch end')
	return res
if __name__ == '__main__':
	main()
