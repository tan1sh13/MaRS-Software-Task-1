def decode_shift(s):
    ds=[]
    i=1
    n=len(s)
    for l in s:
        l=l.upper()
        nl=chr((ord(l)-ord('A')-i) % 26+ord('A'))
        ds.append(nl)
        i+=1
    return "".join(ds)
s=input("Enter the input:")
print("Decoded Output is:",decode_shift(s))
