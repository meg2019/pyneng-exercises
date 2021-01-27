#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ip, mask = argv[1].split ('/')
octets = ip.split ('.')
mask = int (mask)
maskBin = "1" * mask + "0" * (32 - mask)
maskOctets = (
    int(maskBin[0:8], 2),
    int(maskBin[8:16], 2),
    int(maskBin[16:24], 2),
    int(maskBin[24:32], 2),
)

IPBinary = "{:08b}{:08b}{:08b}{:08b}".format(int(octets[0]), int(octets[1]), int(octets[2]), int(octets[3]))
NetBin = IPBinary[:mask] + "0" * (32 - mask)
NETOctets = (
    int(NetBin[0:8], 2),
    int(NetBin[8:16], 2),
    int(NetBin[16:24], 2),
    int(NetBin[24:32], 2),
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

print (ip_template.format (int(NETOctets[0]), int(NETOctets[1]), int(NETOctets[2]), int(NETOctets[3])))
print (mask_template.format (mask, maskOctets[0], maskOctets[1], maskOctets[2], maskOctets[3]))