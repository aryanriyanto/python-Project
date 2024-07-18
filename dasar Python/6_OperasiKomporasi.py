print("---Operasi Komporasi---");
print("jawaban yang dihasilkan adalah TRUE / FALSE");
print("========================================");

c = int;

a = int(input("Masukan nilai A : "));
b = int(input("Masukan nilai B : "));


""""lebih dari"""
c= a > b;
print(a,'>',b,'=',c);

""""kurang dari"""
c= a < b;
print(a,'<',b,'=',c);

""""lebih dari sama dengan"""
c= a >= b;
print(a,'>=',b,'=',c);

""""kurang dari sama dengan"""
c= a <= b;
print(a,'<=',b,'=',c);

""""sama dengan"""
c= a == b;
print(a,'==',b,'=',c);

""""tidak sama dengan"""
c= a != b;
print(a,'>=',b,'=',c);

""""pembandingkan object/memory"""
c= a is b;
print(a,'is',b,'=',c);

""""is not"""
c= a is not b;
print(a,'is not',b,'=',c);