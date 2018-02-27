# -*- coding:utf-8 -*-
import os
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


def maximum(readpath, savepath):
    filewrite = open(savepath, 'w')

    l1 = [int(l.split()[0]) for l in open(readpath)]
    l2 = [int(l.split()[1]) for l in open(readpath)]
    l3 = [int(l.split()[2]) for l in open(readpath)]
    l4 = [int(l.split()[3]) for l in open(readpath)]
    l5 = [int(l.split()[4]) for l in open(readpath)]

    arry = [[], [], [], [], []]
    rearry = [[], [], [], [], []]

    length = len(l1)

    for j1 in l1:
        arry[0].append(j1)
    for j2 in l2:
        arry[1].append(j2)
    for j3 in l3:
        arry[2].append(j3)
    for j4 in l4:
        arry[3].append(j4)
    for j5 in l5:
        arry[4].append(j5)
    w = 0
    s1 =0
    w1 = 0
    a = 0
    s2 = 0
    a1 =0
    b = 0
    s3 =0
    b2 = 0
    c = 0
    c1 = 0
    c2 = 0
    d =0
    d1 = 0
    d2 = 0
    max3 = 0
    max4 =0
    max5 = 0

    while w < length - 1:
        if arry[0][w] < arry[0][w+1]:
            max1 = arry[0][w+1] - arry[0][w]
            if max1 > s1:
                s1 = max1
        w = w + 1

    while w1 < length -1:
        if arry[0][w1] < arry[0][w1+1]:
            x = arry[0][w1+1] - arry[0][w1]
            # print(x)
            if x == s1:
                rearry[0].append(float(w1)+1.5)
        w1 = w1 +1
#--2-----------------------------------------------
    while a < length - 1:
        if arry[1][a] < arry[1][a+1]:
            max2 = arry[1][a+1] - arry[1][a]
            if max2 > s2:
                s2 = max2
        a = a + 1
#
    while a1 < length -1:
        if arry[1][a1] < arry[1][a1+1]:
            x = arry[1][a1+1] - arry[1][a1]
            # print(x)
            if x == s2:
                rearry[1].append(float(a1)+1.5)
        a1 = a1 + 1
#---3----------------------------------------------
    while b < length - 1:
        if arry[2][b] < arry[2][b + 1]:
            max3 = arry[2][b + 1] - arry[2][b]
        if max3 > s3:
            s3 = max3
        b = b + 1

    while b2 < length - 1:
        if arry[2][b2] < arry[2][b2 + 1]:
            x2 = arry[2][b2 + 1] - arry[2][b2]
            # print(x)
            if x2 == s3:
                rearry[2].append(float(b2)+1.5)
        b2 = b2 + 1
# ---4----------------------------------------------
    while c < length - 1:
        if arry[3][c] < arry[3][c + 1]:
            max4 = arry[3][c + 1] - arry[3][c]
        if max4 > c1:
            c1 = max4
        c = c + 1

    while c2 < length - 1:
        if arry[3][c2] < arry[3][c2 + 1]:
            x3 = arry[3][c2 + 1] - arry[3][c2]
            # print(x)
            if x3 == c1:
                rearry[3].append(float(c2)+1.5)
        c2 = c2 + 1
# ---5----------------------------------------------
    while d < length - 1:
        if arry[4][d] < arry[4][d + 1]:
            max5 = arry[4][d + 1] - arry[4][d]
        if max5 > d1:
            d1 = max5
        d = d + 1

    while d2 < length - 1:
        if arry[4][d2] < arry[4][d2 + 1]:
            x4 = arry[4][d2 + 1] - arry[4][d2]
            # print(x)
            if x4 == d1:
                rearry[4].append(float(d2)+1.5)
        d2 = d2 + 1
    # for i in range(len(rearry[0])):
    #         filewrite.write(str(rearry[0][i]) + '\t' + str(rearry[1][i]) + '\t' + '\t' + str(rearry[2][i]) + '\t' + str(rearry[3][i]) +'\t' +str(rearry[4][i]))
    print(rearry)
    for i in rearry:
        filewrite.write(str(i)+'\r\n')
    filewrite.close()

if __name__ == '__main__':
    fileslist = file_name("/Users/xiejiacheng/Downloads/PWV")
    for file in fileslist:
        filepath = "/Users/xiejiacheng/Downloads/PWV/" + file
        savepath = "/Users/xiejiacheng/coding/congcongresult/maxslope/" + file
        maximum(filepath, savepath)

