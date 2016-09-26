import os
try:
    import mechanize
except:
    print "Necesitas tener instalado mechanize, deasea instalarlo ahora y/n"
    option = raw_input("-> ")
    if option == 'y':
        os.system("sudo apt-get install python-mechanize")
    else:
        print "Es necesario tener todas las librerias instaladas para continuar"
        exit()

def logo():
    os.system("clear")
    print """
 _    _      _      ______            _        ___  ___          _       _
| |  | |    | |     | ___ \          | |       |  \/  |         | |     | |
| |  | | ___| |__   | |_/ /_ __ _   _| |_ ___  | .  . | ___   __| |_   _| | ___
| |/\| |/ _ \ '_ \  | ___ \ '__| | | | __/ _ \ | |\/| |/ _ \ / _` | | | | |/ _ \\
\  /\  /  __/ |_) | | |_/ / |  | |_| | ||  __/ | |  | | (_) | (_| | |_| | |  __/
 \/  \/ \___|_.__/  \____/|_|   \__,_|\__\___| \_|  |_/\___/ \__,_|\__,_|_|\___|
      """

def getIp(url):
        dirtyIp = os.popen("ping -c 1 " + url).read()
        dirtyIp = dirtyIp.split("\n")
        if dirtyIp[1] == "":
            print "[!] No se a podido localizar el host"
            raw_input()
            exit()
        dirtyIp = dirtyIp[0]
        dirtyIp = dirtyIp.split(" ")
        dirtyIp = dirtyIp[1] + " "+ dirtyIp[2]
        print (dirtyIp)
        finalIp = dirtyIp.split("(")

        return finalIp[1][:-1]

def loadObjetivo(objetivo):
    print "test"


def start():
    logo()
    print getIp(raw_input("Url/Ip del objetivo: "))
