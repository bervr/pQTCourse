# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или
# ip-адресом. В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего
# сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью
# функции ip_address()
from subprocess import Popen, PIPE
from ipaddress import ip_address
import platform


def get_params():
    param = "-n" if platform.system().lower() == 'windows' else "-c"
    return param


def get_ip(str):
    # пусть будет так, потому что условие не понятное  -
    # список из ip или hostnames, а преобразовывать надо с помощью ipaddress
    # с полным пониманием того что эта функция не нужна:
    try:
        host_ip = ip_address(str)[0]
    except Exception as err:
        # print(f'Exception {err}')
        host_ip = str
    return host_ip


def ping_one(host):
    args = ['ping', get_params(), '2', get_ip(host)]
    reply = Popen(args, stdout=PIPE, stderr=PIPE)
    code = reply.wait()
    if code == 0:
        return True, print(f'Address {host} is available')
    else:
        return False, print(f'Address {host} is NOT available')


def host_ping(host_list):
    for host in host_list:
        ping_one(host)


if __name__ == "__main__":
    test_list = ['8.8.8.8', 'gb.ru', 'haha']
    host_ping(test_list)
