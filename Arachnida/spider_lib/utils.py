from urllib.parse import urlparse
from pathlib import PurePosixPath, Path

EXTENSOES = (".jpg", ".jpeg", ".png", ".gif", ".bmp")


def nome_do_arquivo(url: str) -> str | None:
	"""Retorna o nome do arquivo se a URL terminar com uma extensão de imagem válida."""
	caminho = urlparse(url).path  # ignora ?query e #fragment
	nome = PurePosixPath(caminho).name
	if nome.lower().endswith(EXTENSOES):
		return nome
	return nome

def cria_pasta(nome_pasta : str) -> None:
	"""Cria a pasta com o nome passado como parâmetro."""
	Path(nome_pasta).mkdir(parents=True, exist_ok=True)
