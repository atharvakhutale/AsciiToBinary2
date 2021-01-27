


def AsciiToBinary(txt):
    return [bin(ord(x))[2:].zfill(8) for x in txt]    
    #bin(x) returns binary 0b00000000
    #Ord(x) returns int value
    #zfill(8) adds zeros to the beginning of the string    

newTxt = "Hello World"

bTxt = AsciiToBinary(newTxt)

for b in bTxt:
    print(b)