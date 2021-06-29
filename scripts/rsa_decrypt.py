#!/usr/bin/env python3

# created by e-seng on github
import sys

class Encrypt_Data_Holder:
    def __init__(self):
        self.p = -1
        self.q = -1
        self.n = -1
        self.e = -1
        self.d = -1
        self.encrypted_path = ""

def main():
    # usage ./mp_decrypt.py -n <int> -d <int> -cf <path to encrypted file>
    
    if len(sys.argv) == 1:
        display_help()
        return

    data = Encrypt_Data_Holder()

    # setting flags
    for index in range(1, len(sys.argv)):
        if(sys.argv[index] == "-h"):
            display_help()
            return
        if(sys.argv[index] == "-n"):
            data.n = int(sys.argv[index+1])
        if(sys.argv[index] == "-d"):
            data.d = int(sys.argv[index+1])
        if(sys.argv[index] == "-cf"):
            data.encrypted_path = sys.argv[index+1]


    if data.encrypted_path == "":
        display_help()
        return

    m = ""
    with open(data.encrypted_path, "r") as file:
        c = file.read().split()
        for char in c:
            m += chr(int(char) ** data.d % data.n)

    print(m)

def display_help():
    print("Usage: ./mp_decrypt.py [OPTIONS] -cf <path to encrypted file>")
    print("OPTIONS:")
    print("\tdecryption")
    print("\t----------")
    print("\t-n <int>       The known product of two primes, typically the second value")
    print("\t               in both the private and public key pairs, this is required")
    print("\t-d <int>       The unique private key value, typcally the first value in")
    print("\t               the private key pair, this is required")
    print("\t-cf <filepath> The filepath to the encrypted message, this is required")

if __name__ == "__main__": main()

"""
p = 61527 # some prime number to generate rsa key
q = 23 # some other prime number, different to p, to generate the rsa key

# set known private key, public key pair values
# note:
# public key pair: (e, n)
# private key pair: (d, n)
e = 0
d = 61527
n = 37627

# more detailed information:
# n is the product of two prime numbers p, q.
# n = p * q
#
# e is some number that is coprime to phi = (p-1) * (q-1) where
# 1 < e < phi
#
# once e is obtained, which is used for the public key pair, the
# private key pair can be generated with
# d = (1 % phi) / e.

# test character
c = 2367
known_char = '-'
m = ord('-')

print(c ** d % n == m, m, (c ** d % n))

with open("./encrypted_text.txt", "r") as file:
    c = file.read().split()
    m = ''
    for char in c:
        m += chr(int(char) ** d % n)

    print(m)
"""
