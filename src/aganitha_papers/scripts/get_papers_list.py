# scripts/get_papers_list.py
import click
from aganitha_papers.get_papers.fetch import fetch_pubmed_data
from aganitha_papers.get_papers.filter import parse_pubmed_xml
from aganitha_papers.get_papers.export import export_to_csv, print_results
from aganitha_papers.get_papers.utils import debug_print

@click.command()
@click.argument("query")
@click.option("-d", "--debug", is_flag=True, help="Enable debug logging.")
@click.option("-f", "--file", type=str, help="CSV filename to save the output.")
def main(query: str, debug: bool, file: str | None) -> None:
    """Fetch and process PubMed papers based on a query."""

    debug_print(f"Query: {query}", debug)

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

if __name__ == "__main__":
    main()
