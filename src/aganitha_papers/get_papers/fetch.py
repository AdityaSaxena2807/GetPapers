# get_papers/fetch.py
import requests
from typing import List, Dict

def fetch_pubmed_data(query: str, retmax: int = 50) -> List[Dict]:
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = f"{base}esearch.fcgi?db=pubmed&term={query}&retmode=json&retmax={retmax}"
    search_resp = requests.get(search_url)
    ids = search_resp.json()["esearchresult"]["idlist"]

    fetch_url = f"{base}efetch.fcgi?db=pubmed&id={','.join(ids)}&retmode=xml"
    fetch_resp = requests.get(fetch_url)
    return fetch_resp.text
