from typing import Optional, List, Dict
import argparse
import sys
from datetime import date
from pathlib import Path
from xml.etree import ElementTree as et
import re


import extract_un_fil as euf
from datastructures import Corpus, Article, Token
from export_json import write_json
from export_xml import write_xml

MONTHS = ["Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug", 
          "Sep",
          "Oct",
          "Nov", 
          "Dec"]

DAYS = [f"{x:02}" for x in range(1,32)]

CAT_CODES =  {	
            'une' : '0,2-3208,1-0,0', 
            'international' : '0,2-3210,1-0,0',
            'europe' : '0,2-3214,1-0,0', 
            'societe' :	'0,2-3224,1-0,0',
            'idees'	: '0,2-3232,1-0,0',
            'economie':	'0,2-3234,1-0,0',
            'actualite-medias':	'0,2-3236,1-0,0',
            'sport': '0,2-3242,1-0,0',
            'planete': '0,2-3244,1-0,0',
            'culture': '0,2-3246,1-0,0',
            'livres' : '0,2-3260,1-0,0',
            'cinema' : '0,2-3476,1-0,0',
            'voyage' : '0,2-3546,1-0,0',
            'technologies': '0,2-651865,1-0,0',
            'politique' : '0,57-0,64-823353,0',
            'sciences' : 'env_sciences'
            }



def convert_month(m:str) -> int:
   return MONTHS.index(m) + 1

def parcours_path(corpus_dir:Path, categories: Optional[List[str]]=None, start_date: Optional[date]=None, end_date: Optional[date]=None):
    if categories is not None and len(categories) > 0:
        categories = [CAT_CODES[c] for c in categories]
    else:
        categories = CAT_CODES.values() # on prend tout

    for month_dir in corpus_dir.iterdir():
        if month_dir.name not in MONTHS:
            # on ignore les dossiers qui ne sont pas des mois
            continue
        m = convert_month(month_dir.name)
        for day_dir in month_dir.iterdir():
            if day_dir.name not in DAYS:
                # on ignore les dossiers qui ne sont pas des jours
                continue
            d = date.fromisoformat(f"2022-{m:02}-{day_dir.name}")
            if (start_date is None or start_date <= d) and (end_date is None or end_date >= d):
                for time_dir in day_dir.iterdir():
                    if re.match(r"\d\d-\d\d-\d\d", time_dir.name):
                        for fic in time_dir.iterdir():
                            if fic.name.endswith(".xml") and any([c in fic.name for c in categories]):
                                yield(fic)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", help="méthode de parsing (et, re ou fp)", default="et")
    parser.add_argument("-s", help="start date (iso format)", default="2022-01-01")
    parser.add_argument("-e", help="end date (iso format)", default="2023-01-01")
    parser.add_argument("-o", help="output file (stdout if not specified")
    parser.add_argument("corpus_dir", help="root dir of the corpus data")
    parser.add_argument("categories",nargs="*", help="catégories à retenir")
    args = parser.parse_args()
    if args.m == 'et':
        func = euf.extract_et
    elif args.m == 're':
        func = euf.extract_re
    elif args.m == 'fp':
        func = euf.extract_feedparser
    else:
        print("méthode non disponible", file=sys.stderr)
        sys.exit()
    # création du corpus
    corpus = Corpus(args.categories, args.s, args.e, args.corpus_dir, [])
    for f in parcours_path(Path(args.corpus_dir), 
            start_date=date.fromisoformat(args.s),
            end_date=date.fromisoformat(args.e),
            categories=args.categories):
        # fichier par fichier
        for article in func(f):
            # parcours article par article
            corpus.articles.append(article)

            
    # -> corpus
    write_xml(corpus,"corpus.xml")
    write_json(corpus,"corpus.json")
    # exemple : $ python3 extract_many.py -s "2022-01-01" -e "2022-01-02"   ./Corpus/2022 sport


