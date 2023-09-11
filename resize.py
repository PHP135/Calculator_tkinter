from PIL import Image

image_open = Image.open("navbar.png")

image = image_open.resize((30, 30))

image.save("C:\\Users\\hodin\\OneDrive\\Máy tính\\assets\\navbar1.png")


