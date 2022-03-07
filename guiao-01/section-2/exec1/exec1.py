import sys
import hashlib

ficheiros = [nome for nome in sys.argv[1:]]
h = hashlib.sha1()

for ficheiro in ficheiros:
    conteudo = ''
    with open(ficheiro, 'r') as f:
        conteudo += f.read()
    h.update(conteudo.replace('\n','').encode('utf-8'))
    
print(h.hexdigest())