def extraire_td(rss_file):
	import sys
	import feedparser
	
	# Chemin du fichier XML
	rss_file = sys.argv[1]
	
	# Analyse du fichier XML
	feed = feedparser.parse(rss_file)
	
	# Parcourir les éléments <item> du fichier RSS
	for entry in feed.entries:
    		title = entry.title
    		description = entry.description
    		print(f"{title}")
   		print(f"{description}\n")
    
    

