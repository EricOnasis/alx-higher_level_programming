#!/usr/bin/python3
def magic_string(static={"counter": 0}):
    static["counter"] += 1
    return str("BestSchool, " * static["counter"])[:-2]
