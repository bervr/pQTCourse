# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или
# ip-адресом. В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего
# сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью
# функции ip_address()
from subprocess import Popen, PIPE
from ipaddress import ip_address
import platform
import socket

import chardet


def get_params():
    param = "-n" if platform.system().lower() == 'windows' else "-c"
    return param


def get_ip(str_ip):
    '''пусть будет так, потому что условие не понятное  - список из ip или hostnames, а преобразовывать надо с помощью
     ipaddress и с полным пониманием того что эта функция тут не нужна, особенно с учетом что пинг хочет на вход
     строку, а не обьект ipv4: '''
    try:
        host_ip = ip_address(str_ip)  # пробуем  получить ip из входных данных
    except Exception:
        try:  # если не удается значит это не ip, пробуем разрешить hostname
            host_ip = ip_address(socket.gethostbyname(str_ip))
        except socket.error:
            host_ip = str_ip  # если не удается, то возвращаем как есть строкой, пусть пинг разбирается
    return host_ip


def ping_one(params, ip_addr):
    args = ['ping', params, '1', str(ip_addr)]
    reply = Popen(args, stdout=PIPE, stderr=PIPE)
    code = reply.wait()
    if code == 0:
        return True
    else:
        return False
    # process = Popen(f'python ping.py {ip_addr}', shell=True, stdout=PIPE, stderr=PIPE)
    #
    # result = process.communicate()
    # print(process)
    #
    # if process.returncode == 0:
    #     print('result:', result[0])
    #     return True
    # else:
    #     print('result:', result[0])
    #     return False
    # что-то не ускорилось...


def host_ping(host_list):
    params = get_params()
    for host in host_list:
        ip_addr = get_ip(host)
        print(f'Address {host} is available') if ping_one(params, ip_addr) else print(
            f'Address {host} is NOT available')


if __name__ == "__main__":
    test_list = ['8.8.8.8', 'gb.ru', 'haha']
    host_ping(test_list)
