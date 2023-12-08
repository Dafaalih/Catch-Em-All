import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


#creating a list of texture names that will be used to identify each texture.
texture_names = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39 , 40 , 41, 42 , 43, 44, 45 , 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

# assigning a unique integer identifier to each texture using global constants, which makes it easier to refer to textures throughout the code.
CRUSTLE1 = 0
CRUSTLE2 = 1
CHAR1 = 2
BG1 = 3
PLAY = 4
QUIT = 5
OPTION = 6
GAMENAME = 7
OPTIONCLICK = 8
PLAYCLICK = 9
QUITCLICK = 10
BOTTOM1 = 11
BOTTOM2 = 12
BOTTOM3 = 13
BOTTOM4 = 14
LEFT1 = 15
LEFT2 = 16
LEFT3 = 17
LEFT4 = 18
RIGHT1 = 19
RIGHT2 = 20
RIGHT3 = 21
RIGHT4 = 22
TOP1 = 23
TOP2 = 24
TOP3 = 25
TOP4 = 26
BG2 = 27
BGOUT = 28
POKEMONTRAINER = 29
HOME = 30
GAMEOVER = 31
FINISH = 32
PIDGEOT1 = 33
PIDGEOT2 = 34
PIKACHU1 = 35
PIKACHU2 = 36
TAILLOW1 = 37
TAILLOW2 = 38
INTROBOY = 39
INTROGIRL = 40
EASY = 41
EASYCLICK = 42
MEDIUM = 43
MEDIUMCLICK = 44
HARD = 45
HARDCLICK = 46
BGSUNSET = 47
BGUMI = 48
BACKGROUNDTITLE = 49
FARMERBUTTON = 50
SUNSETBUTTON = 51 
UMIBUTTON = 52
BOXBACKGROUND = 53
BACKBUTTON = 54
BACKBUTTONCLICK = 55



def load_texture():
    """
    enables 2D texture mapping for OpenGL, loads all the texture images and stores them as a list of texture binary data.
    It then generates a unique texture name for each image and sets up the texture parameters for each texture using the setup_texture() function.
    """
    glEnable(GL_TEXTURE_2D)

    images = []

    # Load images from files
    images.append(pygame.image.load("assets/img/Crustle/image1.png"))
    images.append(pygame.image.load("assets/img/Crustle/image2.png"))
    images.append(pygame.image.load("assets/img/trainer.png"))
    images.append(pygame.image.load("assets/img/Background/BG.png"))
    images.append(pygame.image.load("assets/img/Button/PLAY.png"))
    images.append(pygame.image.load("assets/img/Button/QUIT.png"))
    images.append(pygame.image.load("assets/img/Button/OPTION.png"))
    images.append(pygame.image.load("assets/img/Namagame.png"))
    images.append(pygame.image.load("assets/img/Button/OPTION-CLICK.png"))
    images.append(pygame.image.load("assets/img/Button/PLAY-CLICK.png"))
    images.append(pygame.image.load("assets/img/Button/QUIT-CLICK.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image1.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image2.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image3.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image4.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image5.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image6.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image7.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image8.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image9.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image10.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image11.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image12.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image13.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image14.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image15.png"))
    images.append(pygame.image.load("assets/img/pokemontrainer/image16.png"))
    images.append(pygame.image.load("assets/img/Background/background.png"))
    images.append(pygame.image.load("assets/img/Background/bg-out.png"))
    images.append(pygame.image.load("assets/img/trainer2.png"))
    images.append(pygame.image.load("assets/img/home.png"))
    images.append(pygame.image.load("assets/img/Button/Gameover.png"))
    images.append(pygame.image.load("assets/img/Button/Finish.png"))
    images.append(pygame.image.load("assets/img/Pidgeot/image1.png"))
    images.append(pygame.image.load("assets/img/Pidgeot/image2.png"))
    images.append(pygame.image.load("assets/img/Pikachu/image1.png"))
    images.append(pygame.image.load("assets/img/Pikachu/image2.png"))
    images.append(pygame.image.load("assets/img/Taillow/image1.png"))
    images.append(pygame.image.load("assets/img/Taillow/image2.png"))
    images.append(pygame.image.load("assets/img/Background/introBoy.png"))
    images.append(pygame.image.load("assets/img/Background/introGirl.png"))
    images.append(pygame.image.load("assets/img/Button/Easy.png"))
    images.append(pygame.image.load("assets/img/Button/Easy-Click.png"))
    images.append(pygame.image.load("assets/img/Button/Normal.png"))
    images.append(pygame.image.load("assets/img/Button/Normal-Click.png"))
    images.append(pygame.image.load("assets/img/Button/Hard.png"))
    images.append(pygame.image.load("assets/img/Button/Hard-Click.png"))
    images.append(pygame.image.load("assets/img/Background/BG-Sunset.png"))
    images.append(pygame.image.load("assets/img/Background/BG-umi.png"))
    images.append(pygame.image.load("assets/img/Option/Background-title.png"))
    images.append(pygame.image.load("assets/img/Option/farmer-button.png"))
    images.append(pygame.image.load("assets/img/Option/sunset-button.png"))
    images.append(pygame.image.load("assets/img/Option/umi-button.png"))
    images.append(pygame.image.load("assets/img/Option/box-background.png"))
    images.append(pygame.image.load("assets/img/Button/back.png"))
    images.append(pygame.image.load("assets/img/Button/back-click.png"))
    
    # Convert the images to raw binary image data
    textures = [pygame.image.tostring(img,"RGBA", 1) for img in images]

    # Generate texture IDs
    glGenTextures(len(images), texture_names)

    # Bind each texture and set texture parameters
    for i in range(len(images)):
        setup_texture(textures[i],
                      texture_names[i],
                      images[i].get_width(),
                      images[i].get_height())


def setup_texture(binary_img, texture_iden, width, height):
    """
    binds the texture to the texture identifier, sets texture parameters, and then loads the texture binary data.
    """
    glBindTexture(GL_TEXTURE_2D, texture_iden)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width,
                 height, 0, GL_RGBA, GL_UNSIGNED_BYTE, binary_img)
