import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag


def extrai_links(requisicao: requests.Response) -> list[str | None]:
	"""Recebe a resposta HTTP e retorna o 'href' de todas as tags <a> (lista vazia se não for HTML)."""

	if "html" not in requisicao.headers.get("Content-Type", "").lower():
		return []
	soup = BeautifulSoup(requisicao.text, "html.parser")
	return [str(href) if href is not None else None for a in soup.find_all("a") for href in [a.get("href")]]


def filtra_links(url: str, lista_hrefs: list[str | None]) -> list[str]:
	"""Converte os 'href' em URLs absolutas http(s), sem #fragmento e sem duplicatas."""

	resultado = []
	vistos = set()
	for href in lista_hrefs:
		if not href:
			continue
		completa, _ = urldefrag(urljoin(url, href.strip()))
		if urlparse(completa).scheme not in ("http", "https") or completa in vistos:
			continue
		vistos.add(completa)
		resultado.append(completa)
	return resultado


def acessa_url_pega_imagens(requisicao: requests.Response) -> list[str | None]:
	"""Recebe a resposta HTTP e retorna o 'src' de todas as tags <img> da página."""

	list_images_url = []

	soup = BeautifulSoup(requisicao.text, "html.parser")
	img_lists = soup.find_all("img")
	for img in img_lists:
		list_images_url.append(img.get("src"))
	#print(list_images_url)
	return list_images_url

def parser_url(url: str, lista_Urls: list[str | None]) -> list[str]:
	"""Converte os 'src' em URLs absolutas, descartando data URIs e arquivos que não sejam imagens."""
	EXTENSOES = (".jpg", ".jpeg", ".png", ".gif", ".bmp")

	#print(urlparse(url=url))
	#print(lista_Urls)
	listUrlFormatado = []
	for src in lista_Urls:
		if not src or src.startswith("data:"):
			continue
		completa  = urljoin(url, src)
		if urlparse(completa).path.lower().endswith(EXTENSOES):
			listUrlFormatado.append(completa)

	return listUrlFormatado











