from arith_lex import lexer, lexer_lazy_bytes
from arith_parser import mk_parser, Tokens, Color
from termcolor import colored

def parse(code):
    tokens = list(lexer("<test>", code))
    parser = mk_parser()
    return parser(None, Tokens(tokens))

def printC(c):
    if isinstance(c, Color):
        print(colored(c.value, c.color), end=' ')
    else:
        for cn in c:
            printC(cn)

got = parse("1 * 2 + 3 * 4")
printC(got)
