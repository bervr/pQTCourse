# 2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
# Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.

from ipaddress import ip_address
import platform
from task1_1 import get_ip, get_params, ping_one


def ask_user():
    while True:
        start_ip_str = input('Введите начальный IP: ')
        start_ip = get_ip(start_ip_str)  # тут бы конечно todo обработку невалидной строки...
        ip_count = abs(int(float(input('Введите количество адресов для проверки: '))))
        if check_net(start_ip, ip_count):
            return start_ip, ip_count
        else:
            print('Максимально ожидаемое количество адресов в сети - 255 ')


def check_net(start_ip, ip_count):
    last_octet = int(start_ip.exploded.split('.')[-1])
    if last_octet + ip_count > 255:
        return False
    return True


def host_range_ping():
    result_dict ={}
    params = get_params()
    start_ip, ip_count = ask_user()
    for one_ip in range(ip_count):
        host = start_ip+one_ip
        result_dict[str(host)] = f'Address {host} is available' if ping_one(params, host) else f'Address {host} is NOT available'
    return result_dict


if __name__ == "__main__":
    for key, value in host_range_ping().items():
        print(value)
