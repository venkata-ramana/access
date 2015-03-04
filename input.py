from sys import argv

script,number = argv
def input(number):
    if len(number) == 10:
        print "yes"
    else:
        print "no"

if __name__ == "__main__":
    input(number)


