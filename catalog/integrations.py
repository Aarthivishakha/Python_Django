"""Currency-conversion lookup used by the storefront's price display.

A genuine use of the `requests` dependency pinned in requirements.txt -
that pin is intentionally an old release with published CVEs, which is
what gives pip-audit a real finding against this project's own dependency
set rather than an unrelated fixture.
"""

import requests

EXCHANGE_RATE_API = "https://api.exchangerate.example/latest"


def fetch_usd_rate(currency: str) -> float:
    """Fetch the USD conversion rate for `currency`.

    Tests mock this function rather than requiring network access.
    """
    response = requests.get(EXCHANGE_RATE_API, params={"base": "USD", "symbols": currency}, timeout=5)
    response.raise_for_status()
    data = response.json()
    return float(data["rates"][currency])
