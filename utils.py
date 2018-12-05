def print_control_chars():
    from lxml.builder import E

    # 0-31, 127 为控制字符
    control_chars = [i for i in range(32)] + [127]

    for i in control_chars:
        try:
            E.p(chr(i))
        except ValueError:
            fmt = '{:<3} {}'
            print(fmt.format(i, repr(chr(i))))
