import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, Timeout


def acessa_url_pega_imagens(url : str):

	list_images_url = []
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
		#leitor do html
		soup = BeautifulSoup(requisicao.text, "html.parser")

		img_lists = soup.find_all("img")
		for img in img_lists:
			list_images_url.append(img.get("src"))
		print(list_images_url)
		return list_images_url





