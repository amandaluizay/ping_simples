# importa módulo de recursos do s.o
import os
import time


def ping_simples():
    # cria uma variavel que vai receber o ip
    host = input("Digite o IP ou Host a ser verificado: ")
    # executa o ping do ip
    os.system('ping -n 6 {}'.format(host))


def ping_multiplo():
    with open('hosts.txt') as file:
        dump = file.read()
        dump = dump.splitlines()
        for ip in dump:
            print("Verificando o ip: ", ip)
            os.system('ping -n 2' + ip)
            print('-' * 60)
            time.sleep(3)
