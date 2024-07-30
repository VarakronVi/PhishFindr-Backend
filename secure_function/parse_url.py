from typing import TypedDict
from urllib.parse import urlparse, urlunparse

class ParsedURL(TypedDict):
    base_url: str
    hostname: str
    scheme: str

def parse_url(link: str) -> ParsedURL:
    parsed_url = urlparse(link)

    base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
    hostname = parsed_url.hostname
    scheme = parsed_url.scheme

    return {
        "base_url": base_url,
        "hostname": hostname,
        "scheme": scheme
    }