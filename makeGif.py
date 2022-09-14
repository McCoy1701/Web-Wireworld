import glob, os, imageio
from PIL import Image

def makeGif(frameFolder, name):
    with imageio.get_writer('/path/to/movie.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            
def walker(folder):
    folders = os.listdir(folder)
    for dir in folders:
        makeGif(folder + dir + '/', dir)

if __name__ == '__main__':
    makeGif('animations/andGate/', 'andGate')
