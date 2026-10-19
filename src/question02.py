from pathlib import Path

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = PROJECT_ROOT / "answer02"

def power_law(path: str, gamma: float, c: float = 1):

    img = cv.imread(path, flags=cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"

    out = np.zeros(img.shape)
    cv.pow(img/255, gamma, out)
    out = np.clip(np.round(out * c * 255), 0, 255).astype(np.uint8)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cv.imwrite(str(OUT_DIR / "power-law.png"), out)


def hist_cdf(im: np.ndarray):
    """Retorna histograma e CDF normalizada [0, 1] de uma imagem 8 bits de 1 canal."""
    hist = np.bincount(im.ravel(), minlength=256)
    cdf = hist.cumsum()
    return hist, cdf / cdf[-1]


def salvar_hist(hist: np.ndarray, titulo: str, caminho: str) -> None:
    plt.figure(figsize=(7, 4))
    plt.bar(range(256), hist, width=1)
    plt.title(titulo)
    plt.xlabel("Intensidade")
    plt.ylabel("Nº de pixels")
    plt.xlim(0, 255)
    plt.tight_layout()
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(caminho, dpi=150)
    plt.close()


def salvar_cdf(cdf: np.ndarray, titulo: str, caminho: str) -> None:
    plt.figure(figsize=(7, 4))
    plt.plot(cdf)
    plt.title(titulo)
    plt.xlabel("Intensidade")
    plt.ylabel("CDF")
    plt.xlim(0, 255)
    plt.ylim(0, 1.02)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(caminho, dpi=150)
    plt.close()


def equalizar(path: str) -> None:
    
    img = cv.imread(path, flags=cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    
    
    eq = cv.equalizeHist(img)
 
    h1, c1 = hist_cdf(img)
    h2, c2 = hist_cdf(eq)
 
    salvar_hist(h1, "Histograma - original", f"{OUT_DIR}/hist_original.png")
    salvar_cdf(c1, "CDF - original", f"{OUT_DIR}/cdf_original.png")
    salvar_hist(h2, "Histograma - equalizado", f"{OUT_DIR}/hist_equalizado.png")
    salvar_cdf(c2, "CDF - equalizada", f"{OUT_DIR}/cdf_equalizada.png")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cv.imwrite(str(OUT_DIR / "imagem_equalizada.png"), eq)
    
if __name__ == '__main__':
    imagem = str(PROJECT_ROOT / "images" / "car.png")
    power_law(imagem, 0.5, 1)
    equalizar(imagem)
