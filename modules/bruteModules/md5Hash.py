from __future__ import print_function
import os, sys


def logo():
    os.system("clear")
    print ("MD5 Hash Cracker")


def start():
    logo()
    hashList = raw_input("Ruta al archivo con la lista de hashes (/home/usuario/Documentos/hashes): ")
    try:
        hashLoader = open(hashList, 'r')
        for i in hashLoader.readlines():
            print (hashCrack(i), end='')
            print ("\n",end='')
    except:
        print ("[!]Archivo no encontrado")
        raw_input()
        start()

def hashCrack(hash):
    print ("[!]Cracking hash: "+hash, end='')
    return hash
