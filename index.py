from PIL import Image
import imagehash
import argparse
import shelve
import glob

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset of images")
ap.add_argument("-s", "--shelve", required=True, help="output dataset")
args = vars(ap.parse_args())

db = shelve.open(args["shelve"], writeback=True)

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
    image = Image.open(imagePath)
    h = str(imagehash.dhash(image))
    filename = imagePath[imagePath.rfind("/") + 1:]
    db[h] = db.get(h, []) + [filename]

db.close()
