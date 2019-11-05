import couchdb
import json
from couchdb import design

# city1 = ['sydney', 'adelaide', 'south_yarra', 'calton']
# city2 = ['melbourne', 'brisbane', 'kew', 'bundoora']
# city3 = ['perth', 'canberra', 'clayton', 'camberwell']
# city4 = ['cbd', 'doncaster', 'preston', 'brighton']

viewDB_time={
	"time-view19" : {
		"map":"function(doc) {"
			  "if (doc.year==2019){"
			  "emit(doc.year,doc.compound);}}",
		"reduce":"function(keys, values, rereduce) {var sen=0.0; if(rereduce){}"
				 "return sum(values)/values.length;}"
	},
	"time-view18": {
		"map":"function(doc) {"
			  "if (doc.year==2018){"
			  "emit(doc.year,doc.compound);}}",
		"reduce":"function(keys, values, rereduce) {var sen=0.0; if(rereduce){}"
				 "return sum(values)/values.length;}"
	}
	,
	"time-view17": {
		"map":"function(doc) {"
			  "if (doc.year==2017){"
			  "emit(doc.year,doc.compound);}}",
		"reduce":"function(keys, values, rereduce) {var sen=0.0; if(rereduce){}"
				 "return sum(values)/values.length;}"
	},
}

viewDB_text={
	"text_view19_Jan":{
		"map":"function(doc){"
			  "if(doc.year==2019 & ){"
			  	"emit(doc.year,doc.text);}"
			  "}"
	},
	"text_view19_Fab":{
		"map":"function(doc){"
			  "if(doc.year==2019){"
			  	"emit(doc.year,doc.text);}"
			  "}"
	},
	"text_view19_Mar":{
		"map":"function(doc){"
			  "if(doc.year==2019){"
			  	"emit(doc.year,doc.text);}"
			  "}"
	},
	"text_view19_Apr":{
		"map":"function(doc){"
			  "if(doc.year==2019){"
			  	"emit(doc.year,doc.text);}"
			  "}"
	},
	"text_view19_May":{
		"map":"function(doc){"
			  "if(doc.year==2019){"
			  	"emit(doc.year,doc.text);}"
			  "}"
	},
	"text_view19_Jun":{
		"map":"function(doc){"
			  "if(doc.year==2019){"
			  	"emit(doc.year,doc.text);}"
			  "}"
	},
	"text_view19_Jul":{
		"map":"function(doc){"
			  "if(doc.year==2019){"
			  	"emit(doc.year,doc.text);}"
			  "}"
	},
	"text_view19_Aug":{
		"map":"function(doc){"
			  "if(doc.year==2019){"
			  	"emit(doc.year,doc.text);}"
			  "}"
	},
	"text_view19_Sep": {
		"map": "function(doc){"
			   "if(doc.year==2019){"
			   "emit(doc.year,doc.text);}"
			   "}"
	}
}


def create_design_doc(city,design, view):
	# try:
	city[design] = dict(language='javascript', views=view)
		#cities
		# sydney[design] = dict(language='javascript', views=view)
		# perth[design] = dict(language='javascript', views=view)
		# brisbane[design] = dict(language='javascript', views=view)
		# melbourne[design] = dict(language='javascript', views=view)
		# canberra[design] = dict(language='javascript', views=view)

		#small cities
		# south_yarra[design] = dict(language='javascript', views=view)
		# calton[design] = dict(language='javascript', views=view)
		# kew[design] = dict(language='javascript', views=view)
		# bundoora[design] = dict(language='javascript', views=view)
		# clayton[design] = dict(language='javascript', views=view)
		# camberwell[design] = dict(language='javascript', views=view)
		# cbd[design] = dict(language='javascript', views=view)
		# docaster[design] = dict(language='javascript', views=view)
		# preston[design] = dict(language='javascript', views=view)
		# brighton[design] = dict(language='javascript', views=view)

	# except:
	# 	del	melbourne[design]
	# 	melbourne[design] = dict(language='javascript', views=view)
		# del sydney[design]
		# sydney[design] = dict(language='javascript', views=view)
		# del perth[design]
		# perth[design] = dict(language='javascript', views=view)
		# del brisbane[design]
		# brisbane[design] = dict(language='javascript', views=view)

if __name__ == '__main__':
	print('start')
	couch = couchdb.Server('http://admin:project@45.113.234.34:5984')
	# cities=['sydney1','adelaide1','south_yarra1','calton1']
	# cities=['kew2','bundoora2','brisbane2','melbourne2']
	# cities=['clayton3','camberwell3','perth3','canberra3']
	cities=['cbd4','preston4','brighton4','doncaster4']
	for city in cities:
		print(city)
		db=couch[city]
		create_design_doc(db,'_design/mapview', viewDB_time)
		# create_design_doc(db,'_design/textview', viewDB_text)
		# create_design_doc('_design/foodtags', viewDB_topic)
	print("done")