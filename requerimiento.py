from requests import get
from json import loads


def obtener_palabra(caracteres: int) -> str:
    """
    Esta función utiliza la API 'Palabras aleatorias' para generar una palabra con determinado número de caracteres.\n
    caracteres: número de caracteres que debe tener la palabra a generar.\n
    Retorna un string en mayúsculas.
    """
    url = f'https://palabras-aleatorias-public-api.herokuapp.com/random-by-length?length={caracteres}'
    return loads(get(url).text)['body']['Word'].upper()


def genera_lista(palabras: int, caracteres: int) -> list:
    """
    Esta función genera una lista de palabras, todas con la misma cantidad de caracteres, sin tilde.\n
    palabras: número de palabras que integrarán la lista.
    caracteres: número de caracteres que debe tener cada palabra.\n
    Retorna una lista con palabras, en orden alfabético.
    """
    lista = set()
    while len(lista) < palabras:
        candidato = obtener_palabra(caracteres)
        prohibido = ['Á', 'É', 'Í', 'Ó', 'Ú']
        for letra in prohibido:
            if letra in candidato:
                candidato = 'anulado'
        lista.add(candidato) if candidato != 'anulado' else None         
    return sorted(lista)



if __name__ == '__main__':
    caracteres = 5
    print(obtener_palabra(caracteres))

    lista = genera_lista(10, 4)
    print(lista)