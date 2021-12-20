import re

pattern = [
    r'(\d+[.]\d+[.]\d+[.]\d+)[ ]',
    r'\[(.+)\]', r'"(\w+)[ ][\/]',
    r'[ ]([\/].+)[ ]HTTP',
    r'"[ ](\d{3})',
    r' (\d) "-'
]


def search_t(sequence):
    pars = []
    for x in pattern:
        lin = re.search(x, sequence)
        pars.append(lin.group(1) if lin is not None else None)
    return print(tuple(pars))


with open('nginx_logs', 'r') as f:
    for line in f:
        search_t(line)
