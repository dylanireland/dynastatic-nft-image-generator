from PIL import Image
from os import walk
from enum import Enum
import random

def generateImages():
    total = 100
    for i in range(total):
        commonDirectory = getColorPath(randomColorIndex())

        background = Image.open(getPath(commonDirectory, Layer.BACKGROUND, randomIndex(commonDirectory, Layer.BACKGROUND)))
        spikes = Image.open(getPath(commonDirectory, Layer.SPIKES, randomIndex(commonDirectory, Layer.SPIKES)))
        wings = Image.open(getPath(commonDirectory, Layer.WINGS, randomIndex(commonDirectory, Layer.WINGS)))
        base = Image.open(getPath(commonDirectory, Layer.BASE, randomIndex(commonDirectory, Layer.BASE)))
        taltips = Image.open(getPath(commonDirectory, Layer.TAILTIPS, randomIndex(commonDirectory, Layer.TAILTIPS)))
        mouth = Image.open(getPath(commonDirectory, Layer.MOUTH, randomIndex(commonDirectory, Layer.MOUTH)))
        eyes = Image.open(getPath(commonDirectory, Layer.EYES, randomIndex(commonDirectory, Layer.EYES)))

        background.paste(spikes, (0, 0), spikes.convert('RGBA'))
        background.paste(wings, (0, 0), wings.convert('RGBA'))
        background.paste(base, (0, 0), base.convert('RGBA'))
        background.paste(taltips, (0, 0), taltips.convert('RGBA'))
        background.paste(mouth, (0, 0), mouth.convert('RGBA'))
        background.paste(eyes, (0, 0), eyes.convert('RGBA'))

        background.save("output/" + str(i) + ".png")
        print(str(((i + 1) / total * 100)) + "% complete")


def randomColorIndex():
    dirs = []

    for (_, dirname, _) in walk(Layer.COLOR.value):
        dirs.extend(dirname)
        break
    return random.randint(0, len(dirs) - 1)

def randomIndex(colorPath, layer):
    files = []
    for (_, _, filename) in walk(colorPath + layer.value):
        files.extend(filename)
        break
    if ".DS_Store" in files:
        files.remove(".DS_Store")
    return random.randint(0, len(files) - 1)


def getColorPath(index):
    dirs = []

    for (_, dirname, _) in walk(Layer.COLOR.value):
        dirs.extend(dirname)
        break
    return "./COMMONs/" + dirs[index] + "/"

def getPath(colorPath, layer, index):
    files = []
    for (_, _, filename) in walk(colorPath + layer.value):
        files.extend(filename)
        break
    if ".DS_Store" in files:
        files.remove(".DS_Store")

    return colorPath + layer.value + str(files[index])

class Layer(Enum):
    COLOR = "./COMMONs/"
    BACKGROUND = "BACKGROUNDS/"
    SPIKES = "SPIKES/"
    WINGS = "WINGS/"
    BASE = "BASE/"
    TAILTIPS = "TAILTIPS/"
    MOUTH = "../../STATICs/MOUTHS/"
    EYES = "../../STATICs/EYES/"


generateImages()
