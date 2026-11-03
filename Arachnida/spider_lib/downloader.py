from .utils import nome_do_arquivo
from urllib.parse import urlparse
from pathlib import  Path
import requests
import os
import shutil


#Path(args.path).mkdir(parents=True, exist_ok=True)



def baixa_imagem(url : str, path: str):
	"""Recebe uma url e a pasta baixa um arquivo"""

	nome_arquivo = nome_do_arquivo(url)
	if nome_arquivo is None:
		return
	destino = os.path.join(path, nome_arquivo)

	try :
		with requests.get(url, stream=True, timeout=15) as resposta:
			resposta.raise_for_status()

			tipo_conteudo = resposta.headers.get("Content-Type", "")
			if "image" not in tipo_conteudo:
				print(f"❌ Ignorado: {url} não parece ser uma imagem válida.")

			with open(destino, "wb") as arquivo:
				shutil.copyfileobj(resposta.raw, arquivo)
			print(f"✅ Baixada com sucesso: {destino}")
			return True

	except requests.exceptions.RequestException as e:
			print(f"💥 Erro ao baixar {url}: {e}")
			return False

#	# --- EXEMPLO DE USO EM LOTE ---
#urls_imagens = [
#    "https://unsplash.com",  # Imagem normal
#    "https://wikimedia.org",  # Formato pesado
#]
#
#for url in urls_imagens:
#    baixar_imagem_segura(url, pasta_destino="imagens_baixadas")







	return

