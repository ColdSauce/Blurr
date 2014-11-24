import pygame
from pygame.locals import *
from PIL import Image

def getPixels(path):
	im = Image.open(path).convert("RGB")
	pixels = list(im.getdata())
	width, height = im.size
	pixels = [pixels [i * width:(i + 1) * width] for i in xrange(height)]
	return (pixels,width,height)


def main():
	pixels,width,height = getPixels("example.jpg")
	pygame.init()
	screen = pygame.display.set_mode((2001,2001))
	pygame.display.set_caption('Blurr')

	background = pygame.Surface(screen.get_size())
	background = background.convert()

	screen.blit(background,(0,0))
	for x in range(height):
		for y in range(width):
			try:
				backgroundx.set_at((x,y),pixels[x][y])
			except:
				print str(x) + " , " + str(y)

	pygame.display.flip()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
		screen.blit(background,(0,0))
		pygame.display.flip()



if __name__ == "__main__":
	main()
