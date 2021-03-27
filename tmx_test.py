"""
Platformer Game
"""
import arcade
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = .4
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = (SPRITE_PIXEL_SIZE * TILE_SCALING)
SPRITE_SCALING = 0.4

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = .6
PLAYER_JUMP_SPEED = 10

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 250
RIGHT_VIEWPORT_MARGIN = 250
BOTTOM_VIEWPORT_MARGIN = 100
TOP_VIEWPORT_MARGIN = 100


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = SPRITE_SCALING
        self.textures = []

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png")
        self.textures.append(texture)
        texture = arcade.load_texture(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png",
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

class Problem():
    def __init__(self):
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.problem_text, self.answer = self.equation()
        # self.answer = self.equation()

    def equation(self):
        # the operator (+, -, *, /) will be randomly assigned
        operator = random.randint(1, 4)

        # addition problems
        if operator == 1:
            x = int(random.randint(0, 10))
            y = int(random.randint(0, 10))
            question = (f'{x} + {y} = ')
            answer = str(x + y)
            return question, answer
            # if question == answer:
            #     print("Correct!")

        # subtraction problems
        elif operator == 2:
            x = int(random.randint(0, 10))
            y = int(random.randint(0, x))
            question = (f'{x} - {y} = ')
            answer = str(x - y)
            return question, answer
            # if question == answer:
                # print('Correct!')

        # multiplication problems
        elif operator == 3:
            x = int(random.randint(0, 11))
            y = int(random.randint(0, 9))
            question = (f'{x} x {y} = ')
            answer = str(x * y)
            return question, answer
            # if question == answer:
            #     print('Correct!')

        # division problems
        else:
            x = int(random.randint(1, 10))
            y = int(random.randint(0, 10))
            z = x * y
            question = (f'{z} / {x} = ')
            answer = str(z / x)
            return question, answer
            # if question == answer:
            #     print('Correct!')

class Number(arcade.Sprite):

    def __init__(self, value=-1):
        super().__init__()
        if value == -1:
            self.value = random.randint(1, 99)
        else:
            self.value = value
        self.texture = Number.convert_text_to_texture(self, str(self.value))
        self.center_x = random.randint(10, SCREEN_HEIGHT-10)
        self.center_y = SCREEN_WIDTH - 10
        # self.change_x = random.uniform(-5, 2)
        # self.change_y = random.uniform(-0.1, -5)

    # def update(self):
    #     self.center_x += self.change_x
    #     self.center_y += self.change_y
    #     if self.center_x < 0 or self.center_x > SCREEN_WIDTH:
    #         self.change_x *= -1
    #     if self.center_y < 0:
    #         self.remove_from_sprite_lists()

    def convert_text_to_texture(self, text_value):
        img = Image.new('RGBA', (125,125), color = (255, 255, 255, 0))
        d = ImageDraw.Draw(img) 
        fnt = ImageFont.truetype('times', 100)
        d.text((15,5), text_value, font=fnt, fill = arcade.color.BURNT_ORANGE) 
        texture = arcade.Texture(str(text_value), img) 
        return texture

    def hit(self, problem):
        self.remove_from_sprite_lists()
        return problem.solve(self.value)

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.player_list = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        self.problem = None
        self.number = arcade.SpriteList()

        # Load sounds
        # self.collect_coin_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump1.wav")

        # arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # Used to keep track of our scrolling
        self.view_bottom = 0
        self.view_left = 0

        # Keep track of the score
        self.score = 0

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player, specifically placing it at these coordinates.
        # image_source = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
        self.player_list = arcade.SpriteList()
        self.player_sprite = Player()
        self.player_sprite.center_x = 256
        self.player_sprite.center_y = 256
        self.player_list.append(self.player_sprite)

        # --- Load in a map from the tiled editor ---

        # Name of map file to load
        map_name = "floor_is_lava.tmx"
        # Name of the layer in the file that has our platforms/walls
        platforms_layer_name = 'Platforms'

        # Read in the tiled map
        my_map = arcade.tilemap.read_tmx(map_name)

        # -- Platforms
        self.wall_list = arcade.tilemap.process_layer(map_object=my_map,
                                                      layer_name=platforms_layer_name,
                                                      scaling=TILE_SCALING,
                                                      use_spatial_hash=True)

        # --- Other stuff
        # Set the background color
        if my_map.background_color:
            arcade.set_background_color(my_map.background_color)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        
        self.player_list.draw()
        self.number.draw()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10 + self.view_left, 10 + self.view_bottom,
                         arcade.csscolor.WHITE, 18)

        if self.problem is not None:
            arcade.draw_text(self.problem.problem_text, self.problem.center_x, self.problem.center_y, arcade.color.WHITE)

    def create_problem(self):
        # if self.problem_timer == 0:
        self.problem = Problem()
            # self.problem_timer = 6000
        # else:
            # self.problem_timer -= 1
    
    def create_number(self):
        if (self.problem.answer not in self.number) and (random.randint(1, 50) == 1):
            num = Number(self.problem.answer)
            self.number.append(num)
        elif random.randint(1, 50) == 1:
            num = Number()
            self.number.append(num)

    def create_answer_number(self):
        value = Number(self.problem.answer)
        self.number.append(value)
        # self.number.update()
    


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        coor = arcade.Window.get_location(self)
        print(coor)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player with the physics engine
        self.physics_engine.update()

        # --- Manage Scrolling ---

        # Track if we need to change the viewport

        changed = False

        # Scroll left
        left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left
            changed = True

        # Scroll right
        right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary
            changed = True

        # Scroll up
        top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary
            changed = True

        # Scroll down
        bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom
            changed = True

        if changed:
            # Only scroll to integers. Otherwise we end up with pixels that
            # don't line up on the screen
            self.view_bottom = int(self.view_bottom)
            self.view_left = int(self.view_left)

            # Do the scrolling
            arcade.set_viewport(self.view_left,
                                SCREEN_WIDTH + self.view_left,
                                self.view_bottom,
                                SCREEN_HEIGHT + self.view_bottom)
        
        self.create_problem()
        self.create_number()
        self.number.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.number)
        for number in hit_list:
            self.score += number.hit(self.problem)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()