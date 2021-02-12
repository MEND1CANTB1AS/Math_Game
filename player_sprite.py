import arcade
import random

#Controls the size of the sprite
SPRITE_SCALING = 0.1
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Controls the movement of the Sprite
SPRITE_MOV_SPEED = 5

# Inherits the Sprite class
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = SPRITE_SCALING
        self.textures = []

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture("sprite.jpg")
        self.textures.append(texture)
        texture = arcade.load_texture("sprite.jpg",
                                      flipped_horizontally=True)
        self.textures.append(texture)

        # By default, face right.
        self.texture = texture


    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[1]
        elif self.change_x > 0:
            self.texture = self.textures[0]

        # Makes sure the sprite doesn't go off the screen
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MathGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.player_list = None
        self.player_sprite = None
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = Player()
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = SPRITE_MOV_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -SPRITE_MOV_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -SPRITE_MOV_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = SPRITE_MOV_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    window = MathGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()