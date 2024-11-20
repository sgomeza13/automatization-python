import sys
from rename_images import rename_images

"""
Arguments:
    images_list: A list of file paths of the images to be renamed.
"""
if __name__ == "__main__":
    images_list = sys.argv[1:]
    rename_images(images_list)