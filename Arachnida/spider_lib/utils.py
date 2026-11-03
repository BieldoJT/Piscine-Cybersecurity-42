from urllib.parse import urlparse, unquote
from pathlib import PurePosixPath, Path
import hashlib
import os

EXTENSOES = (".jpg", ".jpeg", ".png", ".gif", ".bmp")


def nome_do_arquivo(url: str) -> str | None:
	"""Retorna o nome do arquivo se a URL terminar com uma extensão de imagem válida."""
	caminho = urlparse(url).path  # ignora ?query e #fragment
	nome = PurePosixPath(unquote(caminho)).name
	if nome.lower().endswith(EXTENSOES):
		return nome
	return None


def nome_unico(url: str, nome: str) -> str:
	"""Acrescenta um hash curto da URL ao nome (foto.jpg -> foto_a1b2c3d4.jpg).
	URLs diferentes geram nomes diferentes; a mesma URL gera sempre o mesmo nome."""
	hash_url = hashlib.sha1(url.encode()).hexdigest()[:8]
	base, ext = os.path.splitext(nome)
	return f"{base}_{hash_url}{ext}"

def cria_pasta(nome_pasta : str) -> None:
	"""Cria a pasta com o nome passado como parâmetro."""
	Path(nome_pasta).mkdir(parents=True, exist_ok=True)
