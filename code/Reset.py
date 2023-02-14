from Encryption import EncryptSystem

# Run this code for resetting the data file

data = {
    "catagoryList": [],
    "catagorypasswords": {

    },
    "catagories": {},

}


a = EncryptSystem(master_password="000")
a.StoreJsonData("data.axx", data=data)
