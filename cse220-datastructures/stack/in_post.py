from _Stack import Stack
from _Snipp import p
from _Snipp import opener
from _Snipp import obrs, cbrs, ops


def in_post(expr):
    s = Stack()
    output = ""

    # for formatting
    pd = len(expr) // 2

    for ch in expr:
        if ch in ops:
            print('operator', ch)
            if s.not_empty():
                top = s.peek()
                if top in ops and p(top) < p(ch):
                    s.push(ch)
                else:
                    while s.not_empty() and s.peek() in ops and p(
                            s.peek()) >= p(ch):
                        output += s.pop()
                    s.push(ch)
            else:
                s.push(ch)
        elif ch in obrs:
            # pushing to the operant stack
            s.push(ch)
        elif ch in cbrs:
            while s.peek() != opener(ch):
                # poping to the print stack
                output += s.pop()
            s.pop()
        else:
            output += ch

        # show outputs
        i = len(s.rev())
        print(f'{ch} :> {s.rev()}{" "*(pd-i)} | { output}')

    while s.not_empty():
        output += s.pop()
        # show outputs
        i = len(s.rev())
        print(f'{ch} :> {s.rev()}{" "*(pd-i)} | { output}')
    return output


if __name__ == "__main__":
    ai = 'a+b*c-d'
    ap = 'abc*+d-'

    bi = "A*{B+C-(D+E/F)}"
    bp = "ABC+DEF/+-*"

    ci = 'A+B*(C-D/E)'
    cp = 'ABCDE/-*+'

    di = "a+b*(c-d/e)"
    dp = 'abcde/-*+'

    ri = "3+[5/7-{5%(1+3*1)-0}+1]-1"

    # quiz slver
    q2i = 'A+[B*C+(D/E)+F]-G'

    # pracsheet
    a7i = '3+[5/7-{5%(1+3*1)-0}+1]-1'

    ###################################################
    t = ci
    res = in_post(t)
    print("--------------------------------------------------")
    print(f"infix:{t}=> postfix:{res}")
    print(len(res), len(t))
