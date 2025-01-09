import requests

api_url = "https://clashofclans.fandom.com/api.php"

buildings = ["Archer_Tower", "Cannon", "Double_Cannon", "Eagle_Artillery", "Inferno_Tower", "Mortar", "Wizard_Tower"]

def get_image_urls():

    api_url = "https://clashofclans.fandom.com/api.php"

    params = {
        "action": "query",
        "list": "allimages",
        "format": "json",
        "ailimit": "50",
    }

    all_images = []
    while True:
        response = requests.get(api_url, params=params)
        data = response.json()

        filtered_images = [
            image["url"]
            for image in data["query"]["allimages"]
            if any(building in image["name"] for building in buildings)
        ]
        all_images.extend(filtered_images)

        if "continue" in data:
            params["aicontinue"] = data["continue"]["aicontinue"]
        else:
            break

    for image_url in all_images:
        print(image_url)


get_image_urls()