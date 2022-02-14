import os
import glob
import hashlib

def hash_malicious_files():
    digests = open("digests.txt", "w")
    for file in glob.glob("*.py"):
        f = open("./" + file, "r")
        m = hashlib.sha1(f.read().encode()).hexdigest()
        digests.write(m + "\n")
    digests.close()
    
def main():
    hash_malicious_files()
    f = open("./digests.txt", 'r')
    print(f.read())

if __name__ == "__main__":
    main()
