from PIL import Image

img = Image.open('./pokemons/charmander.jpg')
img.rotate(45).show()

