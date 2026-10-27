from urllib.parse import urlparse
from pathlib import PurePosixPath

EXTENSOES = (".jpg", ".jpeg", ".png", ".gif", ".bmp")


def nome_do_arquivo(url: str) -> str | None:
    """Retorna o nome do arquivo se a URL terminar com uma extensão de imagem válida."""
    caminho = urlparse(url).path  # ignora ?query e #fragment
    nome = PurePosixPath(caminho).name

    if nome.lower().endswith(EXTENSOES):
        return nome
    return None
