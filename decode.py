import cv2
import numpy as np

def decode_message('output.png'):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or invalid format.")
        return

    binary_message = ""
    
    for row in img:
        for pixel in row:
            for channel in range(3):
                binary_message += str(pixel[channel] & 1)

    # Split binary data into bytes
    byte_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    
    # Convert binary to characters
    decoded_chars = []
    for byte in byte_message:
        if byte == '1111111111111110':  # Stop signal
            break
        decoded_chars.append(chr(int(byte, 2)))

    decoded_message = ''.join(decoded_chars)
    print("Decoded Message:", decoded_message)
    
