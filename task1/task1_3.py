# 3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
# результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль
# tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:
# Reachable         # Unreachable
# 10.0.0.1          # 10.0.0.3
# 10.0.0.2          # 10.0.0.4
#
from tabulate import tabulate
from task1_2 import host_range_ping


def reformat_dict(dict):
    result_dict = {'available': [], 'unavailable': []}
    for k, v in dict.items():
        if 'NOT' in v:
            result_dict['unavailable'].append(k)
        else:
            result_dict['available'].append(k)
    return result_dict


if __name__ == "__main__":
    res = reformat_dict(host_range_ping())
    print(tabulate(res, headers='keys', tablefmt="pipe"))
