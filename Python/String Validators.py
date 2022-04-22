if __name__ == '__main__':
    s = input()
    if any([True for i in s if i.isalnum()]):
        print(True)
    else:
        print(False)
    if any([True for i in s if i.isalpha()]):
        print(True)
    else:
        print(False)
    if any([True for i in s if i.isdigit()]):
        print(True)
    else:
        print(False)
    if any([True for i in s if i.islower()]):
        print(True)
    else:
        print(False)
    if any([True for i in s if i.isupper()]):
        print(True)
    else:
        print(False)