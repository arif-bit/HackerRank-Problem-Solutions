def print_formatted(number):
    for i in range(1,number+1):
        # print(str(i)+" "+oct(i)[2:]+" "+hex(i)[2:].upper()+" "+bin(i)[2:] )
        space=len(bin(number)[2:])
        print("{0} {1} {2} {3}".format(str(i).rjust(space),oct(i)[2:].rjust(space),hex(i)[2:].rjust(space).upper(),bin(i)[2:].rjust(space)))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)