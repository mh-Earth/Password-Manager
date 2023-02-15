from Encryption import EncryptSystem

# Run this code for resetting the data file

if __name__ == "__main__":
    data = {
        "catagoryList": [],
        "catagorypasswords": {

        },
        "catagories": {},

    }

    EncryptSystem(master_password="000").StoreJsonData("data.axx", data=data)


