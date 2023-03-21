#!//usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import feedparser

def extraire_td(rss_file):	
	
	# Analyse du fichier XML
	feed = feedparser.parse(rss_file)
	
	# Parcourir les éléments <item> du fichier RSS
	for entry in feed.entries:
		title = entry.title
		description = entry.description
		print(f"{title}")
		print(f"{description}\n")

if __name__ == '__main__':
	if len(sys.argv)>1:
		rss_file = sys.argv[1]
		extraire_td(rss_file)
	else:
		print('Il manque un argument du chemin du fichier')
  

