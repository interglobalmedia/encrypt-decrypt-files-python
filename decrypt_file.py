from cryptography.fernet import Fernet
from get_key import load_key

def decrypt_file(filename, key):
  """
  Given a filename (str) and key (bytes), it decrypts the file and writes it.
  """
  f = Fernet(key)
  with open(filename, "rb") as file:
    # read the encrypted data
    encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the encrypted file
    with open(filename, "wb") as file:
      file.write(decrypted_data)

# load the key
decrypt_key = load_key()
# file name
decrypted_file = "nba.csv"
# dencrypt it
decrypt_file(decrypted_file, decrypt_key)