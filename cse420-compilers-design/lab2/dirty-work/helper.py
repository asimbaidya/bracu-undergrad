left_curly_brace = "{"
right_curly_brace = "}"


def format_rule(left, prefix, right_i, line_one, line_two, line_three):
    print(f"{prefix} {right_i}  {left_curly_brace}")
    print(f"    {line_one}")
    print(f"    {line_two}")
    print(f"    {line_three}")
    print(f"{right_curly_brace}")


# read cfgs
with open("./pdf.txt") as file:
    data = file.read()

    # CFGs are separated by ;
    rules = data.split(";")
    rules.pop()  # remove tailing empty string

    # rules - production rules
    # pr - production rule
    for pr in rules:
        left, right = pr.split(":")

        # left - non terminals
        left = left.strip()

        # right - terminal/non terminal
        right = right.split("\n|")
        right = [x.strip() for x in right]
        right = [x for x in right if x != ""]

        ## ****
        print(left, end=" ")

        for ind in range(len(right)):
            right_i = right[ind]
            right_i_tokens = right_i.split(" ")

            total_tokens = len(right_i.split(" "))

            # line 1
            line_one = (
                f'outlog<<"At line no: "<<lines<<" {left} : {right_i} "<<endl<<endl;'
            )

            # symbols
            sym_getname = [f"${str(x)}->getname()" for x in range(1, total_tokens + 1)]

            # line 2
            line_two = ""
            for i in range(len(sym_getname)):
                if (
                    right_i_tokens[i] == "LCURL"
                    or right_i_tokens[i] == "RCURL"
                    or right_i_tokens[i] == "SEMICOLON"
                ):
                    line_two += f'{sym_getname[i]}<<"\\n"<<'
                else:
                    line_two += f'{sym_getname[i]}<<" "<<'
            line_two = f"outlog<<{line_two}endl<<endl;"
            # print(line_two)

            # line 3
            line_three = ""
            for i in range(len(sym_getname)):
                if (
                    right_i_tokens[i] == "LCURL"
                    or right_i_tokens[i] == "RCURL"
                    or right_i_tokens[i] == "SEMICOLON"
                ):
                    line_three += f'{sym_getname[i]}+"\\n"+'
                else:
                    line_three += f"{sym_getname[i]}+"
            line_three = line_three[:-1]
            line_three = f'$$ = new symbol_info({line_three},"{left}");'
            # print(line_three)

            # # prefix
            prefix = ":"
            if ind != 0:
                prefix = "    |"

            format_rule(left, prefix, right_i, line_one, line_two, line_three)
