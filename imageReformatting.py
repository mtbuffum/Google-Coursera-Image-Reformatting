#!/usr/bin/env python
#Created by Mason Buffum for Google Coursera Certification Module 1
import os
from PIL import Image

old_path = os.path.expanduser('~') + '/images/'
new_path = '/opt/icons/'

for image in os.listdir(old_path):
    # Check if the file has an extension and is an image
    if '.' in image and image.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        try:
            # Open and process the image
            img = Image.open(os.path.join(old_path, image))
            img.rotate(-90).resize((128, 128)).convert("RGB").save(os.path.join(new_path, image.split('.')[0] + '.jpeg'), 'jpeg')
            img.close()
        except Exception as e:
            print(f"Error processing {image}: {e}")
