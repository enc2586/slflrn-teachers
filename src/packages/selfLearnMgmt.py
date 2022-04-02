from bs4 import BeautifulSoup
import requests as req
import json

BASE_URL = "http://www.cbshself.kr/"

SIGNIN_URL = BASE_URL + "sign/actionLogin.do"


def cleanUp(str):
    stringList = str.split()
    result = " ".join(stringList)
    return result


def login(id, password):
    userData = {
        "id": id,
        "password": password
    }

    res = req.post(SIGNIN_URL, data=userData)
    page = BeautifulSoup(res.content.decode("utf-8"), "html.parser")

    credentialTag = page.find("li", {"class": "pl-3"})

    if credentialTag == None:
        return False

    else:
        credential = cleanUp(credentialTag.get_text())
        return credential
