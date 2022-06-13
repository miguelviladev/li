from PIL import Image
from PIL import ExifTags
import sys

def main(fnames):
    print("1 - Nearest")
    print("2 - Bilinear")
    print("3 - Bicubic")
    print("4 - Antialias")
    print("Metodo de processamento:")
    metodo = int(input())
    if metodo == 1:
        metodo = Image.NEAREST
    elif metodo == 2:
        metodo = Image.BILINEAR
    elif metodo == 3:
        metodo = Image.BICUBIC
    elif metodo == 4:
        metodo = Image.ANTIALIAS
    else:
        print("Metodo inválido")
        return

    for fname in fnames[1:]:
        im = Image.open(fname)
        name = fname.split('.')[0]
        ext  = fname.split('.')[1]
        width, height = im.size
        for s in [2, 1.5, 0.5, 0.25, 0.125]:
            dimension = (int(width*s), int(height*s))
            new_im = im.resize(dimension, metodo)
            new_im.save(f"./out/exec2-{name}-{s}.{ext}")
main(sys.argv)