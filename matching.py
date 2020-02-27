#!/usr/bin/env python3

pots = [line.rstrip("\n") for line in open("hashcat.potfile", "r")]
users = [line.rstrip("\n") for line in open("shadow", "r")]

output = open("cracked.txt", "w")

for user in users:
    for cracked in pots:
        if user.split(":")[1] == cracked.split(":")[0]:
            pair = user.split(":")[0] + ":" + cracked.split(":")[1] + "\n"
            output.write(pair)
