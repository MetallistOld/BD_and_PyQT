"""Программа-лаунчер"""
import random
import subprocess
import time

PROCESSES = []


def get_name(i):
    return f'{random.getrandbits(128)}/{i}'


while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, '
                   'x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        clients_count = int(input('Введите количество тестовых клиентов для запуска: '))
        PROCESSES.append(subprocess.Popen('python server.py', creationflags=subprocess.CREATE_NEW_CONSOLE))

        time.sleep(0.5)
        for i in range(clients_count):
            # Добавил так имя так как имена 1-2-3 бывают заняты
            # name = get_name(i)
            PROCESSES.append(subprocess.Popen(f'python client.py -n test{i + 1}', creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif ACTION == 'x':
        while PROCESSES:
            VICTIM = PROCESSES.pop()
            VICTIM.kill()
