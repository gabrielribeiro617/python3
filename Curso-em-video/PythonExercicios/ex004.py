n = input('\033[1;32mDigite algo: ')
print('\033[1;32mO tipo primitivo desse valor é \033[1;33m{}'.format(type(n)))
print('\033[1;32mEle só tem espaços? \033[1;33m{}'.format(n.isspace()))
print('\033[1;32mEle é um número? \033[1;33m{}'.format(n.isnumeric()))
print('\033[1;32mEle é alfabético? \033[1;33m{}'.format(n.isalpha()))
print('\033[1;32mEle é alfanumérico? \033[1;33m{}'.format(n.isalnum()))
print('\033[1;32mEle está em minúsculo? \033[1;33m{}'.format(n.islower()))
print('\033[1;32mEle está em maiúsculo? \033[1;33m{}'.format(n.isupper()))
print('\033[1;32mEle está capitalizado? \033[1;33m{}'.format(n.istitle()))
