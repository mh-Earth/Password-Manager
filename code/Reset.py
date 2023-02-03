from Encryption import Encryption

# Run this code for resetting the data file

data={
"catagoryList":[],
"catagorypasswords":{

},
"catagories": {},

}


    
a = Encryption()
a.storeData(data,"data.pkl")
# data = a.loadObjFromFile("data.pkl")