def append(carr,start,size,value):
    if size < len(carr):
        carr[(start+size)%len(carr)] = value
        print(carr)
    else:
        new_carr = []*(len(carr)+1)
        for i in range(size):
            new_carr[(start+i)%len(new_carr)] = carr[(start+i)%len(carr)]
        new_carr[(start+size)] = value
        print(new_carr)

def insert(carr,start,size,index,value):
    if index < 0 or index == len(carr) :
        return False
    for i in range(index,start+size+1):
        carr[(start+size-i)%len(carr)] = carr[(start+size-i-1)%len(carr)]
    carr[index] = value
    print(carr)



if __name__ == "__main__":

    ca = [0,0,0,3,4,5,6,7,8,9,0,0,0]

    ca_size = 7
    start = 3


    print(ca)
    insert(ca,start,ca_size,3,100)
    append(ca,start,ca_size+1,10)
    append(ca,start,ca_size+2,11)
    append(ca,start,ca_size+3,12)
    append(ca,start,ca_size+4,13)
    append(ca,start,ca_size+5,14)

#    for i in range(ca_size):
#        print(ca[start+i])


