def leiaDinheiro(txt):
    while True:
        val = str(input(txt)).strip().replace(',', '.')
        try:
            float(val)
            break
        except ValueError:
            print(f'\033[31mERRO! \"{val}\" é um preço inválido!\033[m')
    return float(val)


def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return
        else:
            return num


def leiaFloat(txt):
    while True:
        try:
            num = str(input(txt)).strip().replace(',', '.')
            float(num)
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def acessivel(url):
    import requests

    try:
        site = requests.get(url, verify=False)
        if site.status_code == 200:
            return f'\033[32mConsegui acessar o site {url} com sucesso!'
    except requests.exceptions.RequestException:
        return f'\033[31mO site {url} não está acessível no momento.'


def menu(lst):
    from utilidadesCeV import string

    string.titulo('MENU PRINCIPAL')
    for cont, item in enumerate(lst):
        print(f'\033[1;33m{cont + 1}\033[m - \033[0;34m{item}\033[m')
    string.linha()
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
