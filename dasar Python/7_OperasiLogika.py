print("---Operasi Logika atau Boolean---");
print("Not/Or/Xor/And");
print("========================================");

a = True;
b = False;

""""Not"""
c = not a;
print("--NOT--");
print('Data a = ',a);
print('Data c (not a)= ',c);

""""Or"""
c = a or b;
print("--OR--");
print(a, 'or', b,'= ',c);

""""And"""
c = a and b;
print("--AND--");
print(a, 'AND', b,'= ',c);

""""Xor"""
c = a ^ b;
print("--XOR (^)--");
print(a, '^', b,'= ',c);