import cv2 as cv
import numpy as np

OUTPUT_DIR = 'answer01/'

def TAM2(path: str, scale: int):

    img = cv.imread(path)
    assert img is not None, "file could not be read, check with os.path.exists()"

    H, W, _ = img.shape

    new_H = H * scale
    new_W = W * scale
    out = np.zeros((new_H, new_W, 3), dtype=img.dtype)

    for i in range(new_H):
        for j in range(new_W):
            source_x = j * W // new_W
            source_y = i * H // new_H

            out[i][j] = img[source_y][source_x]

    cv.imwrite(f'{OUTPUT_DIR}tam2.png', out)

def TAMM(path: str):

    img = cv.imread(path)
    assert img is not None, "file could not be read, check with os.path.exists()"

    H, W, _ = img.shape
    new_H = H * 2
    new_W = W * 2
    out = np.zeros((new_H, new_W, 3), dtype=img.dtype)

    for i in range(0,new_H, 2):
        for j in range(0,new_W,2):
            out[i][j] = img[i//2][j//2]
    cv.imwrite(f'{OUTPUT_DIR}tamm_step1.png', out)

    # linhas 
    for i in range(0,new_H,2):
        for j in range(1,new_W,2):
            if (j + 1) >= new_W:
                out[i][j] = img[i//2][j//2]
                continue
            prev = img[i//2][(j//2)]
            successor = img[i//2][(j//2) + 1]
            mean = (prev.astype(np.uint16) + successor.astype(np.uint16) + 1) // 2

            out[i][j] = mean.astype(np.uint8)   
    cv.imwrite(f'{OUTPUT_DIR}tamm_step2.png', out)

    # colunas
    for i in range(1,new_H,2):
        for j in range(0,new_W):
            if (i + 1) >= new_H:
                out[i][j] = out[i-1][j]
                continue
            prev = out[i-1][j]
            successor = out[i+1][j]
            mean = (prev.astype(np.uint16) + successor.astype(np.uint16) + 1) // 2

            out[i][j] = mean.astype(np.uint8)   
            
    cv.imwrite(f'{OUTPUT_DIR}tamm_step3.png', out)

def SURPERRES(path1: str, path2: str):
    img1 = cv.imread(path1)
    assert img1 is not None, "img1 could not be read, check with os.path.exists()"
    img2 = cv.imread(path2)
    assert img2 is not None, "img2 could not be read, check with os.path.exists()"

    assert img1.shape == img2.shape, "images are not compatible"

    H, W, _ = img1.shape
    new_H = H*2
    new_W = W*2
    out = np.zeros((new_H, new_W, 3), dtype=img1.dtype)

    for i in range(new_H):
        for j in range(new_W):
            if i % 2 == 0 and j % 2 == 0:
                out[i][j] = img1[i//2][j//2]
            if i % 2 == 1 and j % 2 == 1:
                out[i][j] = img2[i//2][j//2]

    cv.imwrite(f"{OUTPUT_DIR}superres.png", out)


if __name__ == "__main__":


    path = "images/fruit01.png"
    path2 = "images/fruit02.png"
    TAM2(path, 8)
    TAMM(path)
    SURPERRES(path, path2)
