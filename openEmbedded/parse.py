from typing import Iterable
import urllib.request
from itertools import islice
from selectolax.parser import HTMLParser, Node


# TODO: either examine the redirects or count number of tables in the page
class RedirectHandler(urllib.request.HTTPRedirectHandler):
    is_redirected = False

    def redirect_request(self, *args, **kwargs):
        self.is_redirected = True
        return super().redirect_request(*args, **kwargs)


def raw_html(url: str) -> tuple[int, bool, bytes]:
    req = urllib.request.Request(url, method="GET")
    handler = RedirectHandler()
    builder = urllib.request.build_opener(handler)

    with builder.open(req) as r:
        return (r.status, handler.is_redirected, r.read())


def parse_html(html: str) -> HTMLParser:
    return HTMLParser(html)


def parse_recipe_table(node: Node) -> tuple[str, str, str, str]:
    first_table: Node = node.css_first("table")
    rows: list[Node] = first_table.css("tbody > tr")
    erg = list(
        map(
            lambda x: x.css_first("td").text(),
            rows,
        )
    )
    # TODO: assert erg length
    return (erg[0], erg[1], erg[3], erg[8])


def parse_search_table(node: Node) -> Iterable[tuple[str, str]]:
    first_table: Node = node.css_first("table")
    rows: list[Node] = first_table.css("tbody > tr")
    erg = map(
        lambda c: (
            next(c).text(),  # Recipe name
            next(c).text(),  # Version
            next(c).text(),  # Description
            next(c).text(),  # Layer
        ),
        map(lambda x: iter(x.css("td")), rows),
    )
    # TODO: assert erg length
    return erg


def scrape(term: str, limit: int = 5) -> list[tuple[str, str, str, str]]:
    _, is_redirect, content = raw_html(
        f"https://layers.openembedded.org/layerindex/branch/master/recipes/?q={term}"
    )
    if is_redirect:
        return [parse_recipe_table(parse_html(content))]
    return list(islice(parse_search_table(parse_html(content)), limit))
