"""Membuat gabungan area rentang dari angka
++++++3------------10+++++++
"""

inputUser = int(input("Masukan angka yang bernilai : "));

#+++++3----------
#Meriksa angka < 3
KurangDari = (inputUser < 3);
print(KurangDari);

#--------10++++++
#Meriksa angka 3 > 10
LebihDari = (inputUser > 10);
print(LebihDari);

#+++++3--------10+++++++
isCorrect = KurangDari or LebihDari
print("Angka yang dimasukan or : ",isCorrect);

#-----3+++++++10--------
isCorrect = KurangDari and LebihDari
print("Angka yang dimasukan and : ",isCorrect);

isCorrect = KurangDari ^ LebihDari
print("Angka yang dimasukan xor : ",isCorrect);

""""PR
Masukan angka, dengan rentang
no.1 ------0++++++++5--------8+++++++++11--------
no.2 ++++++0-------5++++++++8---------11++++++++
"""