import pickle

class Encryption:

    def loadObjFromFile(self,file):
        with open(file,'rb') as f:
            data = pickle.loads(f.read())
            return data

    def storeData(self,data,file):
        with open(file,'wb') as f:
            pickle.dump(data,f)
        
    




