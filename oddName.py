"""
Stephen Ohl
"""

def main () :
    name = input ( "Please enter your name : ")
    while len ( name ) < 1 :
        print ( "\n\nERROR - Your name can not be nothing\n")
        name = input("Please enter your name : ")

    for i in range ( 1, len ( name ), 2 ) :
        print ( name[i] )

main ()