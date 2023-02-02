from Encryption import Encryption

# Run this code for resetting the data file

data={
"MasterPassword": "123456789",
"catagoryList":[],
"totalCatagory":0,
"catagorypasswords":{
    "game":"11",
    "social":"11",
    "work":"11"
},
"catagories": {},

}


    
a = Encryption()
a.storeData(data,"data.pkl")
# data = a.loadObjFromFile("data.pkl")