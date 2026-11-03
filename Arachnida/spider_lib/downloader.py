from .utils import nome_do_arquivo, nome_unico
from urllib.parse import urlparse
from pathlib import  Path
import requests
import os
import hashlib



def _hash_arquivo(caminho: str) -> str:
	"""Retorna o SHA-256 do conteúdo de um arquivo."""
	h = hashlib.sha256()
	with open(caminho, "rb") as f:
		for bloco in iter(lambda: f.read(8192), b""):
			h.update(bloco)
	return h.hexdigest()


def baixa_imagem(url : str, path: str):
	"""Baixa a imagem da url para a pasta. Nomes iguais com conteúdo diferente
	ganham um hash no nome; conteúdo idêntico a um arquivo existente é descartado."""

	nome_arquivo = nome_do_arquivo(url)
	if nome_arquivo is None:
		return False

	temporario = os.path.join(path, f".{nome_unico(url, nome_arquivo)}.part")
	try :
		with requests.get(url, stream=True, timeout=15) as resposta:
			resposta.raise_for_status()

			tipo_conteudo = resposta.headers.get("Content-Type", "")
			if "image" not in tipo_conteudo:
				print(f"❌ Ignorado: {url} não parece ser uma imagem válida.")
				return False

			with open(temporario, "wb") as arquivo:
				for bloco in resposta.iter_content(chunk_size=8192):
					arquivo.write(bloco)

		# Escolhe o destino: nome original -> nome com hash -> descarta se for igual
		novo_hash = _hash_arquivo(temporario)
		for nome in (nome_arquivo, nome_unico(url, nome_arquivo)):
			destino = os.path.join(path, nome)
			if not os.path.exists(destino):
				os.replace(temporario, destino)
				print(f"✅ Baixada com sucesso: {destino}")
				return True
			if _hash_arquivo(destino) == novo_hash:
				print(f"⏭️  Já baixada (conteúdo idêntico): {destino}")
				return True
		print(f"⏭️  Já baixada: {destino}")
		return True

	except (requests.exceptions.RequestException, OSError) as e:
		print(f"💥 Erro ao baixar {url}: {e}")
		return False
	finally:
		if os.path.exists(temporario):
			os.remove(temporario)

	return

