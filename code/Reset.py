from Encryption import EncryptSystem

# Run this code for resetting the data file

if __name__ == "__main__":
    data = {'catagoryList': ['kau', 'work', 'fun'], 'catagorypasswords': {'1': '1', 'test': '1', 'kau': '111', 'work': '111', 'fun': '111', 'fun1': '111'}, 'catagories': {'kau': {
        '1': {'id': '1', 'email': 'abdalluh@gmail.com', 'tag': 'league of legends', 'password': 'lnT3WzFPAEs0Ytf3', 'url': 'Riot.com', 'username': 'Takez1', 'catagory': 'kau'}}, 'work': {},'fun': {}}}

    EncryptSystem(master_password="000").StoreJsonData("data.axx", data=data)
