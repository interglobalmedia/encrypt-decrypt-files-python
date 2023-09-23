from cryptography.fernet import Fernet
from get_key import load_key

def encrypt_file(filename, key):
  """
  Given a filename (str) and key (bytes), it encrypts the file and writes it
  """
  f = Fernet(key)
  # after initializing the Fernet object with the given key, let's read the target file.
  with open(filename, "rb") as file:
    # read all file data
    file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
      file.write(encrypted_data)

# load the key
key = load_key()
# file name
file = "nba.csv"
# encrypt it
encrypt_file(file, key)


