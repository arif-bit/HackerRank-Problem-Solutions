if __name__ == '__main__':
    n = int(input())
    output = []
    for i in range(0, n):
        command = input().split()
        if 'insert' in command:
            output.insert(int(command[1]), int(command[2]))
        elif 'print' in command:
            print(output)
        elif 'remove' in command:
            output.remove(int(command[1]))
        elif 'append' in command:
            output.append(int(command[1]))
        elif 'sort' in command:
            output.sort()
        elif 'pop' in command:
            output.pop()
        else:
            output.reverse()