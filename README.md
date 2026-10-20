# Processamento de Imagens

Projeto de processamento digital de imagens com implementações em Python e um
notebook demonstrativo. O projeto aborda ampliação de imagens, super-resolução,
transformação power-law (correção gamma), equalização de histograma e análise
de histogramas e CDFs.

## Estrutura

```text
.
├── answer01/          # Resultados da questão 1
├── answer02/          # Resultados da questão 2
├── images/            # Imagens de entrada
├── test_images/       # Imagens de teste
├── src/
│   ├── gerar_imagem_teste.py
│   ├── converter_jpg_para_png.py
│   ├── question01.py
│   └── question02.py
├── main.ipynb         # Notebook com explicações, código e visualizações
└── requirements.txt
```

Os scripts resolvem os caminhos a partir da raiz do projeto, portanto podem ser
executados de qualquer diretório. As pastas de dados e resultados permanecem na
raiz.

## Requisitos e instalação

É necessário ter Python 3 e `pip` instalados. Recomenda-se criar um ambiente
virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

No Windows, ative o ambiente com:

```powershell
.venv\Scripts\Activate.ps1
```

## Como executar

Na raiz do projeto, execute os scripts:

```bash
python src/question01.py
python src/question02.py
python src/gerar_imagem_teste.py
```

- `question01.py` contém as funções `TAM2`, `TAMM` e `SUPERRES`. Ao executar o
  script, a super-resolução é aplicada às imagens `fruit01.png` e `fruit02.png`,
  e o resultado é salvo em `answer01/superres.png`.
- `question02.py` aplica a transformação power-law com `gamma=0.5` e equaliza
  `car.png`, salvando imagens e gráficos em `answer02/`.
- `gerar_imagem_teste.py` gera uma imagem 4×4 em
  `test_images/teste_4x4_2.png`.

Para executar o material completo, abra `main.ipynb` no Jupyter ou no VS Code e
execute suas células em ordem. O notebook demonstra os testes das duas questões
e salva os resultados nas pastas `answer01/` e `answer02/`.

## Entradas e resultados

As imagens de entrada estão em `images/` e `test_images/`. Os resultados da
questão 1 são organizados em subpastas de `answer01/`; os da questão 2 ficam em
`answer02/`, incluindo transformações power-law candidatas, imagens equalizadas
e gráficos de histogramas e CDFs quando o notebook é executado.
