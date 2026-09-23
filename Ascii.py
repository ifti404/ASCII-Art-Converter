from PIL import Image

im = Image.open("ascii-pineapple.jpg")

# Convert image to grayscale
gray_image = im.convert("L")

# Create brightness matrix
brightness_matrix = []

for y in range(gray_image.height):
    row = []

    for x in range(gray_image.width):
        brightness = gray_image.getpixel((x, y))
        row.append(brightness)

    brightness_matrix.append(row)


# Characters ordered from darkest to lightest
ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# Create ASCII matrix
ascii_matrix = []

for y in range(len(brightness_matrix)):
    row = []

    for x in range(len(brightness_matrix[y])):
        brightness = brightness_matrix[y][x]

        # Map brightness (0-255) to character index
        index = round(
            brightness / 255 * (len(ascii_chars) - 1)
        )

        character = ascii_chars[index]

        row.append(character)

    ascii_matrix.append(row)


print("Successfully constructed ASCII matrix!")
print("ASCII matrix size:", len(ascii_matrix[0]), "x", len(ascii_matrix))

print("Iterating through pixel ASCII characters:")
for row in ascii_matrix:
    for character in row:
        print(character, end="")
    print()