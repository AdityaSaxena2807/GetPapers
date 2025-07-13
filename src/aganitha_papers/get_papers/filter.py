# get_papers/filter.py
import xml.etree.ElementTree as ET
from typing import List, Dict
import re


def is_non_academic(affiliation: str) -> bool:
    keywords = ["pharma", "biotech", "inc", "ltd", "llc", "corporation", "therapeutics"]
    academic_terms = ["university", "college", "institute", "hospital", "school", "faculty", "center"]
    aff_lower = affiliation.lower()
    return any(k in aff_lower for k in keywords) and not any(a in aff_lower for a in academic_terms)


def extract_email(text: str) -> str:
    """Extract the first email address found in a string using regex."""
    match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return match.group(0) if match else None


def parse_pubmed_xml(xml_data: str) -> List[Dict]:
    root = ET.fromstring(xml_data)
    results = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID") or "N/A"
        title = article.findtext(".//ArticleTitle") or "N/A"
        date = article.findtext(".//PubDate/Year") or "N/A"
        authors = article.findall(".//Author")

        non_academic_authors = []
        company_affiliations = []
        email = None

        for author in authors:
            aff = author.findtext("AffiliationInfo/Affiliation") or ""
            name = f"{author.findtext('ForeName', '')} {author.findtext('LastName', '')}".strip()

            if is_non_academic(aff):
                if name:
                    non_academic_authors.append(name)
                company_affiliations.append(aff)

                if not email:  # Extract only first email found
                    extracted = extract_email(aff)
                    if extracted:
                        email = extracted

        if non_academic_authors:
            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": date,
                "Non-academic Author(s)": "; ".join(non_academic_authors),
                "Company Affiliation(s)": "; ".join(company_affiliations),
                "Corresponding Author Email": email or "N/A"
            })

    return results