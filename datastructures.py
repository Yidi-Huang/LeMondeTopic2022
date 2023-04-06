from typing import List, Dict
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Token:
    forme: str
    lemme: str
    pos: str   


@dataclass
class Article:
    titre: str
    description: str
    analyse: List[Token]

@dataclass
class Corpus:
    categories: List[str]
    begin: str
    end: str
    chemin: Path
    articles: List[Article]


