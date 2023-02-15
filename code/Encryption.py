from EncryptCore import Encrypt
import json


class EncryptSystem():
    def __init__(self, master_password: str) -> None:
        """Initialize the Encrypt class."""
        self.Encryption = Encrypt(master_password=master_password)

    # Encrypt a File
    def EncryptFile(self, FilePath: str) -> None:

        # Read the file
        with open(FilePath, "rb") as f:
            # Encrypt the read data
            encryptData = self.Encryption.encrypt(f.read())

        # Write the encrypted data in the file
        with open(FilePath, "wb") as f:
            f.write(encryptData)

    def DecryptFile(self, FilePath: str) -> None:
        '''
        Load a Encrypt file and decrypt it
        '''

        with open(FilePath, "rb") as f:
            # Read the encrypted file
            data = self.Encryption.decrypt(f.read())

        with open(FilePath, "wb") as f:
            # Write the decrypted data in the file
            f.write(data)

        return None

    def loadJsonData(self, filePath: str) -> dict:

        # Decrypt a json encrypted file and pares the valid json str to python dict

        with open(filePath, "rb") as f:

            # Read the encrypted file
            data = self.Encryption.decrypt(f.read())

            try:
                # Parse the json string to python dict
                jsonData = json.loads(data.decode("utf8").replace("'", '"'))
                return jsonData

            except Exception as e:
                print(e)

	#  Encrypt a python dict and store it in a file
    def StoreJsonData(self, filePath: str, data: dict) -> None:

        with open(filePath, "wb") as f:
            # Convert the python dict to json string
            data = bytes(str(data), encoding='utf8')
            # Encrypt the json string and write it in the file
            f.write(self.Encryption.encrypt(token=data))
