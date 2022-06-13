from PIL import Image
from PIL import ExifTags
import sys

def main(fnames):
    for fname in fnames[1:]:
        im = Image.open(fname)
        name = fname.split('.')[0]
        ext  = fname.split('.')[1]
        width, height = im.size
        for s in [2, 1.5, 0.5, 0.25, 0.125]:
            dimension = (int(width*s), int(height*s))
            new_im = im.resize(dimension, Image.NEAREST)
            new_im.save(f"./out/exec2-{name}-{s}.{ext}")
main(sys.argv)