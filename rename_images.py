import os
"""
Rename a list of images to a standard format.

Parameters
----------
dirs_paths: list
    A list of file paths of the images to be renamed.

Returns
-------
None
"""
def rename_images(dirs_paths):
    print(dirs_paths)
    try:
        for images_list in dirs_paths:
            images = os.listdir(images_list)
            index = 0
            for image in images:
                image_format = get_og_format(image)
                os.rename(images_list+"/"+image,(f'{images_list}/{index}.{image_format}'))
                index += 1
            return
    except Exception as e:
        print(e)

"""
Get the original format of an image.

Parameters
----------
image: str
    The original image name.

Returns
-------
str
    The original format of the image.
"""
def get_og_format(image):
    format = image.split(".")[-1]
    return format


    
