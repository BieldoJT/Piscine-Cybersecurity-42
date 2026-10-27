import requests
from requests.exceptions import HTTPError, Timeout


def requisicao_url(url: str) -> requests.Response | None:
	"""Faz o GET na URL e retorna a resposta; em caso de erro imprime a mensagem e retorna None."""

	try:
		#timeout -> um numero -> tempo em segundos
		#		 -> tupla     -> Tempo (tempo pra conectar, tempo pra receber os dados)
		requisicao = requests.get(url, timeout=(10,10))
	except HTTPError as httpError:
		print(f"HTTP Error ocurred: {httpError}")
	except Timeout:
		print("Time out of the request")
	except Exception as e:
		print(f"Error ocurred: {e}")
	else:
		#print(list_images_url)
		return requisicao
