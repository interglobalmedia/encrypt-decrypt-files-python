# Encrypting/Decrypting Files and Strings

## Python vs Command Line (macOS)

In cybersecurity, we want to be as efficient and swift as possible when executing our tasks. In this scenario, I want to compare encrypting and decrypting files and strings in Python vs doing the same thing via the Command Line.

First of all, in my `Python` ***approach*** to `encrypting` and `decrypting` a ***file***, I wanted to make sure that I `modularized` my `task functions`. So I ***created*** the ***following*** `files`:

- create_key.py
- get_key.py
- encrypt_file.py
- decrypt_file.py

As for `encrypting` and `decrypting` a `string`, I ***created*** the ***following*** `files`:

- encrypt_string.py
- decrypt_string.py

***Now*** to ***break*** `things` ***down*** and ***explain*** `what` ***each*** `file` ***does***. I ***tried*** to ***create*** `file names` that ***describe*** the `individual tasks` they are ***responsible*** for. I call this `"task modularization"`.

The `create_key.py` file ***creates*** an `encryption key` ***using*** the `Python Fernet` ***symmetric encryption method***. It was ***created*** by `Google` and ***uses*** `128-bit AES keys`. `AES 128-bit encryption` in of ***itself*** is ***safe against*** `brute-force attacks`. ***The only*** `"wildcard"` is the ***safety*** of the `key`. I ***would say*** that ***using*** `symmetric encryption` is ***best when*** you are `encrypting` and `decrypting` ***for yourself*** and ***don't need*** to ***share*** the `key` ***with others*** for `successful completion` of the ***process***.

The `get_key.py` file's `task` is to ***load*** the `key` that has been `generated`. So ***for example***, I ***make*** the ***following*** `import statement` in the `decrypt_file.py`, `decrypt_string.py`, `encrypt_file.py`, `encrypt_string.py`:

```python
from get_key import load_key
```

***And*** I ***also make*** the ***following*** `import statement` for `Python Fernet` ***in all*** the `files` ***except for*** `get_key.py`:

```python
from get_key import load_key
```

All `get_key.py` ***does*** is ***load*** the `key.key` file ***which contains*** the `encryption key` ***itself***, so ***importing*** `Fernet`, or ***anything else*** for ***that matter***, is ***not necessary***.

The ***difference between*** the `code` for `encrypting` and `decrypting` a ***file*** was ***minimal*** and ***therefore easy*** to ***set*** up ***modularly***. It was a ***bit trickier***, ***however***, with the ***creation*** of the `message_encrypt` and `message_decrypt` functions. ***There***, I ***had*** to ***make sure*** that the `string` which is `encrypted` is the ***same string*** that is then `decrypted`.

In the `encrypt_string.py` file, I ***had*** to ***make sure*** that I ***created*** a `local variable` ***inside*** the `message_encrypt` ***function*** that I ***would*** be ***able*** to `import` ***into the*** `decrypt_string.py` file and then ***use inside*** the `message_decrypt` ***function***. So:

```python
# store string in variable
message = 'super secret message'
# inside the message_encrypt function
# encrypt data
message_encrypt.message_encrypted = f.encrypt(message.encode())
```

`message_encrypt` is the ***name*** of the ***function***, and `message_encrypted` is the `variable name`. This ***made*** it ***possible*** to ***include*** the ***following*** `import statement` ***inside*** the `decrypt_string.py` file:

```python
from encrypt_string import message_encrypt
```

***And this*** then ***made it*** possible ***to add*** the ***following*** inside the `message_decrypt` function ***thereby linking*** the `encrypted message` ***created*** in `encrypt_string.py` to the `encrypted message` ***imported from*** the `encrypt_string.py` file into `decrypt_string.py`, which ***resulted in*** the ***successful***  `decryption` ***of the*** `encrypted message` (`string`):

```python
from encrypt_string import message_encrypt
# inside the message_decrypt function
message_encrypt.message_encrypted = f.decrypt(message_encrypt.message_encrypted.decode())
```

The above ***prevents*** the ***following*** `error` ***from*** `taking place` in `Terminal` ***when running*** the ***string related*** files ***containing*** the `modularized functions`:

```python
File "/Users/mariacam/Development/cyber-projects/encrypt-decrypt-files-python/venv/lib/python3.11/site-packages/cryptography/fernet.py", line 86, in decrypt
    timestamp, data = Fernet._get_unverified_token_data(token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mariacam/Development/cyber-projects/encrypt-decrypt-files-python/venv/lib/python3.11/site-packages/cryptography/fernet.py", line 119, in _get_unverified_token_data
    raise InvalidToken
```

***Lastly***, it is ***important*** to ***note that*** in the `message_decrypt` ***function***, the `message` ***represented by*** `message_encrypt.message_encrypted` ***passed*** to the `f.decrypt()` method, is ***chained*** to the `decode()` method ***instead of*** the `encode()` method. ***Not only*** are we `decrypting` our `message`, but we ***also have*** to `decode` it, ***since*** it was `encoded` when `encrypted`. ***Now*** the `message` is just `"plain text"` as it was ***originally*** when ***first created***.

## Using GnuPG to encrypt and decrypt strings and files via the Command Line

This was ***a lot*** of ***work***, right? A `programmatic approach` ***will always*** be ***more complex*** than `executing` the ***same task*** via the `Command Line`. And in `Cybersecurity`, we ***won't*** necessarily ***have*** the `luxury` or `even need` to `programmatically execute` ***such tasks***.

***This*** is ***where*** `tools` ***such as*** `gnupg` ***come in***. `gnupg`, ***aka*** `gpg`, which ***stands for*** [GNU Privacy Guard](https://gnupg.org/), is

>a complete and free implementation of the OpenPGP standard as defined by RFC4880 (also known as PGP). GnuPG allows you to encrypt and sign your data and communications; it features a versatile key management system, along with access modules for all kinds of public key directories. GnuPG, also known as GPG, is a command line tool with features for easy integration with other applications. A wealth of frontend applications and libraries are available. GnuPG also provides support for S/MIME and Secure Shell (ssh).

GNUPG's "claim to fame" is that

> GnuPG is one of the tools that Snowden used to uncover the secrets of the NSA.

## Encrypting a file with GnuPG

***Next***, I ***installed*** `gpg` ***using*** [Homebrew](https://formulae.brew.sh/formula/gnupg) so I could ***use it*** to `encrypt` and `decrypt` a `file`. If you ***have*** `Homebrew` ***already installed*** on your `macOS`, but ***don't have*** `gnupg` ***installed***, ***run*** the ***following command*** in `Terminal`:

```shell
brew install gnupg
```

If you ***think that*** you ***might have*** it ***installed***, ***run*** the ***following command*** in `Terminal`:

```shell
gpg --version
```

If you ***get back*** something like the ***following***:

```shell
gpg (GnuPG) 2.4.3
```

Then you ***do have*** it ***installed***. ***But*** if you ***get back***:

```shell
zsh: command not found: gpg
```

You ***do not*** have it ***installed***.

If you are on `Linux`, you ***would*** `use` the ***following command*** to ***install*** `gpg` ***using*** the `package manager` ***of your*** `Linux distribution`:

```shell
sudo apt install gnupg
```

***After*** `gnupg` was ***installed***, I ***ran*** the ***following command*** in `Terminal`:

```shell
echo Hello Maria! > greetings.txt
```

**Note**: ***On*** `macOS`, ***when*** we ***run*** the `echo` command, we ***should not*** `use quotes` ***around*** the `string` of `words`. It ***throws*** an `error`.

***Then*** I ***ran*** the `gpg` command to `encrypt` my ***new*** `greetings.txt` file, and I ***included*** the ***use*** of a `passphrase`. I even ***use them*** when ***communicating*** with `Github`, ***even though*** I am ***connected*** via `SSH`. ***So***:

```shell
gpg --batch --output greetings.txt.gpg --passphrase mypassword --symmetric greetings.txt
```

`mypassword` should be ***replaced with*** your ***actual*** `passphrase` value. This command ***creates*** the `encrypted` file `greetings.txt.gpg` in the ***same location*** as `greetings.txt` using its ***default*** `AES256 algorithm`. [As for the --batch option, with GPG2](https://superuser.com/questions/972204/how-to-use-gnupg-with-passphrase), ***which is*** what `GPG 2.4.3` is (`Homebrew` ***links*** `GPG` to `GPG2`), you ***have*** to ***use*** it ***with*** the --passphrase option.

***After*** I ***executed*** this command, the ***following*** was ***returned*** in `Terminal`:

```shell
gpg: WARNING: unsafe permissions on homedir '/Users/mariacam/.gnupg'
```

***First***, to ***make sure*** that the `.gnupg` directory and its `contents` is ***accessible*** to me, I ***run*** the ***following command***:

```shell
chown -R $(whoami) ~/.gnupg
```

The `chown` command ***changes*** the `file ownership` of a ***specific*** `file` or `folder`. ***Here***, it ***pertains to*** the `.gnupg` folder in my `home directory`. `whoami` ***refers to*** the `current user`, ***which*** in ***my case***, is `me`, and ***refers to*** the `current user`'s `username` on the `system`. `-R` ***indicates*** that `ownership` of a `folder` is ***being changed***. In ***my case***, this is ***simply*** a `confirmation` of `ownership`, ***since*** I am the ***only user*** on ***my computer***.

***But*** this was ***not enough***. I l***ike*** to ***make sure***, ***even though*** there are ***no other*** `users` at ***this time*** on ***my computer***, that ***only*** I ***have access*** to the `.gnupg` folder. ***So first*** I ***ran*** the ***following command***:

```shell
chmod 700 ~/.gnupg
```

`chmod` is used to ***change*** the `permissions` of `files` and `directories`. The ***above changes*** the `permissions` on the `.gnupg` folder to `700`. And `700` ***means*** that ***only*** the `creator` and `owner` of the `folder` ***can*** `Read`, `Write`, and `Execute` on the directory. And `group` and `others` ***cannot perform*** any operation on the `files` in the `directory`.

***Then*** I ***ran*** the ***following***:

```shell
chmod 600 ~/.gnupg/*
```

***Here***, the `permissions` for the `files` ***inside*** the `.gnupg` folder are ***set to*** `600`. This ***means*** the `owner` has `Read` and `Write` permissions on the `files` ***but not*** `execution` permissions.

***Lastly***, I ***ran*** the ***following***:

```shell
chmod 700 ~/.gnupg/*.d
```

***This is*** an `extra` and `special command` ***which is*** what ***made*** it ***possible*** for me to ***change*** the `permissions` on the `.gnupg` folder and `contents` to the ***proper settings***. ***Inside*** the `folder`, ***there is*** a `directory` which ***by default*** does ***not have*** `execution permissions` when one ***tries*** to `send keys` ***without*** a `keyserver` specified:

```shell
drw-------  2 rik rik  4096 Jun  9 03:28 crls.d    <---- Notice this here
```

So `*.d` ***ensures that*** all `.d` directories ***inside*** have `execution permissions`. ***To view*** the `source` ***where*** I ***got*** this `information` ***from*** on `Github`, ***please visit*** [This fixes the " gpg: WARNING: unsafe permissions on homedir '/home/path/to/user/.gnupg' " error while using Gnupg.](https://gist.github.com/oseme-techguy/bae2e309c084d93b75a9b25f49718f85), and scroll down to kirvedx's comment from Jun 13, 2022.

## Decrypting files with GnuPG

***Next***, I ***ran*** the ***following command*** to `decrypt` the `greetings.txt.gpg` file I ***just*** had ***encrypted***:

```shell
gpg --batch --output greetings1.txt --passphrase mypassword --decrypt greetings.txt.gpg
```

***And*** the ***following*** was ***returned*** in `Terminal`:

```shell
gpg: AES256 encrypted data
gpg: encrypted with 1 passphrase
```

***Then***, to ***clear*** the `passphrase` which was ***stored*** in the ***session***, I ***ran*** the ***following command***:

```shell
echo RELOADAGENT | gpg-connect-agent
```

***Next***, I ***wanted*** to ***verify*** that my `decrypted` file `matched` my ***original*** `greetings.txt` file, so I ***ran*** the ***following command***:

```shell
diff -s greetings.txt greetings1.txt
```

***And*** the ***following*** was ***returned*** in `Terminal`:

```shell
Files greetings.txt and greetings1.txt are identical
```

Success!

**Note**: the `-s` option is short for `--sign`, which stands for "sign a message". So basically, I am checking to make sure that the integrity of the file when decrypted was intact.

### Related Resources

- [Encrypting and Decrypting Files in Linux](https://www.baeldung.com/linux/encrypt-decrypt-files)

- [How to Encrypt and Decrypt Files in Python](https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python)