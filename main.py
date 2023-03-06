import re


def ex1(string):
    return string[::-1]

def ex2(string):
    if string == sorted(string):
        return True
    else:
        return False
    
def ex3(string):
    return len(string.split())
    
def ex4(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower

def ex5(string):
    string = re.sub(r'[^a-zA-Z0-9]', '', string)
    return string
    
def ex6(string, n):
    for chr in string :
        for i in range(n):
            print(chr, end='')

def ex7(oddn):
    sum = 0
    for i in range(oddn):
        if i % 2 != 0:
            sum += i
    return sum

def ex8(evenn):
    numbers = []
    for i in range(evenn):
        if i % 2 == 0:
            numbers.append(i)
    return numbers

def ex9(string):
    if string == string[::-1]:
        return True
    else:
        return False

def ex10(string1, string2):
    if len(string1) != len(string2):
        return print("Strings must be the same length")
    else:
        if string1 == string2:
            return print("Strings are the same")
        else:
            count = 0
            for i in range(len(string1)):
                if string1[i] != string2[i]:
                    count += 1
            return print("Hamming distance is: ", count)



