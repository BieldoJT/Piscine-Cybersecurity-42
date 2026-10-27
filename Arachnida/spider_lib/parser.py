from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


def acessa_url_pega_imagens(requisicao):

	list_images_url = []

	soup = BeautifulSoup(requisicao.text, "html.parser")
	img_lists = soup.find_all("img")
	for img in img_lists:
		list_images_url.append(img.get("src"))
	#print(list_images_url)
	return list_images_url

def parser_url(url: str, lista_Urls):
	EXTENSOES = (".jpg", ".jpeg", ".png", ".gif", ".bmp")

	print(urlparse(url=url))
	#print(lista_Urls)
	listUrlFormatado = []
	for src in lista_Urls:
		if not src or src.startswith("data:"):
			continue
		completa  = urljoin(url, src)
		if urlparse(completa).path.lower().endswith(EXTENSOES):
			listUrlFormatado.append(completa)

	return listUrlFormatado











