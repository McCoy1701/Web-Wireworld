import glob, os
from PIL import Image

def makeGif(frameFolder, name):
    frame = [Image.open(image) for image in glob.glob(f'{frameFolder}/*.PNG')]
    frameOne = frame[0]
    frameOne.save('gifs/' + name + '.gif', format='GIF', append_images=frame, save_all=True, duration=100, loop=0)

def walker(folder):
    folders = os.listdir(folder)
    for dir in folders:
        makeGif(folder + dir + '/', dir)

if __name__ == '__main__':
    walker('animations/')
