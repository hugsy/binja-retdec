import string

def read_cstring(view, addr):
    """Read a C string from address."""
    s = ""
    while True:
        c = view.read(addr, 1)
        if c not in string.printable:
            break
        if c == "\n": c = "\\n"
        if c == "\t": c = "\\t"
        if c == "\v": c = "\\v"
        if c == "\f": c = "\\f"
        s+= c
        addr += 1
    return s
