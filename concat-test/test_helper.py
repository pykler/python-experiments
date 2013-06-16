def test_creator(style, count):
    a = ['a%s' % i for i in range(count)]
    s = ['lambda %s: ' % ','.join(a)]
    if style == 'plus':
        s.append('+'.join(a))
    elif style == 'join':
        s.append("''.join([%s])" % ','.join(a))
    elif style == 'format':
        s.append('"%s" %% (%s)' %('%s' * count, ','.join(a)))
    return eval(''.join(s))
