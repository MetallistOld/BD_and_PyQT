from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(list_ip_addresses, timeout=3, requests=1):
    results = {'Доступные узлы': "", 'Недоступные узлы': ""}  # словарь с результатами
    for address in list_ip_addresses:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        args = ["ping", "-W", str(timeout), "-c", str(requests), str(address)]
        proc = Popen(args, shell=False, stdout=PIPE)
        proc.wait()
        # проверяем код завершения подпроцесса
        if proc.returncode == 0:
            results['Доступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел доступен'
        else:
            results['Недоступные узлы'] += f"{str(address)}\n"
            res_string = f'{address} - Узел недоступен'
        print(res_string)
    return results


if __name__ == '__main__':
    ip_addresses = ['yandex.ru', '2.2.2.2', '192.168.0.100', '172.20.10.8']
    host_ping(ip_addresses)
