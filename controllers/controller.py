from models.LinkedList import LinkedList

def rpi(lista, pais_novo):
    lista.insert_at_start(pais_novo)
    return

def rpf(lista, pais_novo):
    lista.insert_at_end(pais_novo)
    return

def rpde(lista, pais_novo, pais_indicado):
    lista.insert_after_item(pais_novo, pais_indicado)
    return

def rpae(lista, pais_novo, pais_indicado):
    lista.insert_before_item(pais_novo, pais_indicado)
    return

def rpii(lista, pais_novo, indice):
    lista.insert_at_index(int(indice), pais_novo)
    return

def vne(lista):
    return lista.get_count()

def vp(lista, pais):
    if lista.search_item() == True:
        return pais, True
    return pais, False

def epe(lista):
    lista.reverse_linkedlist()
    pais=lista.get_last_node()
    lista.reverse_linkedlist()
    lista.delete_at_start()
    return pais

def eue(lista):
    pais=lista.get_last_node()
    lista.delete_at_end()
    return pais

def ep(lista, pais):
    temp = vp(lista, pais)
    if temp[1]==True:
        lista.delete_element_by_value(pais)
        return pais, True
    return pais, False
    