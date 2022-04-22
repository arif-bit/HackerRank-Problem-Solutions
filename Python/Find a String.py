def count_substring(string, sub_string):
    result=0
    sub_string_len=len(sub_string)
    for i in range(len(string)):
        if string[i:i+sub_string_len]==sub_string:
            result+=1
    return result



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)