def notas(* valores, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param valores: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opicional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    from statistics import mean
    boletim = dict()
    boletim['total'] = len(valores)
    boletim['maior'] = max(valores)
    boletim['menor'] = min(valores)
    boletim['média'] = mean(valores)
    if sit:
        if boletim['média'] < 5:
            boletim['situação'] = 'RUIM'
        elif boletim['média'] < 7:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'BOA'
    print('--' * 20)
    return boletim


resp = notas(5.5, 1.5, 10, 6.5, sit=True)
help(notas)
print(resp)
