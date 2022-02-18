from requests import get
from json import loads


def obtener_palabra(caracteres: int) -> str:
    """
    Esta función utiliza la API 'Palabras aleatorias' para generar una palabra con determinado número de caracteres.\n
    caracteres: número de caracteres que debe tener la palabra a generar.\n
    Retorna un string en mayúsculas."""
    url = f'https://palabras-aleatorias-public-api.herokuapp.com/random-by-length?length={caracteres}'
    return loads(get(url).text)['body']['Word'].upper()



if __name__ == '__main__':
    caracteres = 5
    print(obtener_palabra(caracteres))