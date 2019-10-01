import sys
try:
    from PIL import Image
except ImportError:
    print("Please install Pillow from: https://pypi.python.org/pypi/Pillow/3.0.0")
    sys.exit(1)


def main(argv=[__name__]):

    if len(sys.argv) != 4:
        print("Usage %s <image> <logoimage> <outimage>" % argv[0])
        return 1

    inimage, logo, outimage = sys.argv[1], sys.argv[2], sys.argv[3]
    add_logo(inimage, logo, outimage)

    return 0


def add_logo(mfname, lfname, outfname):

    mimage = Image.open(mfname)
    limage = Image.open(lfname)

    # resize logo
    wsize = int(min(mimage.size[0], mimage.size[1]) * 0.25)
    wpercent = (wsize / float(limage.size[0]))
    hsize = int((float(limage.size[1]) * float(wpercent)))

    simage = limage.resize((wsize, hsize))
    mbox = mimage.getbbox()
    sbox = simage.getbbox()

    # right bottom corner
    box = (mbox[2] - sbox[2], mbox[3] - sbox[3])
    mimage.paste(simage, box)
    mimage.save(outfname)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
