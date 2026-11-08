fin = open("billboard.in", "r")

b1 = list(map(int, fin.stdin.readline().split()))
b2 = list(map(int, fin.stdin.readline().split()))
truck = list(map(int, fin.stdin.readline().split()))


b1ll=(b1[0],b1[1]) #(1,2)
b1ur=(b1[2],b1[3]) #(3,5)
b1lr=(b1[2],b1[1]) #(3,2)
b1ul=(b1[0],b1[3]) #(1,5)

b2ll=(b2[0],b2[1])
b2ur=(b2[2],b2[3])
b2lr=(b2[2],b2[1])
b2ul=(b2[0],b2[3])

truckll=(truck[0],truck[1])
truckur=(truck[2],truck[3])
trucklr=(truck[2],truck[1])
truckul=(truck[0],truck[3])


widthb1t = min(b1lr[0], trucklr[0]) - max(b1ll[0],truckll[0])
widthb2t = min(b2lr[0], trucklr[0]) - max(b2ll[0],truckll[0])
heightb1t = min(b1lr[1], trucklr[1]) - max(b1ll[1],truckll[1])
heightb2t = min(b2lr[1], trucklr[1]) - max(b2ll[1],truckll[1])

areab1t= widthb1t*heightb1t
areab2t= widthb2t*heightb2t
b1area=(b1[3]-b1[1]) * (b1[2]-b1[0])
b2area=(b2[3]-b2[1]) * (b2[2]-b2[0])

print(b1area+b2area-areab1t-areab2t)
