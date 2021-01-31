import arcade
import images
import math
import random
import time
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Math Game"
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * SPRITE_SCALING)
LEFT_LIMIT = 0
RIGHT_LIMIT = SCREEN_WIDTH

# Physics
MOVEMENT_SPEED = 10 * SPRITE_SCALING
JUMP_SPEED = 20 * SPRITE_SCALING
GRAVITY = .75 * SPRITE_SCALING
FRICTION = 1.1

class GameView(arcade.View):
    """ Main game """

    def __init__(self):
        super().__init__()
        
        arcade.set_background_color(arcade.color.AMAZON)
        self.wall_list = arcade.SpriteList()

    def setup(self):
        pass
        #Create Border

class InstructionView(arcade.View):
    """ View to show instructions """

    def on_show(self):
        self.count = 0
        arcade.set_background_color(arcade.color.AMAZON)
        # self.background_1 = arcade.load_texture("images/forest_background_wide_a.png")
        # arcade.set_background_color = None
    
    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()


        arcade.draw_text("Click to Start", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Controls: ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("WASD / Spacebar - Move / Jump", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-100,
                         arcade.color.WHITE, font_size=20, anchor_x="center")                 
        arcade.draw_text("Left Mouse - Interact", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-125,
                         arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.draw_text("Pause ", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-150,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        self.window.show_view(GameView())

def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, fullscreen=True)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


main()