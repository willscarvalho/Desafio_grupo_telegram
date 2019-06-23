"""
O professor da disciplina de História da Arte de uma determinada turma
elaborou uma avaliação com dez questões e cada uma delas com 5
respostas. Para otimizar a correção solicitou aos alunos de programação
um programa em Python com as seguintes características:

1 - O programa deve permitir o cadastramento do gabarito da prova ex:
(questão 1 --> resposta a, etc.);

2 - O programa deve solicitar a quantidade de alunos que realizaram a
prova;

3 - Permitir o cadastramento do nome do aluno e de cada uma de suas
respostas da 10 questões;

4 - Ao término da digitação o programa deve imprimir:
a) Relação dos alunos e suas respectivas notas;
b) A maior nota e o(s) nome(s) que obtiveram esse valor;
c) A média das notas da turma;
d) O percentual dos alunos que obtiveram nota acima da média.

"""


def questao_resposta(respostas, questao):
    print("Respostas possíveis: {}.".format(respostas))
    gabarito = str(input("Questão {} - Reposta: ".format(questao)))
    gabarito_questao = {"Questao": questao, "Resposta": gabarito}
    return gabarito_questao


def criar_resposta_prova(respostas, n_questoes):
    gabarito_prova = list()
    for i in range(0, n_questoes):
        questao = i + 1
        gabarito_questao = questao_resposta(respostas, questao)
        gabarito_prova.append(gabarito_questao)
    return gabarito_prova


def quantidade_alunos():
    quantidade_alunos = int(input('Quantos alunos irão fazer a prova? '))
    return quantidade_alunos


def respostas_alunos_prova(respostas, quantidade_alunos, n_questoes):
    provas = list()
    for i in range(0, quantidade_alunos):
        aluno = str(input('Nome: '))
        resposta_questao = criar_resposta_prova(respostas, n_questoes)
        turma = {'Aluno': aluno, 'Prova': resposta_questao}
        provas.append(turma)
    return provas


def correcao_prova(provas, gabarito):
    for aluno in provas:
        acertos = 0
        for i in range(0, len(aluno['Prova'])):
            if aluno['Prova'][i] == gabarito[i]:
                acertos += 1
        aluno['Nota'] = acertos
    return provas


def exibir_questao_resposta(prova_dicionario, nome):
    print('{}'.format('='*30))
    print('{}\n'.format(nome))
    for questao in prova_dicionario:
        print('{} - {}'.format(questao['Questao'], questao['Resposta']))
    print('{}'.format('='*30))


def exibir_aluno_nota(p_corrigidas):
    for aluno in p_corrigidas:
        print('Nome: {} - Nota: {}.'.format(aluno['Aluno'], aluno['Nota']))


def maior_nota_aluno(p_corrigidas):
    maior = 0
    for aluno in p_corrigidas:
        if aluno['Nota'] > maior:
            maior = aluno['Nota']
    return maior


def exibir_aluno_maior_nota(maior_nota, p_corrigidas):
    print('Maior Nota = {}.'.format(maior_nota))
    for aluno in p_corrigidas:
        if aluno['Nota'] == maior_nota:
            print('Nome: {}.'.format(aluno['Aluno']))


def media_notas_alunos(quantidade_alunos, p_corrigidas):
    soma_notas = 0
    media = 0
    for aluno in p_corrigidas:
        soma_notas += aluno['Nota']
    media = soma_notas / quantidade_alunos
    return media


def percentual_acima_media(p_corrigidas, qtd_questoes, qtd_alunos):
    media_questoes = qtd_questoes / 2
    contador_aluno = 0
    percentual = 0
    for aluno in p_corrigidas:
        if aluno['Nota'] >= media_questoes:
            contador_aluno += 1
    percentual = contador_aluno / qtd_alunos
    return percentual


def main():
    respostas = ['a', 'b', 'c', 'd', 'e']
    print("Criar Gabarito:")
    n_questoes = 5
    gabarito = criar_resposta_prova(respostas, n_questoes)
    n_alunos = quantidade_alunos()
    provas = respostas_alunos_prova(respostas, n_alunos, n_questoes)
    p_corrigidas = correcao_prova(provas, gabarito)

    # 4) a -
    exibir_aluno_nota(p_corrigidas)
    print()
    # 4) b -
    maior_nota = maior_nota_aluno(p_corrigidas)
    exibir_aluno_maior_nota(maior_nota, p_corrigidas)
    print()
    # 4) c -
    media_notas = media_notas_alunos(n_alunos, p_corrigidas)
    print('Média = {}.'.format(media_notas))
    print()
    # 4) d -
    percentual = percentual_acima_media(p_corrigidas, n_questoes, n_alunos)
    print('Percentual de aluno {}% .'.format(percentual))

main()
