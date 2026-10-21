from .cli import validar_input
from .parser import acessa_url_pega_imagens, parser_url

def main():
	args = validar_input()
	lista_urls = acessa_url_pega_imagens(args.URL)
	lista = parser_url(args.URL, lista_urls)
	print("RODEI")
	print(lista)
