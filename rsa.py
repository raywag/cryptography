
def rsa(p, q, e):
   n = p * q
   w = (p-1) * (q-1)
   d = pow(e, -1, w)
   return d, n


def rsa_encrypt(plaintext, e, n):
   return pow(plaintext, e, n)


def rsa_decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)


if __name__ == '__main__':
    #p = input("Please enter the value for p: ")
    #q = input("Please enter the value for q: ")
    #print("17 is chosen as value for e")
    #key_calc = rsa(int(p), int(q), 17)
    print("This rsa function uses the values p=7, q=11, e=17")
    key_calc = rsa(7, 11, 17)
    print(f'd= {key_calc[0]}, n= {key_calc[1]}')

    input_plain = input("please enter your integer plaintext in the range 0 and 76: ")
    ciphertext = rsa_encrypt(int(input_plain), 17, key_calc[1])
    print(f'ciphertext of {input_plain}: {ciphertext}')

    plaintext = rsa_decrypt(ciphertext, key_calc[0], key_calc[1])
    print(f'decrypted plaintext: {plaintext}')



