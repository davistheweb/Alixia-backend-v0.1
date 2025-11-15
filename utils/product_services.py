from functools import lru_cache
import httpx
from bs4 import BeautifulSoup
from functools import lru_cache
# import asyncio

async_client = httpx.AsyncClient(timeout=5)

@lru_cache(maxsize=50)
def cached_products_html(search: str, html: str):
    """Use caching for parsed results only."""
    return parse_products(html)


async def load_products(search: str):
    url = f"https://store.aliconnects.com/?product_cat=0&s={search}&post_type=product"

    r = await async_client.get(url)
    if r.status_code != 200:
        return ""

    return cached_products_html(search, r.text)
def parse_products(html: str):
    soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("ul.products li.product")[:6]

    products = []
    for c in cards:
        name = c.select_one("h2").get_text(strip=True) if c.select_one("h2") else ""
        price = c.select_one(".price").get_text(strip=True) if c.select_one(".price") else ""
        img = c.select_one("img")["src"] if c.select_one("img") else ""

        products.append(
            f"""
<div class="product">
    <img src="{img}" alt="{name}" />
    <h2>{name}</h2>
    <p>{price}</p>
</div>
"""
        )

    return "\n".join(products)
