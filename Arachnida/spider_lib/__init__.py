from .cli import validar_input
from .crawler import rastreia


def main() -> None:
	"""Ponto de entrada: valida os argumentos e baixa as imagens (da página, ou do site todo com -r)."""

	args = validar_input()

	# sem -r só a página informada; com -r segue links até o nível -l
	nivel_max = args.level if args.recursive else 0
	imagens = rastreia(args.URL, nivel_max, args.path)

	print(f"Total de imagens encontradas: {len(imagens)}")
