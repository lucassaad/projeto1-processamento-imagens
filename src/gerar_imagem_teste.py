from pathlib import Path

import cv2 as cv
import numpy as np


def main() -> None:
    imagem = np.zeros((4, 4, 3), dtype=np.uint8)

    for y in range(4):
        for x in range(4):
            imagem[y, x] = (x * 40, y * 30, 255 - x * 10)

    raiz_projeto = Path(__file__).resolve().parent.parent
    caminho = raiz_projeto / "test_images" / "teste_4x4_2.png"
    caminho.parent.mkdir(parents=True, exist_ok=True)

    if not cv.imwrite(str(caminho), imagem):
        raise RuntimeError(f"Não foi possível salvar a imagem em {caminho}")

    print(f"Imagem 4x4 salva em: {caminho}")
    print("Matriz (4 linhas x 4 colunas):")
    print(imagem)


if __name__ == "__main__":
    main()
