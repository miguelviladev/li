import sys
import hashlib

ficheiros = sys.argv[1:]
h = hashlib.sha1()

for ficheiro in ficheiros:
    with open(ficheiro, 'rb') as f:
        buffer = f.read(512)
        while len(buffer) > 0:
            h.update(buffer)
            buffer = f.read(512)
    print(ficheiro, h.hexdigest())
