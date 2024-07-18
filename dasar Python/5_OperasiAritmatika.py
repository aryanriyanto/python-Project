print("---Operasi Aritmatika---");
print("========================================");

a =int (input("Masukan Angka A : "));
b =int (input("Masukan Angka B : "));
print("========================================");
c = a + b;
print(a,'+',b,'=',float(c)); """Cara penulisan jika ingin mengubah ke type data yang lain"""
c = a + b;
print(a,'+',b,'=', c);

c = a - b;
print(a,'-',b,'=',c);

c = a * b;
print(a,'*',b,'=',c);

c = a / b;
print(a,'/',b,'=',c);

c = a ** b; """"Pangkat"""
print(a,'**',b,'=',c);

c = a % b; """"Modulus / sisa Pembagian"""
print(a,'%',b,'=',c);

c = a // b; """"Floor Division atau kebalikan Modulus"""
print(a,'//',b,'=',c);

print("========================================\n");