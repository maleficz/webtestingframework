import os
from bruteModules import webBrute
from bruteModules import sshBrute
from bruteModules import md5Hash

def logo():
    os.system("clear")
    print """
	    Coder: Hanom1960 Email/XMPP: hanom1960@cock.lu
		Twitter: @hanomlulzsec
        """
def typeAtackSelection():
    logo()
    print """
        Escoja tipo de ataque:
        1) Ataque WEB
        2) Ataque SSH
        3) MD5 Hash
        """
    tipoAtaque = raw_input("Tipo de ataque: ")
    if tipoAtaque == '1':
        webBrute.start()
    elif tipoAtaque == '2':
        sshBrute.test()
    elif tipoAtaque == '3':
        md5Hash.start()
    else:
        print "Wrong option"
        typeAtackSelection()

typeAtackSelection()
