# List of the characters, numbers, alphabets used to create passwords

alphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "%", "\\", "|", "=", "[", "]", "<", ">", "{", "}", "@", "#", "$", "_", "&", "-", "+", "(", ")", "*", '"', "'", ":", ";", "!", "?", ",", ".", "-", "~", "^"]
# print(len(alphaList))  # 98

# Creating File To append the passwords
file_name = input("Enter name of file to be created (without extention) : ") + ".txt"
print(file_name)

with open(file_name, "w") as f:
    f.close()


#  Passwords for 1 key
def passwd1():
    print(94)
    f = open(file_name, "a")
    para1 = [[i] for i in alphaList]
    # print(para1)
    arr1 = ["".join([j for j in i]) for i in para1]
    # print(arr1)
    # char = 0
    for i in arr1:
        f.write(i + "\n")
        # print(i, end = "\n")
        # char += 1
        # print(char)
    f.close()


#  Passwords for 2 key
def passwd2():
    print(94**2)
    f = open(file_name, "a")
    para2 = [[i, j] for i in alphaList for j in alphaList]
    arr2 = ["".join([j for j in i]) for i in para2]
    for i in arr2:
        f.write(i + "\n")
    f.close()


#  Passwords for 3 key
def passwd3():
    print(94**3)
    f = open(file_name, "a")
    para3 = [[i, j, k]
             for i in alphaList for j in alphaList for k in alphaList]
    arr3 = ["".join([j for j in i]) for i in para3]
    for i in arr3:
        f.write(i + "\n")
    f.close()

#  Passwords for 4 key
def passwd4():
    print(94**4)
    f = open(file_name, "a")
    para4 = [[i, j, k, l]
             for i in alphaList for j in alphaList for k in alphaList for l in alphaList]
    arr4 = ["".join([j for j in i]) for i in para4]
    for i in arr4:
        f.write(i + "\n")
    f.close()


#  Passwords for 5 key
def passwd5():
    print(94**5)
    f = open(file_name, "a")
    para5 = [[i, j, k, l, m]
             for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList]
    arr5 = ["".join([j for j in i]) for i in para5]
    for i in arr5:
        f.write(i + "\n")
    f.close()


#  Passwords for 6 key
def passwd6():
    print(94**6)
    f = open(file_name, "a")
    para6 = [[i, j, k, l, m, n]
             for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList]
    arr6 = ["".join([j for j in i]) for i in para6]
    for i in arr6:
        f.write(i + "\n")
    f.close()


#  Passwords for 7 key
def passwd7():
    print(94**7)
    f = open(file_name, "a")
    para7 = [[i, j, k, l, m, n, o]
             for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList]
    arr7 = ["".join([j for j in i]) for i in para7]
    for i in arr7:
        f.write(i + "\n")
    f.close()


#  Passwords for 8 key
def passwd8():
    print(94**8)
    f = open(file_name, "a")
    para8 = [[i, j, k, l, m, n, o, p]
             for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList]
    arr8 = ["".join([j for j in i]) for i in para8]
    for i in arr8:
        f.write(i + "\n")
    f.close()


#  Passwords for 9 key
def passwd9():
    print(94**9)
    f = open(file_name, "a")
    para9 = [[i, j, k, l, m, n, o, p, q]
             for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList]
    arr9 = ["".join([j for j in i]) for i in para9]
    for i in arr9:
        f.write(i + "\n")
    f.close()


#  Passwords for 10 key
def passwd10():
    print(94**10)
    f = open(file_name, "a")
    para10 = [[i, j, k, l, m, n, o, p, q, r]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList]
    arr10 = ["".join([j for j in i]) for i in para10]
    for i in arr10:
        f.write(i + "\n")
    f.close()


#  Passwords for 11 key
def passwd11():
    print(94**11)
    f = open(file_name, "a")
    para11 = [[i, j, k, l, m, n, o, p, q, r, s]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList]
    arr11 = ["".join([j for j in i]) for i in para11]
    for i in arr11:
        f.write(i + "\n")
    f.close()


#  Passwords for 12 key
def passwd12():
    print(94**12)
    f = open(file_name, "a")
    para12 = [[i, j, k, l, m, n, o, p, q, r, s, t]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList]
    arr12 = ["".join([j for j in i]) for i in para12]
    for i in arr12:
        f.write(i + "\n")
    f.close()


#  Passwords for 13 key
def passwd13():
    print(94**13)
    f = open(file_name, "a")
    para13 = [[i, j, k, l, m, n, o, p, q, r, s, t, u]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList for u in alphaList]
    arr13 = ["".join([j for j in i]) for i in para13]
    for i in arr13:
        f.write(i + "\n")
    f.close()


#  Passwords for 14 key
def passwd14():
    print(94**14)
    f = open(file_name, "a")
    para14 = [[i, j, k, l, m, n, o, p, q, r, s, t, u, v]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList for u in alphaList for v in alphaList]
    arr14 = ["".join([j for j in i]) for i in para14]
    for i in arr14:
        f.write(i + "\n")
    f.close()


#  Passwords for 15 key
def passwd15():
    print(94**15)
    f = open(file_name, "a")
    para15 = [[i, j, k, l, m, n, o, p, q, r, s, t, u, v, w]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList for u in alphaList for v in alphaList for w in alphaList]
    arr15 = ["".join([j for j in i]) for i in para15]
    for i in arr15:
        f.write(i + "\n")
    f.close()


#  Passwords for 16 key
def passwd16():
    print(94**16)
    f = open(file_name, "a")
    para16 = [[i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList for u in alphaList for v in alphaList for w in alphaList for x in alphaList]
    arr16 = ["".join([j for j in i]) for i in para16]
    for i in arr16:
        f.write(i + "\n")
    f.close()


#  Passwords for 17 key
def passwd17():
    print(94**17)
    f = open(file_name, "a")
    para17 = [[i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList for u in alphaList for v in alphaList for w in alphaList for x in alphaList for y in alphaList]
    arr17 = ["".join([j for j in i]) for i in para17]
    for i in arr17:
        f.write(i + "\n")
    f.close()


#  Passwords for 18 key
def passwd18():
    print(94**18)
    f = open(file_name, "a")
    para18 = [[i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList for u in alphaList for v in alphaList for w in alphaList for x in alphaList for y in alphaList for z in alphaList]
    arr18 = ["".join([j for j in i]) for i in para18]
    for i in arr18:
        f.write(i + "\n")
    f.close()


#  Passwords for 19 key
def passwd19():
    print(94**19)
    f = open(file_name, "a")
    para19 = [[i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList for u in alphaList for v in alphaList for w in alphaList for x in alphaList for y in alphaList for z in alphaList for a in alphaList]
    arr19 = ["".join([j for j in i]) for i in para19]
    for i in arr19:
        f.write(i + "\n")
    f.close()


#  Passwords for 20 key
def passwd20():
    print(94**20)
    f = open(file_name, "a")
    para20 = [[i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, a, b]
              for i in alphaList for j in alphaList for k in alphaList for l in alphaList for m in alphaList for n in alphaList for n in alphaList for o in alphaList for p in alphaList for q in alphaList for r in alphaList for s in alphaList for t in alphaList for u in alphaList for v in alphaList for w in alphaList for x in alphaList for y in alphaList for z in alphaList for a in alphaList for b in alphaList]
    arr20 = ["".join([j for j in i]) for i in para20]
    for i in arr20:
        f.write(i + "\n")
    f.close()


if __name__ == "__main__":
    try:
        charkey = int(
            (input("Enter the no. of characters passwords must be (maximum - 20): ")))
    except Exception as e:
        print("Give a numeric value only...")

    if charkey == 1:
        passwd1()
    elif charkey == 2:
        passwd2()
    elif charkey == 3:
        passwd3()
    elif charkey == 4:
        passwd4()
    elif charkey == 5:
        passwd5()
    elif charkey == 6:
        passwd6()
    elif charkey == 7:
        passwd7()
    elif charkey == 8:
        passwd8()
    elif charkey == 9:
        passwd9()
    elif charkey == 10:
        passwd10()
    elif charkey == 11:
        passwd11()
    elif charkey == 12:
        passwd12()
    elif charkey == 13:
        passwd13()
    elif charkey == 14:
        passwd14()
    elif charkey == 15:
        passwd15()
    elif charkey == 16:
        passwd16()
    elif charkey == 17:
        passwd17()
    elif charkey == 18:
        passwd18()
    elif charkey == 19:
        passwd19()
    elif charkey == 20:
        passwd20()
    else:
        print("Do You Want To Kill Me?")
