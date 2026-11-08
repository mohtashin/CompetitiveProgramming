white=list(map(int, input().split(" ")))
b1=list(map(int, input().split(" ")))
b2=list(map(int, input().split(" ")))

whitell=(white[0],white[1])
whiteur=(white[2],white[3])
whitelr=(white[2],white[1])
whiteul=(white[0],white[3])

b1ll=(b1[0],b1[1])
b1ur=(b1[2],b1[3])
b1lr=(b1[2],b1[1])
b1ul=(b1[0],b1[3])

b2ll=(b2[0],b2[1])
b2ur=(b2[2],b2[3])
b2lr=(b2[2],b2[1])
b2ul=(b2[0],b2[3])


widthb1w = min(b1lr[0], whitelr[0]) - max(b1ll[0],whitell[0])
widthb2w = min(b2lr[0], whitelr[0]) - max(b2ll[0],whitell[0])
heightb1w = min(b1lr[1], whitelr[1]) - max(b1ll[1],whitell[1])
heightb2w = min(b2lr[1], whitelr[1]) - max(b2ll[1],whitell[1])


areab1w = widthb1w * heightb1w
areab2w= widthb2w * heightb2w
b1area=(b1[3]-b1[1]) * (b1[2]-b1[0])
b2area=(b2[3]-b2[1]) * (b2[2]-b2[0])

widthmb1 = min(b1lr[0], b2lr[0]) - max(b1ll[0],b2ll[0])
heightmb1 = min(b1lr[1], b2lr[1]) - max(b1ll[1],b2ll[1])

areamb1=widthmb1*heightmb1


union=areab1w+areab2w-areamb1
