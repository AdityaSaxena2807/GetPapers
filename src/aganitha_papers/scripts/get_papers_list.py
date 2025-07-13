# scripts/get_papers_list.py
import click
from aganitha_papers.get_papers.fetch import fetch_pubmed_data
from aganitha_papers.get_papers.filter import parse_pubmed_xml
from aganitha_papers.get_papers.export import export_to_csv, print_results
from aganitha_papers.get_papers.utils import debug_print

@click.command()
@click.argument("query")
@click.option("-d", "--debug", is_flag=True)
@click.option("-f", "--file", type=str)
def main(query, debug, file):
    if debug:
        print(f"[DEBUG] Query: {query}")
    xml_data = fetch_pubmed_data(query)
    results = parse_pubmed_xml(xml_data)
    
    if not results:
        print("No results with non-academic authors found.")
        return

    if file:
        export_to_csv(results, file)
        print(f"Results saved to {file}")
    else:
        print_results(results)
        
    debug_print(f"Query: {query}", debug)

if __name__ == "__main__":
    main()
