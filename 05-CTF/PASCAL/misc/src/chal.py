#!/usr/bin/env python3
import sys
import argparse
from PIL import Image

def message_to_binary(message):
    return ''.join(format(ord(c), '08b') for c in message)

def generate_border_coordinates(width, height):
    coords = []
    
    for x in range(width):
        coords.append((x, 0))
    
    for y in range(1, height-1):
        coords.append((width-1, y))
    
    if height > 1:
        for x in range(width-1, -1, -1):
            coords.append((x, height-1))
    
    if width > 1:
        for y in range(height-2, 0, -1):
            coords.append((0, y))
    
    return coords

def add_binary_frame(input_image_path, message, output_image_path):
    img = Image.open(input_image_path)
    img = img.convert("RGB")
    orig_width, orig_height = img.size

    binary_str = message_to_binary(message)
    if not binary_str:
        raise ValueError("The provided message is empty; cannot create a binary frame.")

    new_width = orig_width + 2
    new_height = orig_height + 2
    new_img = Image.new("RGB", (new_width, new_height), "white")
    
    new_img.paste(img, (1, 1))

    border_coords = generate_border_coordinates(new_width, new_height)
    border_length = len(border_coords)

    for i, coord in enumerate(border_coords):
        bit = binary_str[i % len(binary_str)]
        # '0' becomes black, '1' becomes white.
        color = (0, 0, 0) if bit == '0' else (255, 255, 255)
        new_img.putpixel(coord, color)
    
    new_img.save(output_image_path)
    print(f"Image saved with binary frame to {output_image_path}")

def main():
    parser = argparse.ArgumentParser(description="Add a 1px binary frame to an image using a message.")
    parser.add_argument("input_image", help="Path to the input image file.")
    parser.add_argument("message", help="Message to convert into a binary frame.")
    parser.add_argument("output_image", help="Path to save the output image file.")
    args = parser.parse_args()
    
    add_binary_frame(args.input_image, args.message, args.output_image)

if __name__ == "__main__":
    main()
