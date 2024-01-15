def insert(cir,item,start,size,index):
    if size < len(cir):
        x  = (start+size-1)%len(cir)
        y = (x+1)%len(cir)

        while y != index:
            cir[y] = cir[x]
            x = x-1
            if x < 0:
                x = 0
            y = y -1
            if y < 0:
                y = 0
    else:
        resize() # where the fuck resize come from
        # fucking repeat what fuck!

