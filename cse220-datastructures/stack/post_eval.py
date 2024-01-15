from _Stack import Stack
from _Snipp import p
from _Snipp import opener
from _Snipp import obrs, cbrs, ops


def post_eval(expr):
    s = Stack()
    outputs = ""

    for ch in expr:
        if ch in ops:
            b = s.pop()
            a = s.pop()
            ex = f"{a}{ch}{b}"
            s.push(eval(ex))

            # show that evaluating
            print(ex)
        else:
            s.push(ch)
    return s.pop()


if __name__ == "__main__":
    ###################################################
    t = '67384/-*+'
    t = "654*+2-"
    t = '259%+2-62-+2/36*8-1++'

    res = post_eval(t)
    print("--------------------------------------------------")
    print(f"postfix: {t} => infix: {res}")
