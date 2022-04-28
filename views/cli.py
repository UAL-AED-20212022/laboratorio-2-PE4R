import controllers.controller as controller

def comando(inst, lista):
    if inst[0]=='RPI' and len(inst)==2: #Registar Pais no Inicio da Lista (RPI pais_novo)
        controller.rpi(lista, inst[1])
        lista.traverse_list()
        return 

    if inst[0]=='RPF' and len(inst)==2: #Registar Pais no Final da Lista (RPF pais_novo)
        controller.rpf(lista, inst[1])
        lista.traverse_list()
        return

    if inst[0]=='RPDE' and len(inst)==3: #Registar Pais Depois de um Existente (RPDE pais_novo pais_indicado)
        controller.rpde(lista, inst[1], inst[2])
        lista.traverse_list()
        return

    if inst[0]=='RPAE' and len(inst)==3: #Registar Pais Antes de um Existente (RPAE pais_novo pais_indicado)
        controller.rpae(lista, inst[1], inst[2])
        lista.traverse_list()
        return
    
    if inst[0]=='RPII' and len(inst)==3: #Registar Pais num Indice determinado (RPII pais_novo indice)
        controller.rpii(lista, inst[1], inst[2])
        lista.traverse_list()
        return
    
    if inst[0]=='VNE' and len(inst)==1: #Verificar Número de Elementos da lista (VNE)
        temp=controller.vne(lista)
        return f"O número de elementos são {temp}."

    if inst[0]=='VP' and len(inst)==2: #Verificar se um País se encontra na lista (VP pais)
        temp=controller.vp(lista, inst[1])
        if temp[1]==True:
            return f"O país {temp[0]} encontra-se na lista."
        return f"O país {temp[0]} não se encontra na lista."

    if inst[0]=='EPE' and len(inst)==1: #Eliminar Primeiro Elemento da lista (EPE)
        temp=controller.epe(lista)
        return f"O país {temp} foi eliminado da lista."
    
    if inst[0]=='EUE' and len(inst)==1: #Eliminar Último Elemento da lista (EUE)
        temp=controller.eue(lista)
        return f"O país {temp} foi eliminado da lista."
    
    if inst[0]=='EP' and len(inst)==2: #Eliminar País indicado (EP pais)
        temp=controller.ep(lista, inst[1])
        if temp[1]==True:
            return f"O país {temp[0]} foi eliminado da lista."
        return f"O país {temp[0]} não se encontra na lista."
    
def main():
    lista = controller.LinkedList()
    while True:
        inserir = input()
        temp = comando(inserir.split(), lista)
        if temp is not None:
            print(temp)