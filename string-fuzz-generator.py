#!/usr/bin/python
import random
from socket import *


def add_random_split(str_input):
    i = random.choice([0, 1, 2, 3])
    if i == 0:
        str_input += ':'
    if i == 1:
        str_input += ';'
    if i == 2:
        str_input += ','
    if i == 3:
        str_input += '.'
    return str_input


def append_random_number(str_input):
    i = random.choice([0, 1])
    random_num_str = random.randint(-4294967296, 4294967296)
    defined_chosen_num_str = ['0.5', '12345678910111213.123', '-0.5', '-12345678910111213.123', '0', '1', '2',
                              '-1', '-2', '255', '256', '257', '-255', '-256', '-257', '65535', '65536',
                              '-65535', '-65536', '4294967295', '4294967296', '-4294967295', '-4294967296']

    if i == 1:
        str_input += str(random_num_str)
    else:
        str_input += random.choice(defined_chosen_num_str)
    str_input = add_random_split(str_input)
    return str_input


def append_non_visible_char(str_input):
    i = random.randint(0, 7)
    str_input += ':'
    defined_non_visible_char = ['/x00', '/x01', '/x02', '/x03', '/x04', '/x05', '/x06', '/x07', '/x07', '/x08',
                                '/x09', '/x0a', '/x0b', '/x0c', '/x0d',
                                '/x0e', '/x0f', '/x10', '/x11', '/x12', '/x13', '/x14', '/x15', '/x16', '/x17',
                                '/x17', '/x18', '/x19', '/x1a', '/x1b', '/x1c', '/x1d',
                                '/x1e', '/x1f', '/x7f']
    while i:
        str_input += random.choice(defined_non_visible_char)
        i = i - 1
    str_input = add_random_split(str_input)
    return str_input


def append_split_char(str_input):
    mode = random.choice([0, 1, 2, 3, 4, 5])
    i = random.randint(0, 7)
    defined_split_char = ['`', '~', '!', '@', '#', '#', '$', '%', '%', '^',
                          '&', '*', '(', ')', '_',
                          '-', '=', '+', '{', '}', '[', ']', '\\', ':', ';',
                          '\'', '"', ',', '<', '.', '>', '?',
                          '/']
    if mode == 1:
        str_input += random.choice(defined_split_char)*i
    else:
        while i:
            str_input += random.choice(defined_split_char)
            i = i - 1
    str_input = add_random_split(str_input)
    return str_input


def append_format_string_char(str_input):
    mode = random.choice([0, 1, 2, 3, 4, 5])
    i = random.randint(0, 7)
    defined_format_string_char = ['%s', '%r', '%c', '%b', '%d', '%i', '%o', '%x', '%e', '%E',
                                  '%f', '%g', '%G', '%%', '%p']
    if mode == 1:
        str_input += random.choice(defined_format_string_char) * i
    else:
        while i:
            str_input += random.choice(defined_format_string_char)
            i = i - 1
    str_input = add_random_split(str_input)
    return str_input


def append_char(str_input):
    mode = random.choice([0, 1, 2, 3, 4, 5])
    i = random.randint(0, 7)
    defined_normal_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                           'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if mode == 1:
        str_input += random.choice(defined_normal_char) * i
    else:
        while i:
            str_input += random.choice(defined_normal_char)
            i = i - 1

    str_input = add_random_split(str_input)
    return str_input


def generate_random_char(str_input):
    n = random.randint(0, 10000)
    while n:
        append_mode = random.choice([0, 1, 2, 3, 4])
        if append_mode == 0:
            str_input = append_random_number(str_input)
        if append_mode == 1:
            str_input = append_non_visible_char(str_input)
        if append_mode == 2:
            str_input = append_split_char(str_input)
        if append_mode == 3:
            str_input = append_format_string_char(str_input)
        if append_mode == 4:
            str_input = append_char(str_input)
        n = n - 1
    return str_input


def generate_fuzz_char():
    mode = random.choice([0, 1])
    if mode == 0:
        print('normal mode')
        fuzz_str = ''
        fuzz_str = generate_random_char(fuzz_str)
        print(fuzz_str)
    if mode == 1:
        print('json mode')
        fuzz_str = '{'
        fuzz_str = generate_random_char(fuzz_str)
        fuzz_str += '}'
        print(fuzz_str)
    return fuzz_str

generate_fuzz_char()

# fuzz_string = generate_fuzz_char()
# ADDR = ('192.168.2.2', '60001')
# tcpCliSock = socket(AF_INET, SOCK_STREAM)
# tcpCliSock.connect(ADDR)
# while 1:
#     tcpCliSock.send(fuzz_string)
#     print('send:\n')
#     print(fuzz_string)

# if mode == 2:
#     print('xml mode')
#     list(fuzz_str).insert(1, '<')
#     k = random.randint(20, 50)
#     index = random.randint(2, len(fuzz_str) - 1)
#     while k:
#         list(fuzz_str).insert(index, '<')
#         list(fuzz_str).insert(index, '>')
#         k = k - 1
#     list(fuzz_str).append('>')
#     fuzz_str = fuzz_str.join(fuzz_str)
#     print(fuzz_str)
