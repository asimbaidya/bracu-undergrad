from in_post import in_post as ip
from post_in import post_in as pi
from post_eval import post_eval as pe

if __name__ == "__main__":
    while True:
        w = input("which operation: ")
        if w == '0':
            print("Exit")
            break
        elif w == 'ip':
            ex = input("Enter expression in infix\n")
            print(ip(ex))
        elif w == 'pi':
            ex = input("Enter expression in postfix\n")
            print(pi(ex))
        elif w == 'pe':
            ex = input("Enter expression in postfix\n")
            print(pe(ex))
        else:
            print(f"{w} is not recognized")
