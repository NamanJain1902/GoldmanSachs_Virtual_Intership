import os

content = open('./passwd_dump.txt')
plain_text = open('./plain_text.txt', 'w')
hashes = open('./hashes.txt', 'w')


for line in content:
    pt, hs = line.split(':')
    plain_text.write(pt+ "\n")
    hashes.write(hs)
        