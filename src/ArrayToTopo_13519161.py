from procToArr_13519161 import strmatkul,makeArr,makeArrdegreein

#fungsi ini menerima input berupa array of array dari
#elemen matkul elemen, dan juga string berupa elemen,
#kemudian mengembalikan array of array dengan elemen sudah dihapus
def DeleteEl(arr, element):
    a = ['' for i in range(len(arr)) ]
    i = 0
    #melakukan deleting elemen
    for lines in arr:
        #merubah array of words menjadi string
        lines = ' '.join(lines)
        #me-replace element dengan spasi apabila terdapat elemen pada string
        lines = lines.replace(element," ")
        #melakukan split untuk menghasilkan array dari string
        lines = lines.split()
        #maemasukkannya ke array a
        a[i] = lines
        i+=1
    a.remove([]) #menghapus list kosong
    return a

#fungsi ini menerima input berupa array of array dari elemen matkul prereq
#array of array dari array derajat masuk, beserta arrFin yang berupa 
# array yang nantinya akan dikembalikan sebagai solusi topological sort  
def Topological(arrPre, arrdegree, arrFin):
    if (len(arrdegree)==0): #apabila sudah tidak terdapat elemen //basis
        return arrFin
    else:   #rekursif 
        element = [] 
        for i in range(len(arrdegree)) :
            if (arrdegree[i][1] == 0) :
                #append elemen yang berderajat 0
                element.append(arrdegree[i][0])
        arrfinnew = []
        arrFin.append(element)
        arrfinnew = arrFin
        #malakukan update terhadap array of array prereq
        newDelpre = arrPre
        for words in element:
            #menghapus elemen yang berderajat 0 
            newDelpre = DeleteEl(newDelpre,words)
        #melakukan update terhadap array derajat masuk
        decdegree = makeArrdegreein(newDelpre)
        return Topological(newDelpre,decdegree,arrfinnew)
    
#prosedur ini menerima array of array elemen matkul yang 
#kemudian melakukan print berupa output sesuai dengan format
#yang dibuat
def outputSemester(arrayfinal):
    i = 1
    #malakukan printing solusi
    for semester in arrayfinal:
        print("Semester ",i," : ",end="")
        for j in range(len(semester)):
            print(semester[j],end="")
            if (j==len(semester)-1) :
                print(".",end="")
            else:
                print(", ",end="")
        print()
        i+=1