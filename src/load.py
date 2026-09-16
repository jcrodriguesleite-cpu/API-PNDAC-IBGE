class Load:
    def __init__(self):
        pass

        """
        Método de extração de dados do PNADC

        Atributos:
            nome_arquivo: string
            data: list (resultado do request na api do IBGE)
        """

    def load_json(self, nome_arquivo, data:list):
        with open(f'{nome_arquivo}.json','w',encoding='utf-8') as f:
            f.write(str(data))
