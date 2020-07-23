import sys 
import os
from PIL import Image

def main():

	#grad the first (folder with images) and second argument (new folder with converted images)
	image_folder = sys.argv[1]
	output_folder = sys.argv[2]
	

	print(output_folder)


	path = os.getcwd()

	if not os.path.exists(output_folder):
		os.makedirs(output_folder)


	#loop through pictures and convert to png and save them to the new folder
	for filename in os.listdir(image_folder):
		img = Image.open(f'{image_folder}/{filename}')
		clean_name = os.path.splitext(filename)[0]
		print("clean name ",clean_name)
		img.save(f"{output_folder}/{clean_name}.png", "png")
		print("all done")
			
	


main()
