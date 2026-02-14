import requests
import json

def load_smartphones():
    response = requests.get("https://dummyjson.com/products")
    api_data = response.json()
    products = api_data["products"]

    with open("db.json", "r") as f:
        db = json.load(f)

    if "smartphones" not in db:
        db["smartphones"] = {}

    last_id = len(db["smartphones"])

    for i, product in enumerate(products[:30], start=last_id+1):
        db["smartphones"][str(i)] = {
            "brand": product.get("brand", "Unknown"),
            "model": product.get("title", "No title"),
            "price": f"${product.get('price', 0)}",
            "battery": product.get("batteryCapacity", "Unknown"),
            "image": product.get("thumbnail", "")
    }


    with open("db.json", "w") as f:
        json.dump(db, f, indent=4)

    


if __name__ == "__main__":
    load_smartphones()
