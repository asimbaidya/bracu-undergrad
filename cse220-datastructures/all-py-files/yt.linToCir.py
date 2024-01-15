def linToCir(lin,start,size):
    cir = [0]*len(lin)

    i = 0
    st = start

    while i < len(lin):
        cir[st] = lin[i]
        i = i+1
        st = (st+1)%len(cir)
    print(cir)

lin = [1,2,3,0,0]
linToCir(lin,2,3)
