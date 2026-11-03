import argparse
from pathlib import Path
from .utils import cria_pasta


DEPTH_RECURSIVE = 5
DEFAULT_PATH = "./data/"

def validar_input() -> argparse.Namespace:
	"""Lê e valida os argumentos da linha de comando (-r, -l, -p e URL) e retorna o namespace do argparse."""

	# Iniciar o argparse
	parser = argparse.ArgumentParser(description="Download images from a website recursivily")

	# Define os argumentos
	parser.add_argument("-r", "--recursive", action="store_true", help="flag to the program be recursive")
	parser.add_argument("-l","--level", type=int, default=None, help="depth recursion")
	parser.add_argument("-p", "--path", type=str, default=None, help="Path of the download")
	parser.add_argument("URL")

	# Recebe os input do usuario
	args = parser.parse_args()

	#Verifica se colocou o level sem o recursive
	if args.level is not None and args.recursive is False:
		parser.error("Must specify --recursive [-r] if --level [-l] is used")
	if args.level is None:
		args.level = DEPTH_RECURSIVE

	#Usa o path padrão se não foi informado; cria a pasta se ela não existir
	if args.path is None:
		args.path = DEFAULT_PATH
	if Path(args.path).exists() and not Path(args.path).is_dir():
		parser.error(f"PATH '{args.path}' exists but is not a directory")
	try:
		cria_pasta(args.path)
	except OSError as e:
		parser.error(f"Could not create PATH '{args.path}': {e}")

	return args


	# BLOCO DE TESTES DO ARGS
	#print(f"Recursive é {args.recursive}")
	#if(args.level):
	#	print(f"level é {args.level}")
	#if(args.path):
	#	print(f"path é {args.path}")
	#if(args.URL):
	#	print(f"url é {args.URL}")
