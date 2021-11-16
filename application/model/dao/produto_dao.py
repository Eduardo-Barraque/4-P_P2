import json

with open(url_for('static',filename="products.json")) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()