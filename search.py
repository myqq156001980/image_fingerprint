from PIL import Image
import imagehash
import argparse
import shelve

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset of images")
ap.add_argument("-s", "--shelve", required=True, help="output dataset")
ap.add_argument("-q", "--query", required=True, help="path to query image")
args = vars(ap.parse_args())

db = shelve.open(args["shelve"])

query = Image.open(args["query"])
h = str(imagehash.dhash(query))
filenames = db[h]
print("Found {0} images".format(len(filenames)))

for filename in filenames:
    image = Image.open(args["dataset"] + "/" + filename)
    image.show()

db.close()
