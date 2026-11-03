import requests
from bs4 import BeautifulSoup

#pega links de uma pagina html
def pega_links(requisicao : requests.Response):

	lista_links_url = []
	soup = BeautifulSoup(requisicao.text, "html.parser")
	a_lists = soup.find_all("a")
	for a in a_lists:
		lista_links_url.append(a.get("href"))

	return lista_links_url

#  fazer a verificação no looping pra fazer a criação da fila de links (BFS)

