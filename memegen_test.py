# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator
from simpleimage import SimpleImage

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('distracted_boyfriend.png')

    # add text to the top and bottom of the meme
    meme_gen.add_text('Python', 110, 300)
    meme_gen.add_text('Me', 430, 200)
    meme_gen.add_text('C', 610, 220)
    meme_gen.add_text(';', 610, 300)

    # generate the meme!
    meme_gen.render()

if __name__ == '__main__':
    main()