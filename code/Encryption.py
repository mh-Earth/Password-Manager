import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import json


class Encrypt:
    _backend = default_backend()
    _iterations = 100_000

    def __init__(self) -> None:
        # master_password: str
        key = "3swH6SyUCTAZ0GRYqnOFuuRZ_ra8q2k8HHGC-GwV_Cc="
        self.Fernet = Fernet(key, self._backend)

        # password = bytes(master_password,encoding='utf8')
        # salt = os.urandom(16)
        # kdf = PBKDF2HMAC(
        #     algorithm=hashes.SHA256(),
        #     length=32,
        #     salt=salt,
        #     iterations=self._iterations,
        #     )
        # key = b64e(kdf.derive(password))
        # token = f.encrypt(b"Secret message!")
        # print(token)

    def generate_key(self) -> bytes:
        return self.Fernet.generate_key()

    def Decrypt(self, token: bytes) -> bytes:
        return self.Fernet.decrypt(token)

    def Encrypt(self, token: bytes) -> bytes:
        return self.Fernet.encrypt(token)

    # Encrypt a File
    def EncryptFile(self, FilePath: str) -> None:

        with open(FilePath, "rb") as f:
            encryptData = self.Encrypt(f.read())

        with open(FilePath, "wb") as f:
            f.write(encryptData)

    def DecryptFile(self, FilePath: str) -> None:
        '''
        Load a Encrypt file and decrypt it
        '''

        with open(FilePath, "rb") as f:
            data = self.Decrypt(f.read())

        with open(FilePath, "wb") as f:
            f.write(data)

        return None

    def loadJsonData(self, filePath: str) -> dict:

        # Decrypt a json encrypted file and pares the valid json str to python dict

        with open(filePath, "rb") as f:

            data = self.Decrypt(f.read())

            try:
                jsonData = json.loads(data.decode("utf8").replace("'", '"'))
                return jsonData

            except Exception as e:
                print(e)

	#  Encrypt a python dict and store it in a file
    def StoreJsonData(self, filePath: str, data: dict) -> None:

        with open(filePath, "wb") as f:
            data = bytes(str(data), encoding='utf8')
            f.write(self.Encrypt(token=data))


if __name__ == "__main__":
    a = Encrypt(
		
	)

    # a.EncryptFile("test.json")
    # a.DecryptFile(FilePath="test.txt")
    a.loadJsonData("test.json")
    demoData = {
        "catagoryList": [],
        "catagorypasswords": {

        },
        "catagories": {}

    }

    # a.StoreJsonData("test.json",data=demoData)
