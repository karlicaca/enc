def encrypt(arr, key):
    encrypted = [None] * len(arr)
    for i in range(len(arr)):
        encrypted[i] = arr[i] ^ ord(key[i % len(key)])
    return encrypted


template = '''#https://t.me/j_b_i\ndef decrypt(arr, key):
    decrypted = ""
    for i in range(len(arr)):
        decrypted += chr(arr[i] ^ ord(key[i % len(key)]))
    return decrypted


key = input(" Password : ")
exec(decrypt({}, key))'''

filename = input("اسـم الـمـلـف الـمـراد تـشـفـيـره : ")
key = input(" بـاسـورد الـذي تـريـد وضـعـه فـي الاداة : ")
with open(filename, 'rb') as fin:
    encrypted = encrypt(list(fin.read()), key)
    fin.close()

encrypted_programm = template.format(encrypted)
with open(filename[:-3] + "-enc" + ".py", 'w') as fout:
    fout.write(encrypted_programm)
    fout.close()