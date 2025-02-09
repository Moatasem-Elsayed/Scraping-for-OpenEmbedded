import argparse
from tabulate import tabulate
from openEmbedded.parse import scrape


def cli():
    parser = argparse.ArgumentParser(
        prog="Scraping-for-OpenEmbedded",
        description="Scrape Recipe Information from (https://layers.openembedded.org/)",
        epilog="All rights reserved",
    )

    parser.add_argument(
        "-s",
        "--term",
        required=True,
        type=str,
        help="name of recipe search term",
    )
    parser.add_argument(
        "-p",
        "--pretty",
        action=argparse.BooleanOptionalAction,
        default=False,
        help="print results as table (tabulate)",
    )

    args = parser.parse_args()

    erg: list[tuple[str, str, str, str]] = scrape(args.term)
    if args.pretty:
        print(
            tabulate(
                erg,
                headers=["Name", "Version", "Description", "Layer"],
                tablefmt="grid",
            )
        )
    else:
        print(erg)


if __name__ == "__main__":
    cli()
