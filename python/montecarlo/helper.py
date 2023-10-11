#!/usr/bin/env python3


def input_str(message, default_value):
    ret_str = input(message + ", [" + default_value + "]: ")
    ret_str = default_value if len(ret_str) == 0 else ret_str
    return ret_str


def input_int(message, default_value):
    ret_int = input(message + ", [" + str(default_value) + "]: ")
    ret_int = default_value if len( str(ret_int) ) == 0 else ret_int
    return int(ret_int)


def input_float(message, default_value):
    ret_float = input(message + ", [" + str(default_value) + "]: ")
    ret_float = default_value if len( str(ret_float) ) == 0 else ret_float
    return float(ret_float)
