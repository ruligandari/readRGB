from PIL import Image

# Membaca gambar
image_path = "4x4-anggi.jpg"
image = Image.open(image_path)

# Mendapatkan mode gambar
mode = image.mode

# Memastikan gambar dalam mode RGB
if mode != "RGB":
    image = image.convert("RGB")

# Mendapatkan lebar dan tinggi gambar
width, height = image.size

# Membuat list untuk menyimpan nilai R, G, dan B
R = []
G = []
B = []

# Mengiterasi setiap pixel dan menyimpan nilai RGB
for y in range(height):
    row_R = []
    row_G = []
    row_B = []
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        row_R.append(r)
        row_G.append(g)
        row_B.append(b)
    R.append(row_R)
    G.append(row_G)
    B.append(row_B)

# Menyimpan nilai R, G, dan B ke dalam file txt
with open("rgb_values.txt", "w") as file:
    file.write("R = " + str(R) + "\n")
    file.write("G = " + str(G) + "\n")
    file.write("B = " + str(B) + "\n")

print("Nilai R, G, dan B telah disimpan ke dalam file txt.")
