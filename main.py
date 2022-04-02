import eel
import re
import json
import src.packages.selfLearnMgmt as slm

nameExpression = re.compile("[가-힣]+ \(")

with open("src/properties.json") as f:
    global properties
    properties = json.load(f)

eel.init('src/web')


@eel.expose
def initialize():
    print("initializing")

    userId = False
    userPassword = False

    if properties["saveCredentials"]["saveId"] == True:
        userId = properties["saveCredentials"]["credentials"]["id"]

    if properties["saveCredentials"]["savePassword"] == True:
        userPassword = properties["saveCredentials"]["credentials"]["password"]

    eel.fillCredentialsToJs(userId, userPassword)


@eel.expose
def login(id, password, saveId, savePassword):
    global properties
    print(properties)
    print("logging in...")
    returnedCredential = slm.login(id, password)
    print(returnedCredential)

    if returnedCredential == False:
        eel.loginReturnToJs(False, {})

    else:
        name = nameExpression.search(returnedCredential)[0][:-2]

        if "독서실좌석NO" in returnedCredential:
            eel.loginReturnToJs(True, {
                "isTeacher": False,
                "name": name
            })

        else:
            eel.loginReturnToJs(True, {
                "isTeacher": True,
                "name": name
            })

            diff = {
                "saveCredentials": {
                    "saveId": saveId,
                    "savePassword": savePassword,
                    "credentials": {
                        "id": id,
                        "password": password
                    }
                }
            }

            if diff["saveCredentials"] != properties["saveCredentials"]:
                with open("src/properties.json") as f:
                    properties = json.load(f)
                    properties.update(diff)

                with open("src/properties.json", "w") as f:
                    json.dump(properties, f)


eel.start("index.html", size=(800, 600))
