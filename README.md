Source
======
https://haveibeenpwned.com/

Description
===========
It takes your password, performs a sha1 hash, sends to the haveibeenpwned api the first 5 characters of the hash.

The API then returns all possible combinations of hashes with them, and if you find you hash with many occurences, then its time to change your password.

```
Password - nopassword
sha1 of Password1 -  D186E8DAC48A24D0115B568D0AB2C9E8B82E6ADB
'D186E' is sent to API for a response
....
D186E8ABC797A976615B568D0AB2C9E8B82E6ADB:21
D186E8DAC48A24D0115B568D0AB2C9E8B82E6ADB:21421
....
Verify your hash if present with greatest occurances in response.

```

Run
---
python pwned.py your_password
```
python pwned.py nopassword
Entire hash of nopassword is D186E8DAC48A24D0115B568D0AB2C9E8B82E6ADB
passing D186E to the API
Your password was found as D186E8DAC48A24D0115B568D0AB2C9E8B82E6ADB in 21421 occurances
```