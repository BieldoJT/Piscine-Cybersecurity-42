from .cli import validar_input
from .parser import acessa_url_pega_imagens, parser_url
from .fetcher import requisicao_url


def main() -> None:
	"""Ponto de entrada: valida os argumentos, busca a página e lista as URLs de imagens encontradas."""
	args = validar_input()
	requisao = requisicao_url(args.URL)
	if requisao is None:
		raise RuntimeError("Não foi possível obter a resposta da URL")
	lista_urls = acessa_url_pega_imagens(requisao)
	lista = parser_url(args.URL, lista_urls)
	print("RODEI")
	print(lista)
