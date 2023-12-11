import string
alpha=list(string.ascii_lowercase)
def encrp(str1,key):
    e=""
    for i in str1:
        k=alpha.index(i)
        e=e+str(alpha[k+key])
    return e
print(encrp("abcd",2))