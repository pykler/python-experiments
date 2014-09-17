def noop(*args):
    pass

def test1(style, count):
    x = range(count)
    if style == 'map':
        def test():
            map(noop, x)
    if style == 'list_comp':
        def test():
            [noop(a) for a in x]
    elif style == 'loop':
        def test():
            for a in x:
                noop(a)
    return test


def test2(style, count):
    x = range(count)
    if style == 'map':
        def test():
            map(lambda a: map(lambda b: noop(a,b), x), x)
    if style == 'list_comp':
        def test():
            [noop(a, b) for a in x for b in x]
    elif style == 'loop':
        def test():
            for a in x:
                for b in x:
                    noop(a, b)
    return test

def test3(style, count):
    x = range(count)
    if style == 'map':
        def test():
            map(lambda a: map(lambda b: map(lambda c: noop(a,b,c), x), x), x)
    if style == 'list_comp':
        def test():
            [noop(a, b, c) for a in x for b in x for c in x]
    elif style == 'loop':
        def test():
            for a in x:
                for b in x:
                    for c in x:
                        noop(a, b, c)
    return test

def test4(style, count):
    x = range(count)
    if style == 'map':
        def test():
            return map(noop, x)
    if style == 'list_comp':
        def test():
            return [noop(a) for a in x]
    elif style == 'loop':
        def test():
            r = []
            for a in x:
                r.append(noop(a))
            return r
    return test

def test5(style, count):
    x = range(count)
    if style == 'map':
        def test():
            return map(lambda a: map(lambda b: noop(a,b), x), x)
    if style == 'list_comp':
        def test():
            return [noop(a, b) for a in x for b in x]
    elif style == 'loop':
        def test():
            r = []
            for a in x:
                for b in x:
                    r.append(noop(a, b))
            return r
    return test

def test6(style, count):
    x = range(count)
    if style == 'map':
        def test():
            return map(lambda a: map(lambda b: map(lambda c: noop(a,b,c), x), x), x)
    if style == 'list_comp':
        def test():
            return [noop(a, b, c) for a in x for b in x for c in x]
    elif style == 'loop':
        def test():
            r = []
            for a in x:
                for b in x:
                    for c in x:
                        r.append(noop(a, b, c))
            return r
    return test
