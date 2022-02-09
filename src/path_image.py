import os

def take_path(folder): 
    path = os.getcwd() 
    os.chdir(path)
    return os.path.abspath(folder)

def take_image(path):
    lista = []
    for _, _, arquivo in os.walk(path):
        lista.append(arquivo)
    return lista

def make_path(path, lista):
    output = []
    for item in lista[0]:
        output.append(os.path.join(path, item))
    return output
