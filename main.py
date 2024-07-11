import requests
import common


# def add_new_product(sku, prices):
def add_new_product(sku):
    add_new_product_url = f"{common.get_api_base_url()}/products.json"

    values = ['10K White Gold', '10K Yellow Gold', '10K Rose Gold', '14K White Gold', '14K Yellow Gold',
              '14K Rose Gold', '18K White Gold', '18K Yellow Gold', '18K Rose Gold']

    variants = []
    for value in values:
        # price = common.get_variant_price(value, prices)
        # price = round(int(price) / 10) * 10
        variants.append({"option1": value, "price": 999, "sku": sku})

    folder_path = fr"D:\EWS\{sku}"
    images = common.get_images_from_folder(folder_path)

    product_type = common.get_type_from_file()

    payload = {
        "product": {
            "title": sku,
            "body_html": common.get_description(product_type[sku]),
            "vendor": "ES-moissanite",
            "product_type": product_type[sku],
            "variants": variants,
            "options": [{"name": "Material", 'values': values}],
            "tags": f"{product_type[sku]}, {sku}",
            "images": images,
            "Category": product_type[sku],
            "status": "draft"
        }
    }

    response = requests.post(add_new_product_url, json=payload, headers=common.get_headers())

    response.raise_for_status()
    print(response.json())


# skus = [
#     "SMM003"
# ]

# sku_prices = common.get_prices_from_file()
types_dict = common.get_type_from_file()
skus = [key for key in types_dict]
# print(skus)
for sku in skus:
    # sku_price = sku_prices[sku]
    # add_new_product(sku, sku_price)
    add_new_product(sku)
