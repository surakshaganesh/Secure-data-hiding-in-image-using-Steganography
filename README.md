# Secure-data-hiding-in-image-using-Steganography

This project involves implementing image steganography to securely hide data inside images. The goal is to conceal information within an image file without significantly altering the image's appearance. The project will use cryptographic techniques and Least Significant Bit (LSB) steganography for embedding and extracting hidden data.

Implementation Steps:

1. Encoding (Hiding Data)
Load the cover image.
Convert the image into a pixel matrix.
Convert the secret message into binary.
Modify the Least Significant Bit (LSB) of selected pixels to embed the binary data.
Save the modified image as the stego-image.

3. Decoding (Extracting Data)
Load the stego-image.
Retrieve the LSBs of selected pixels.
Extract and reconstruct the binary data to recover the hidden message.
