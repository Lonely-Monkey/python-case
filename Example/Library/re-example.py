import re
from typing import NamedTuple


def displaymatch(match: re.Match):
    if match:
        print('<match: %r, group=%r, groups=%r>' % (match,match.group(),match.groups()))
    else:
        print(match)

#检查对子
def checkPair():
    #给定的字符串是否有效
    valid = re.compile("^[a2-9tjqk]{5}$")
    displaymatch(valid.match("akt5q"))
    displaymatch(valid.match("akt5h"))
    displaymatch(valid.match("aktq"))
    displaymatch(valid.match("727ak"))
    #匹配对子
    pair = re.compile(r".*(.).*\1")
    displaymatch(pair.match("m7hb17a8k8i"))
    displaymatch(pair.match("718ak"))
    displaymatch(pair.match("354aa"))


#词法分析器
class Token(NamedTuple):
    type: str
    value: str
    line: int
    column: int

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_sepe = [
        ('NUMBER', r'\d+(\.\d*)?'),
        ('ASSIGN', r':='),
        ('END', r';'),
        ('ID', r'[A-Za-z]+'),
        ('OP', r'[+\-*/]'),
        ('NEWLINE', r'\n'),
        ('SKIP', r'[ \t]+'),
        ('MISMATCH', r'.'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_sepe)
    print(tok_regex)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        # print(mo)
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)


if __name__ == '__main__':
    #检查对子
    # checkPair()

    #词法分析
    statements = """
    IF quantity THEN
    total := total + price * quantity;
    tax := price * 0.05;
    ENDIF;
    """
    for token in tokenize(statements):
        print(token)