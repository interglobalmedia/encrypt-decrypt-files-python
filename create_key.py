from cryptography.fernet import Fernet

def write_key():
  """
  Generates a key and saves it into a file
  """
  # generate and write a new key
  key = Fernet.generate_key();
  with open('key.key', 'wb') as key_file:
    key_file.write(key)

# generate new key
write_key()