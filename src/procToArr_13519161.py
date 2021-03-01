#fungsi yang menerima input nama file kemudian mengembalikan
#array of string perlines dari file input
def strmatkul(name): 
    f = open(name,'r') 
    file = f.readlines()
    operand = []
    #melakukan replace beberapa character seperti koma, titik, dan newline
    for lines in file:
        lines = lines.replace(","," ")
        lines = lines.replace("\n"," ")
        lines = lines.replace("."," ")
        operand.append(lines)
    return operand

#fungsi yang menerima input array of string kemudian 
#mengembalikan array of array dari elemen pada matkul prereq
def makeArr(arr):
    a = ['' for i in range(len(arr))]
    i = 0
    #melakukan split dari string untuk menghasilkan array
    for lines in arr:
        #melakukan split dari string untuk menghasilkan array
        a[i] = lines.split()
        i+=1
    return a

#fungsi yang menerima input berupa array of array dari 
#elemen matkul prereq, kemudian menghasilkan array of array
#yang berisi elemen maktul beserta derajat masuk
def makeArrdegreein(arr):
    a = [['' for j in range(2)] for i in range(len(arr))]
    i = 0
    for lines in arr:
        count = len(arr[i])-1
        a[i][0] = lines[0] #memasukkan elemen
        a[i][1] = count #memasukkan derajat masuk
        i+=1
    return a
