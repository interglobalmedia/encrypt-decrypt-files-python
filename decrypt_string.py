from cryptography.fernet import Fernet
from get_key import load_key
from encrypt_string import message_encrypt

def message_decrypt():
  # load the key
  crypto_key = load_key()
  # initialize the Fernet class
  f = Fernet(crypto_key)
  # encrypt data
  message_encrypt.message_encrypted = f.decrypt(message_encrypt.message_encrypted.decode())
  print(message_encrypt.message_encrypted)

# decrypt data
message_decrypt()