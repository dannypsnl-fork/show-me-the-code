from arith_lex import lexer, lexer_lazy_bytes
from arith_parser import mk_parser, Tokens, Color
from termcolor import colored

def parse(code):
    tokens = list(lexer("<test>", code))
    parser = mk_parser()
    return parser(None, Tokens(tokens))

def flatten(c, result):
    if isinstance(c, Color):
        result.append(c)
    elif isinstance(c, list):
        for cn in c:
            flatten(cn, result)

got = parse("1 * 2 + 3 * 4")
flat_list = []
flatten(got, flat_list)
for c in flat_list:
    print(colored(c.value, c.color), end=' ')
