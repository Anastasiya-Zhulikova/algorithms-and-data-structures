inp = input()
outp = input()

def letter_counter(ls):
    d = dict()
    for el in ls:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    return d

inp_d = letter_counter(inp)
outp_d = letter_counter(outp)
if inp_d == outp_d:
    print("YES")
else:
    print("NO")
