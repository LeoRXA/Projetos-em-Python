import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    list_sub=[]
    soma=0
    for i in range(len(as_a)):
        subtração=as_a[i]-as_b[i]
        list_sub.append(abs(subtração))  
    for i in range(len(list_sub)):
        soma=list_sub[i]+soma
    ass=soma/6
    return ass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura=[]
    #Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    list_fr=[]
    list_sent=separa_sentencas(texto)
    list_palavras=[]
    list_n_word=[]
    soma_letter=0
    for sent in list_sent:
        novas_frases=separa_frases(sent)
        list_fr.extend(novas_frases)
    for fr in list_fr:
        palavras=separa_palavras(fr)
        list_palavras.extend(palavras)
    max_word=len(list_palavras)
    for n_word in list_palavras:
        list_n_word.append(len(n_word))
    min_letter=0
    while min_letter<(len(list_n_word)):
        soma_letter=soma_letter+list_n_word[min_letter]
        min_letter=min_letter+1
    media_total=soma_letter/max_word
    assinatura.append(media_total)
    #Relação Type-Token
    list_word_diferente=n_palavras_diferentes(list_palavras)
    typetoken=list_word_diferente/max_word
    assinatura.append(typetoken)
    #Razão Hapax Legomana
    list_word_unica=n_palavras_unicas(list_palavras)
    hapax_legomana=list_word_unica/max_word
    assinatura.append(hapax_legomana)
    #Tamanho médio de sentença
    max_caracteres=[]
    for sent in list_sent:
        max_caracteres.append(len(sent))
    soma_sent=0
    min_sent=0
    while min_sent<len(max_caracteres):
        soma_sent=soma_sent + max_caracteres[min_sent]
        min_sent=min_sent+1
    media_sent=soma_sent/(len(list_sent))
    assinatura.append(media_sent)
    #Complexidade de sentença
    media_sent_fr=len(list_fr)/len(list_sent)
    assinatura.append(media_sent_fr)
    #Tamanho médio de frase
    max_carac_fr=[]
    for fr in list_fr:
        max_carac_fr.append(len(fr))
    soma_fr=0
    min_fr=0
    while min_fr<len(max_carac_fr):
        soma_fr=soma_fr + max_carac_fr[min_fr]
        min_fr=min_fr+1
    media_fr=soma_fr/(len(list_fr))
    assinatura.append(media_fr)
    return assinatura

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    list_comp=[]
    textos_1=textos
    for texto in textos_1:
        assinatura=calcula_assinatura(texto)
        comparador=compara_assinatura(assinatura,ass_cp)
        list_comp.append(comparador)
    for comp in list_comp:
        if comp==min(list_comp):
            indice=list_comp.index(comp)
    return indice+1
def main():
    assinatura_comp=le_assinatura()
    textos_totais=le_textos()
    avaliador=avalia_textos(textos_totais,assinatura_comp)
    print("O autor do texto",avaliador,"está infectado com COH-PIAH")
main()