from .cli import validar_input
from .fetcher import acessa_url_pega_imagens

def main():
	args = validar_input()
	lista_urls = acessa_url_pega_imagens(args.URL)
	#print("RODEI")
	#print(args)
