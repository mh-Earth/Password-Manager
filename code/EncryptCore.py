import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


'''
Class Encrypt is a class that creates a key based on the password and salt
and then encrypts the data given with that key using Fernet

Class Decrypt is a class that decrypts the data given with the key and salt
and then decodes it using the password given
'''

class Encrypt:
    _backend: default_backend = default_backend()
    _iterations: int = 100_000

    def __init__(self, master_password:str) -> None:
        self._password: bytes = master_password.encode()        
        self._salt = secrets.token_bytes(16)
        self._key = self._derive_key(self._salt)


    def _derive_key(self, salt: bytes) -> bytes:
        '''
        Generate a key from a given password and salt
        '''
        # Create the object that will derive the key
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt,iterations=self._iterations, backend=self._backend)
        # Derive the key
        key = kdf.derive(self._password)
        # Encode the key
        encoded_key = b64e(key)
        # Return the encoded key
        return encoded_key

    def encrypt(self, token: bytes) -> bytes:
        return b64e(b'%b%b%b' % (self._salt, self._iterations.to_bytes(4, 'big'), b64d(Fernet(self._key).encrypt(token))))

    def decrypt(self, token: bytes) -> str:
        # Decode the encrypted message
        decoded = b64d(token)
        
        # Extract the salt, iterations, and encrypted message
        salt, iter, encrypted_message = decoded[:16], decoded[16:20], b64e(decoded[20:])
        iterations = int.from_bytes(iter, 'big')
        
        # Derive the key
        key = self._derive_key(salt)
        
        # Decrypt the message using the key
        try:
            Buffer =  Fernet(key).decrypt(encrypted_message)
            return Buffer
        except InvalidToken:
            return "Invalid Password"
    