import requests
from bs4 import BeautifulSoup

def load_products(user_search):
    aliconnects_store_url = f"https://store.aliconnects.com/?product_cat=0&s={user_search}&post_type=product"
    response = requests.get(aliconnects_store_url)
    
    if response.status_code != 200:
        print("Failed to load the page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all relevant tags (without relying on class names)
    tags = soup.find_all(["h2", "p", "img"], limit=60)

    products = []
    product = {}

    for tag in tags:
        if tag.name == "h2" and "name" not in product:
            product["name"] = tag.text.strip()
        elif tag.name == "p" and "price" not in product:
            product["price"] = tag.text.strip()
        elif tag.name == "img" and "img" not in product:
            product["img"] = tag.get("src")
        
        # If we have all 3 keys, we assume it's a full product and store it
        if all(k in product for k in ("name", "price", "img")):
            products.append(product)
            product = {}  # reset for next product

    # Render each product like a frontend div
    for p in products:
        return (f"""
<div class="product">
  <img src="{p['img']}" alt="{p['name']}" />
  <h2>{p['name']}</h2>
  <p>{p['price']}</p>
</div>
""")
