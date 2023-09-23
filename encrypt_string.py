from cryptography.fernet import Fernet
from get_key import load_key

def message_encrypt():
  # load the key
  crypto_key = load_key()
  # store string in variable
  message = 'super secret message'
  # initialize the Fernet class
  f = Fernet(crypto_key)
  # encrypt data
  message_encrypt.message_encrypted = f.encrypt(message.encode())
  print(message_encrypt.message_encrypted)

# encrypt data
message_encrypt()