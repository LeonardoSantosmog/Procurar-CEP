import requests  # Biblioteca para fazer requisições HTTP

def buscar_cep(cep: str) -> dict:
    # Faz a requisição GET para a API com o CEP informado
    if cep.isnumeric and len(cep) == 8:
        resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
        return resposta.json()
    raise ValueError("somente permitidos CEPs numericos com 8 digitos")

