# from Encryption import Encryption
from Encryption import Encrypt

# Run this code for resetting the data file

data = {
    "catagoryList": [],
    "catagorypasswords": {

    },
    "catagories": {},

}


a = Encrypt()
# a.storeData(data,"data.pkl")
a.StoreJsonData("data.axx", data=data)
# data = a.loadObjFromFile("data.pkl")
