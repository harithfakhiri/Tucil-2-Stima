from ArrayToTopo_13519161 import DeleteEl,Topological,outputSemester
from procToArr_13519161 import strmatkul,makeArr,makeArrdegreein

def main():
    filename = str(input("Masukkan nama file prereq mata kuliah: ")) 
    #memasukkan input nama file dengan format nya, contoh "<namafile>.txt"
    fname = "../test/"+filename
    #membuat array perlines dari input
    a = strmatkul(fname)
    #membuat array of array of elemen matkul dari prereq input
    arrayPre = makeArr(a) 
    #membuat array of array yang berisi elemen dan jumlah derajat masuk
    arraydegree = makeArrdegreein(arrayPre)
    sort=[] #inisiasi array kosong
    # melakukan topological sorting
    topo = Topological(arrayPre,arraydegree,sort)
    print()
    print("Solusi penyusunan rencana kuliah :")
    print()
    #output print solusi
    outputSemester(topo)
    print()


main()