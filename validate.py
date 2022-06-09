import requests
r = requests.get("https://sfsymbols.com")


def isValid(symbol):
    if symbol in r.text:
        return True
    else:
        return False
