import math as m


def area(wid, len):
    return wid*len


def parameter(wid, len):
    return (2*(len+wid))


def diagonal(wid, len):
    return m.sqrt(wid**2 + len**2)
