# Instructions

Download rockyou.txt wordlist using 
> https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt




Run follwoing on the command line.


* sudo apt-get update
* sudo apt install hashcat

* hashcat -a 0 -m 0 hashes.txt rockyou.txt