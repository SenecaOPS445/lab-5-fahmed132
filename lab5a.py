#!/usr/bin/env python3
# Author ID: Fahmed132

def read_file_string(file_name):
    f = open(file_name, 'r')
    contents = f.read()
    f.close()
    return contents 

def read_file_list(file_name):
    f = open(file_name, 'r')
    contents = [line.strip() for line in f.readlines()]
    f.close()
    return contents

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))