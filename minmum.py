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
    l5 = [int(l.split()[3]) for l in open(readpath)]

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
    # calculate the maximum
    w1 = 0
    while w1 < length - 2:
        if arry[0][w1+1] < arry[0][w1] and arry[0][w1 + 1] < arry[0][w1 + 2]:
            rearry[0].append(w1+2)
        if arry[1][w1 + 1] < arry[1][w1] and arry[1][w1 + 1] < arry[1][w1 + 2]:
            rearry[1].append(w1+2)
        if arry[2][w1 + 1] < arry[2][w1] and arry[2][w1 + 1] < arry[2][w1 + 2]:
            rearry[2].append(w1+2)
        if arry[3][w1 + 1] > arry[3][w1] and arry[3][w1 + 1] < arry[3][w1 + 2]:
            rearry[3].append(w1+2)
        if arry[4][w1 + 1] > arry[4][w1] and arry[4][w1 + 1] < arry[4][w1 + 2]:
            rearry[4].append(w1+2)
        w1 = w1 + 1
    print(len(rearry[0]))
    print(len(rearry[1]))
    # for i in range(len(rearry[0])):
    #         filewrite.write(str(rearry[0][i]) + '\t' + str(rearry[1][i]) + '\t' + '\t' + str(rearry[2][i]) + '\t' + str(rearry[3][i]))

    for i in rearry:
        filewrite.write(str(i)+'\r\n')
    filewrite.close()

if __name__ == '__main__':
    fileslist = file_name("/Users/xiejiacheng/Downloads/PWV")
    for file in fileslist:
        filepath = "/Users/xiejiacheng/Downloads/PWV/" + file
        savepath = "/Users/xiejiacheng/coding/congcongresult/mininum/" + file
        maximum(filepath, savepath)
