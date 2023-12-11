
def sub_n(li,sli):
    re=""
    se=""
    for n in li:
        re=re + ','.join(str(n))
    for n in sli:
        se=se + ','.join(str(n))
    print(re)
    print(se)
    if se in re:
        print("True")
    else:
        print("False")
sub_n([1,2,3,4,5,6],[1,4])