import urllib.request
try:
    pudim = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[0;31mO site do PUDIM não pode ser acessado!')
else:
    print('\033[0;32mO site do PUDIM está acessível!')
