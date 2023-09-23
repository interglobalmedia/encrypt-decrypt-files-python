from cryptography.fernet import Fernet
from get_key import load_key

# load the key
crypto_key = load_key()
# store string in variable
message = 'super secret message'
# initialize the Fernet class
f = Fernet(crypto_key)
# encrypt data
message_encrypted = f.encrypt(message.encode())
print(message_encrypted)

# decrypt data
message_decrypted = f.decrypt(message_encrypted.decode())
print(message_decrypted)