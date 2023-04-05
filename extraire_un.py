#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import feedparser
import argparse

def extraire_td(rss_file):	
	# Créer un élément racine pour le fichier XML
	root = ET.Element("channel")
    
	# Analyse du fichier XML
	feed = feedparser.parse(rss_file)
	
	# Parcourir les éléments <item> du fichier RSS
	for entry in feed.entries:
		title = entry.title
		description = entry.description
		yield title, description

def main():
	parser = argparse.ArgumentParser(description='Extraction des titres et descriptions des articles d\'un flux RSS')
	parser.add_argument('chemin', nargs = '*', help='Chemin du fichier RSS')
	args = parser.parse_args()
	if len(args)>1 :
		rss_file = args.chemin[0]
		extraire_td(rss_file)
	else:
		print('Il manque un argument du chemin du fichier')

if __name__ == '__main__':
	main()

