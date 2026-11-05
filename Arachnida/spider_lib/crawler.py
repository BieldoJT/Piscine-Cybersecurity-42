from collections import deque
from urllib.parse import urlparse

from .fetcher import requisicao_url
from .parser import acessa_url_pega_imagens, parser_url, extrai_links, filtra_links
from .downloader import baixa_imagem


def rastreia(url_inicial: str, nivel_max: int, path: str) -> list[str]:
	"""Percorre o site em largura (BFS) a partir de url_inicial, baixando as imagens de cada página.
	nivel_max = quantos níveis de links seguir além da página inicial (0 = só a inicial).
	Só segue links do mesmo domínio e nunca visita a mesma página nem baixa a mesma imagem duas vezes.
	Retorna a lista de URLs de imagens encontradas."""

	dominio = urlparse(url_inicial).netloc
	paginas_vistas = {url_inicial}
	imagens_vistas: set[str] = set()
	imagens_encontradas: list[str] = []
	fila = deque([(url_inicial, 0)])

	while fila:
		url_atual, profundidade = fila.popleft()
		print(f"🕷️  [nível {profundidade}] {url_atual}")

		requisicao = requisicao_url(url_atual)
		if requisicao is None:
			continue  # página inacessível: segue a fila em vez de abortar tudo

		imagens = parser_url(url_atual, acessa_url_pega_imagens(requisicao))
		for imagem in imagens:
			if imagem in imagens_vistas:
				continue
			imagens_vistas.add(imagem)
			imagens_encontradas.append(imagem)
			baixa_imagem(imagem, path)

		if profundidade >= nivel_max:
			continue

		for link in filtra_links(url_atual, extrai_links(requisicao)):
			if urlparse(link).netloc != dominio or link in paginas_vistas:
				continue
			paginas_vistas.add(link)
			fila.append((link, profundidade + 1))

	return imagens_encontradas
