import requests

siglas_estados = {
    "AC": "Acre",
    "AL": "Alagoas",
    "AP": "Amapá",
    "AM": "Amazonas",
    "BA": "Bahia",
    "CE": "Ceará",
    "DF": "Distrito Federal",
    "ES": "Espírito Santo",
    "GO": "Goiás",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "MS": "Mato Grosso do Sul",
    "MG": "Minas Gerais",
    "PA": "Pará",
    "PB": "Paraíba",
    "PR": "Paraná",
    "PE": "Pernambuco",
    "PI": "Piauí",
    "RJ": "Rio de Janeiro",
    "RN": "Rio Grande do Norte",
    "RS": "Rio Grande do Sul",
    "RO": "Rondônia",
    "RR": "Roraima",
    "SC": "Santa Catarina",
    "SP": "São Paulo",
    "SE": "Sergipe",
    "TO": "Tocantins"
}

def obter_clima(estado, api_key):
    estado_nome = siglas_estados.get(estado.upper(), estado)
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={estado_nome},BR&appid={api_key}&units=metric&lang=pt_br"
    
    resposta = requests.get(url)
    dados = resposta.json()
    
    if resposta.status_code == 200:
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        return f"A temperatura em {estado_nome} é de {temperatura}°C com {descricao}."
    else:
        return "Não foi possível obter os dados de clima. Verifique o nome do estado e tente novamente."

def main():
    estado = input("Digite o nome ou a sigla do seu estado: ")
    api_key = ''  # Substitua pela sua chave de API Do https://openweathermap.org
    print(obter_clima(estado, api_key))

if __name__ == "__main__":
    main()
