import config
import csv
import glob
import base64


def get_shop_url():
    return "https://" + config.SHOP_NAME + ".myshopify.com/"


def get_api_base_url():
    return "https://" + config.SHOP_NAME + ".myshopify.com/" + "admin/api/" + config.API_VERSION


def get_headers():
    return {"Content-Type": "application/json",
            "X-Shopify-Access-Token": config.ADMIN_TOKEN}


def get_initial_params():
    return {'limit': config.BATCH_SIZE}


def get_prices_from_file():
    prices = {}
    with open("Engagement Price.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            sku = line[0]

            prices[sku] = {
                "10k": line[1],
                "14k": line[2],
                "18k": line[3],
            }
    return prices


def get_type_from_file():
    types = {}

    with open('EWS type.csv', 'r') as t:
        reader = csv.reader(t, delimiter=',')

        for i, line in enumerate(reader):
            sku = line[0]
            types[sku] = line[1]

        return types


def get_images_from_folder(folder_path):
    images = []

    image_files = glob.glob(folder_path + '/*.jpg') + glob.glob(folder_path + '/*.jpeg') + glob.glob(
        folder_path + '/*.png') + glob.glob(folder_path + '/*.webp')

    for image_path in image_files:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

            image = {
                "attachment": encoded_string
            }
            images.append(image)

    return images


def get_variant_price(material, sku_price):
    if '10k' in material.lower():
        return sku_price['10k']
    if '14k' in material.lower():
        return sku_price['14k']
    if '18k' in material.lower():
        return sku_price['18k']


def get_params():
    return {"limit": config.BATCH_SIZE}


def get_description(product_type):
    return {
        "Engagement Ring": """<p><meta charset="utf-8"><span data-mce-fragment="1"> </span><b data-stringify-type="bold" data-mce-fragment="1">The showcased ring features a stunning 1.91 CT Oval Cut Moissanite as the center stone, complemented by elegant side stones.</b><br data-mce-fragment="1"><span data-mce-fragment="1"></span></p>
                              <p><span data-mce-fragment="1">✦</span><b data-stringify-type="bold" data-mce-fragment="1"><span data-mce-fragment="1"> </span>Center Stone: </b> 1.91 CT Oval Cut Moissanite (7.0 x 9.0 mm)</p>
                              <p><span data-mce-fragment="1">✦</span><b data-stringify-type="bold" data-mce-fragment="1"><span data-mce-fragment="1"> </span>Side Stones: </b> 0.27 CT total weight, Marquise & Round Cut Moissanite</p>
                              <p><span data-mce-fragment="1">✦</span><b data-stringify-type="bold" data-mce-fragment="1"><span data-mce-fragment="1"> </span>Color Grade: </b>  DEF (Colorless)</p>
                              <p><span data-mce-fragment="1">✦</span><b data-stringify-type="bold" data-mce-fragment="1"><span data-mce-fragment="1"> </span>Clarity Grade: </b> VVS</p>
                              <p><meta charset="utf-8"><span data-mce-fragment="1"> </span><b data-stringify-type="bold" data-mce-fragment="1">Discover our beautiful moissanite jewelry collection, available in 10KT, 14KT, and 18KT gold. Choose from Yellow gold, White gold, or Rose gold to find the perfect piece that suits your style.
                              </b><br data-mce-fragment="1"><span data-mce-fragment="1"></span></p>""",

        "Wedding Band": """<p><meta charset="utf-8"><span data-mce-fragment="1"> </span><b data-stringify-type="bold" data-mce-fragment="1">The showcased band features a stunning 0.5 TCW Round Cut Moissanites as the accent stones.</b><br data-mce-fragment="1"><span data-mce-fragment="1"></span></p>
                                    <p><span data-mce-fragment="1">✦</span><b data-stringify-type="bold" data-mce-fragment="1"><span data-mce-fragment="1"> </span>Accent Stones: </b>  0.5 CT total weight, Round Cut Moissanites</p>
                                    <p><span data-mce-fragment="1">✦</span><b data-stringify-type="bold" data-mce-fragment="1"><span data-mce-fragment="1"> </span>Color Grade: </b>  DEF (Colorless)</p>
                                    <p><span data-mce-fragment="1">✦</span><b data-stringify-type="bold" data-mce-fragment="1"><span data-mce-fragment="1"> </span>Clarity Grade: </b> VVS</p>
                                    <p><meta charset="utf-8"><span data-mce-fragment="1"> </span><b data-stringify-type="bold" data-mce-fragment="1">Discover our beautiful moissanite jewelry collection, available in 10KT, 14KT, and 18KT gold. Choose from Yellow gold, White gold, or Rose gold to find the perfect piece that suits your style.
                                    </b><br data-mce-fragment="1"><span data-mce-fragment="1"></span></p>""",

        "Bridal Set": """<p><meta charset="utf-8"><span data-mce-fragment="1">✦ </span><b data-stringify-type="bold" data-mce-fragment="1">A stunning 1.50 CT pear-cut moissanite (5.50 x 7.50 mm) is the focal point of this engagement ring.</b><br data-mce-fragment="1"><span data-mce-fragment="1"></span></p>
                             <p><span data-mce-fragment="1">✦</span><b data-stringify-type="bold" data-mce-fragment="1"><span data-mce-fragment="1"> </span>Engagement Ring Details: </b><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Center Stone: 1.50 Carat Pear Cut Moissanite</span><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Side Stones: Round brilliant cut moissanite</span><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Color: DEF(Colorless)</span><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Clarity: VVS</span><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Band Width: Approx. 2.0 mm</span></p>
                             <p><span aria-label="" class="c-mrkdwn__br" data-stringify-type="paragraph-break" data-mce-fragment="1"></span><b data-stringify-type="bold" data-mce-fragment="1">✦ Wedding Band Details:</b><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Side Stone Weight: 1.15 TCW</span><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Stone Cuts: Marquise and round brilliant cut Moissanite</span><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Moissanite Details: DEF color, VVS+ clarity</span><br data-mce-fragment="1"><span data-mce-fragment="1">✧ Band Width: Approx. 2.0 mm</span></p>
                             <p><meta charset="utf-8"><span data-mce-fragment="1"> </span><b data-stringify-type="bold" data-mce-fragment="1">This bridal set is designed to symbolize your eternal love with a perfect blend of elegance and brilliance. Discover our beautiful moissanite jewelry collection, available in 10KT, 14KT, and 18KT gold. Choose from Yellow gold, White gold, or Rose gold to find the perfect piece that suits your style.</b><br data-mce-fragment="1"><span data-mce-fragment="1"></span></p>""",

        "Necklace": "",
        "Earrings": "",
        "Earring": "",
        "Bracelet": "",
        "Men's Wedding Band": "",
        "Ring": "",
    }[product_type]

