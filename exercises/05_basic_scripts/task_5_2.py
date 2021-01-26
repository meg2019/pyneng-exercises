# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
address = input ('Введите ip адрес в формате XXX.XXX.XXX.XXX/XX ')
ip, mask = address.split ('/')
octets = ip.split ('.')
mask = int (mask)
maskBin = "1" * mask + "0" * (32 - mask)
maskOctets = (
    int(maskBin[0:8], 2),
    int(maskBin[8:16], 2),
    int(maskBin[16:24], 2),
    int(maskBin[24:32], 2),
)
ip_template = '''
    Network:
    {0:<8} {1:<8} {2:<8} {3:<8}
    {0:08b} {1:08b} {2:08b} {3:08b}
    '''
mask_template = '''
    Mask:
    /{0}
    {1:<8} {2:<8} {3:<8} {4:<8}
    {1:08b} {2:08b} {3:08b} {4:08b}
    '''

print (ip_template.format (int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3])))
print (mask_template.format (mask, maskOctets[0], maskOctets[1], maskOctets[2], maskOctets[3]))