'''Select primes: p=17 & q=11 
Compute n = pq =17×11=187 ; n=187 
Compute ø(n)=(p–1)(q-1)=16×10=160 
Select e ; gcd(e,160)=1; choose e=7 
Determine d: d*e-1 (mod 160) and d < 160 
Hence, Value is d=23 since 23×7=161= 160+1
Publish public key Kpub={7,187} (e,n) 
Keep secret private key Kpvt={17,11,23} (p,q,d)
message ‘M’= 88 (88<187) 

Encryption: [c = me (mod n)] 
c = 887 (mod 187) = 11 
C = 11 

Decryption: [m = cd (mod n)] 
m = 1123 (mod 187) = 88 
m = 88 
If message is 8888 then ? 
Try the RSA example using the following values:

p = 61
q = 53
e = 17
de ≡ 1 (mod φ(n)) so use d=2753
𝑚=123
Work out:
𝑛
∅(𝑛)
c (Alice works this out using 𝑐=𝑚^𝑒 (𝑚𝑜𝑑 𝑛))
m (Bob works this out using 𝑚=𝑐^𝑑 (𝑚𝑜𝑑 𝑛))

'''
n=60*52

c=(123**17)*n
m=(c**1 )*n
print(n,c)