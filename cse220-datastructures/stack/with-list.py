from in_post import in_post as ip
from post_in import post_in as pi
from post_eval import post_eval as pe

if __name__ == "__main__":
    q0 = "(1/6>c)==[{(6-2-3)&&(x==8-1)}!=4*3]"
    q1 = "( 1 / 6 > c ) == [ { ( 6 > 2 - 3 ) && ( x == 8 - 1 ) } != 4 * 3 ]"
    q2 = q1.split(" ")

    print(ip(q2))
