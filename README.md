# How it begins🧐?

Read the following blog post. This will give you idea how rockyou password breach incident lead to series of incidents that made life of hackers easy to guess the password even if it's masked with cryptographic algorithm such as MD5.
https://arstechnica.com/information-technology/2013/05/how-crackers-make-minced-meat-out-of-your-passwords/


# Task
#### Try to crack the passwords provided in the 'password dump' file below using available tools.

# Instructions

* filter.py extracts all hashes from passwd_dump.txt and stores it in hashes.txt.
```
$ python3 filter.py
```


Download rockyou.txt wordlist using 
> https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt



Run follwoing on the command line.

```
$ sudo apt-get update
```
```
$ sudo apt install hashcat
```
```
$ hashcat -a 0 -m 0 hashes.txt rockyou.txt
```

If you don't want to download hashcat use https://crackstation.net/. Crackstation has their own wordlist, wheneven you enter passphrase it matches with a list deciphered passphrases and returns corresponding password from db.
