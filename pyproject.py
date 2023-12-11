MAX_LINES=3
def deposit():
    while(True):
        amount=input("Enter the amount: $")
        if amount.isdigit :
            amount=int(amount)
            if(amount<0):
                print("Enter postive amount!")
            else:
                return amount
        else:
            print("Plz Enter a valid amount !")

def get_line():
    while(True):
        line=input("Enter lines(1-"+str(MAX_LINES)+"): ")
        if line.isdigit :
            line=int(line)
            if(0>line or line>MAX_LINES ):
                print("Enter lines on the range(1-"+str(MAX_LINES)+"): ")
            else:
                return line
        else:
            print("Plz Enter a valid input !")

print(deposit())
print(get_line())
        