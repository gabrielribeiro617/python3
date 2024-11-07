from time import sleep
print('\033[33m-=-' * 20)
print(' \033[1;34mConversor de Base Numérica')
print('\033[33m-=-' * 20)
n = int(input('\033[mDigite um número inteiro: '))
print('\033[1m[ 1 ]\033[m BINÁRIO\n\033[1m[ 2 ]\033[m OCTAL\n\033[1m[ 3 ]\033[m HEXADECIMAL')
r = int(input('Para queal você quer converter? '))
print('\033[1;35mPROCESSANDO...\033[m')
sleep(1)
print('\033[1m---' * 10)
if r == 1:
    print('O número {} em \033[1;32mBINÁRIO é {}'.format(n, bin(n)[2:]))
elif r == 2:
    print('O número {} em \033[1;32mOCTAL é {}'.format(n, oct(n)[2:]))
elif r == 3:
    print('O número {} em \033[1;32mHEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('\033[1;31mERRO! O número escolhido não é uma opção!')
