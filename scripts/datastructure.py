from typing import List, Dict
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Tokens:
    forme: str
    lemme: str
    pos: str

@dataclass
class Article:
    title: str
    descrption: str
    analyse : List[Tokens]

@dataclass
class Corpus:
    categories: List[str]
    begin: str
    end: str
    chemin: Path
    articles: List[Article]