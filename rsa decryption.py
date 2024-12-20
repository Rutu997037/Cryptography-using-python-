def rsa():
 p = 3
 q = 7
 n = p * q
 print("n =", n)
 phi = (p - 1) * (q - 1)
 print("phi =", phi)
 e = 5
 print("e =", e)

 k = 1
 while (k * phi + 1) % e != 0:
  k += 1
 d = (k * phi + 1) // e
 print("d =", d)

 M = 10
 C = pow(M, e, n)
 print("Encrypted message (C) =", C)

 decrypted_M = pow(C, d, n)
 print("Decrypted message (M) =", decrypted_M)
rsa()