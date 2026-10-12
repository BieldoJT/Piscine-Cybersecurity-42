import argparse
from pathlib import Path


DEPTH_RECURSIVE = 5
DEFAULT_PATH = "./data/"

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

#Verifica se o path é valido, caso contrário, cria o .data
if args.path is None:
	args.path = DEFAULT_PATH
	Path(args.path).mkdir(parents=True, exist_ok=True)
elif not Path(args.path).is_dir():
	parser.error("Must specify a valid PATH")


# BLOCO DE TESTES DO ARGS
#print(f"Recursive é {args.recursive}")
#if(args.level):
#	print(f"level é {args.level}")
#if(args.path):
#	print(f"path é {args.path}")
#if(args.URL):
#	print(f"url é {args.URL}")
