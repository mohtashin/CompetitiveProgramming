n="10 7"
sentence ="hello my name is Bessie and this is my essay"

#If Bessie types a word, and that word can fit on the current line, put it on that line.
#Otherwise, put the word on the next line and continue adding to that line.
#

#The next line contains N
 #words separated by single spaces. No word will ever be larger than K
 #characters, the maximum number of characters on a line.


nk= n.split(" ")
sentence=sentence.split(" ")
counter= int(nk[1])
res=""
for i in range(len(sentence)):
    length=int(len(sentence[i]))

    if counter < length:
        counter= int(nk[1])
        res += "\n"

    if counter >= length:
        counter-=length
        res += sentence[i]
        if i + 1 != int(nk[0]):
            res += " "
