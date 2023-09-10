# Enter your code here. Read input from STDIN. Print output to STDOUT
def repeater(string):

    num = 0
    string_list = []

    for char in string:
        if char.isdigit():
            num=num+int(char)
        else:
            string_list.append(char)
    
    string_without_digits = ''.join(string_list)

    if num>0:
        return string_without_digits*num
    else:
        return string_without_digits

if __name__=='__main__':
    # string=input()
    string="welco5me2"
    print(repeater(string))