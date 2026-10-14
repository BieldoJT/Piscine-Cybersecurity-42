## 📐 Estrutura de Responsabilidades dos Módulos

| Módulo | Responsabilidade | Não deve |
| :--- | :--- | :--- |
| **cli** | Ler e validar argumentos, devolver algo estruturado | Fazer requisições |
| **fetcher** | Buscar uma URL e devolver o conteúdo (ou falhar de forma controlada) | Interpretar HTML |
| **parser** | Receber HTML + URL base e devolver listas de URLs absolutas (imagens e links) | Acessar a rede ou o disco |
| **downloader** | Receber uma URL de imagem e uma pasta, e gravar o arquivo | Decidir o que baixar |
| **crawler** | Orquestrar: quem visitar, em que profundidade, o que já foi visto | Saber detalhes de HTTP ou de HTML |

### Criar a venv
- python3 -m venv .venv
### Pra abrir a .venv
- source .venv/bin/activate
### Pra desativar a venv
- deactivate



### Forma que o input do spider funciona
- ./spider [-r] [-l N] [-p PATH] URL

### Onde altera o codigo?
- a main está no __init__.py, o executavel só roda o esse arquivo agora
- Sempre que adicionar algo novo, colocar no __init__


##### Pra testar
- https://books.toscrape.com/
