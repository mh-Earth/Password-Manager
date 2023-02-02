import pickle

class Encryption:

    def loadObjFromFile(self,file):
        with open(file,'rb') as f:
            data = pickle.loads(f.read())
            return data

    def storeData(self,data,file):
        with open(file,'wb') as f:
            pickle.dump(data,f)
        
    

if __name__ == "__main__":

    # Run this code for resetting the data file

    data={
    "MasterPassword": "123456789",
    "catagoryList":["game","social","work"],
    "totalCatagory":3,
    "catagorypasswords":{
        "game":"11",
        "social":"11",
        "work":"11"
    },
    "catagories": {

        "game": {
            "1": {
                "id": 1,
                "email": "email",
                "tag": "tag",
                "password": "password",
                "url": "www.google.com"
            }
        },
        
        "social": {
            "1": {
                "id": 1,
                "email": "email",
                "tag": "tag",
                "password": "password",
                "url": "www.google.com"
            }
        },

        "work": {
            "1": {
                "id": 1,
                "email": "email",
                "tag": "tag",
                "password": "password",
                "url": "www.google.com"
            },
            "2": {
                "id": 2,
                "email": "email",
                "tag": "tag",
                "password": "password",
                "url": "www.google.com"
            },
            "3": {
                "id": 3,
                "email": "email",
                "tag": "tag",
                "password": "password",
                "url": "www.facebook.com"
            },
        }
    }
}
    
    a = Encryption()
    a.storeData(data,"data.pkl")
    # data = a.loadObjFromFile("data.pkl")



