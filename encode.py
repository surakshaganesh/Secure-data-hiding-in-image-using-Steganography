>>> import cv2
... import numpy as np
... 
... def encode_message('C:/Users/Suraksha/OneDrive/Desktop/project/input.png', 'Secret123', 'output.png')
...     img = cv2.imread(image_path)
...     if img is None:
...         print("Error: Image not found or invalid format.")
...         return
... 
...     binary_message = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110'  # Stop signal
... 
...     data_index = 0
...     total_pixels = img.shape[0] * img.shape[1] * 3  # Total RGB values available
... 
...     if len(binary_message) > total_pixels:
...         print("Error: Message is too large to fit in the image.")
...         return
... 
...     for row in img:
...         for pixel in row:
...             for channel in range(3): 
...                 if data_index < len(binary_message):
...                     pixel[channel] = pixel[channel] & ~1 | int(binary_message[data_index])
...                     data_index += 1
...                 else:
...                     break
...             if data_index >= len(binary_message):
...                 break
...         if data_index >= len(binary_message):
...             break
... 
...     cv2.imwrite(output_image, img)
...     print(f"Message successfully encoded in {output_image}!")
... 
