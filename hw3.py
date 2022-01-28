import math
import csv
import os

def q1(string_input):
    v_count = 0
    c_count = 0
    for i in string_input:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            v_count += 1
        else:
            c_count +=1
    if v_count > c_count:
        return True
    elif c_count > v_count:
        return False
    else:
        return None
        
print(q1("aaabbb"))

def q2(rad, hei):
    rad_sq = math.pow(rad, 2)
    vol = (math.pi) * hei * rad_sq
    return vol

print(q2(3,5))

def q3(string_list):
    string1 = ""
    for i in string_list:
        string1 += i
        string1 += ", "
    return string1

print(q3(["hello", "insert", "name"]))

def q4(list_of_list):
    string2 = ""
    for i in list_of_list:
        s = q3(i)
        string2 += s
    z = open("file.txt", "w")
    z.write(string2)
    return ("file.txt")

print(q4([["hello", "insert"], ["name", "here"]]))

def q5(csvfile1):
    z = open(csvfile1, "r", encoding = 'utf-8-sig')
    list1 = []
    lines1 = z.readlines()
    for row in lines1:
        string1 = row.split()
        string1 = list(string1)
        list1.append(list(string1))
    return list1

print(q5('hw3.csv'))

def q6(num1, num2):
    try:
        nums = num1 / num2
        return nums
    except Exception as e:
        print('This code is not running because of ', e)

print(q6(1, 0))

def q7(list_ints):
    list1 = []
    for i in list_ints:
        if i in list1:
            continue
        list1.append(i)
    return list1

print(q7([8, 8, 6, 2, 4, 5, 6, 3, 4]))

def q8(foldername):
    try:
        directory = foldername
        cur_dir = os.getcwd()
        fin_dir = os.path.join(cur_dir, directory)
        os.mkdir(fin_dir)
        return "New Folder Created"
    except FileExistsError:
        return "This file already exists."

print(q8("newest folder"))