from _Stack import Stack
from _Snipp import p
from _Snipp import opener
from _Snipp import obrs, cbrs, ops


def post_in(expr):
    s = Stack()
    outputs = ""

    for ch in expr:
        print(ch)
        if ch in ops:
            b = s.pop()
            a = s.pop()
            s.push(f"({a}{ch}{b})")
        else:
            s.push(ch)
        print(s)
    return s.pop()


if __name__ == "__main__":
    ai = 'a+b*c-d'
    ap = 'abc*+d-'

    bi = "A*{B+C-(D+E/F)}"
    bp = "ABC+DEF/+-*"

    ci = 'A+B*(C-D/E)'
    cp = 'ABCDE/-*+'

    di = "a+b*(c-d/e)"
    dp = 'abcde/-*+'

    # quiz slver
    q2i = 'A+[B*C+(D/E)+F]-G'
    q2p = "ABC*DE/+F++G-"

    ###################################################
    t = 'ABC*D/+E-'
    t = '259%+2-62-+2/36*8-1++'
    res = post_in(t)
    print("--------------------------------------------------")
    print(f"postfix: {t} => infix: {res}")
    print(eval(res))
