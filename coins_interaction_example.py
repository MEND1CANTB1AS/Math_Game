# https://arcade.academy/examples/sprite_collect_rotating.html
# https://arcade.academy/arcade.html 
# https://arcade.academy/examples/sprite_no_coins_on_walls.html
# http://programarcadegames.com/index.php?chapter=introduction_to_sprites

import arcade
import random
import os
from PIL import Image

SPRITE_SCALING = 0.75
SPRITE_SCALING_COIN = 0.75

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite No Coins on Walls Example"

NUMBER_OF_COINS = 7

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.all_sprites_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None
        self.wall_list = None
        self.physics_engine = None
        self.score = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64

        # -- Set up the walls
        # Create a series of horizontal walls
        for y in range(0, 800, 200):
            for x in range(100, 700, 64):
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
        
        images_list = [r"number_images\0.png",r"number_images\1.png",r"number_images\2.png",r"number_images\3.png",r"number_images\4.png",r"number_images\5.png",r"number_images\6.png",r"number_images\7.png",r"number_images\8.png",r"number_images\9.png"]
        
        answer = "12"

        if len(str(answer)) == 2 and (f"number_images\{answer}.png" not in images_list):
            images = [Image.open(x) for x in [f"number_images\{answer[0]}.png", f"number_images\{answer[1]}.png"]]
            total_width = 0
            max_height = 0
            for image in images:
                total_width += image.size[0]
                max_height = max(max_height, image.size[1])
            new_image = Image.new('RGB', (total_width, max_height))
            current_width = 0
            for image in images:
                new_image.paste(image, (current_width,0))
                current_width += image.size[0]
            new_image.save(f"number_images\{answer}.png")
        
        answer_image = (f"number_images\{answer}.png")

        # images_list = ["number_images\0.png","number_images\1.png","number_images\2.png","number_images\3.png","number_images\4.png","number_images\5.png","number_images\6.png","number_images\7.png","number_images\8.png","number_images\9.png"]

        # -- Randomly place coins where there are no walls
        # Create the coins
        answer_coin = arcade.Sprite(answer_image, SPRITE_SCALING_COIN)
        self.coin_list.append(answer_coin)

        for i in range(NUMBER_OF_COINS-1):

            # Create the coin instance
            # image = f'r"{random.choice(images_list)}"'
            # if len(str(answer)) == 2:
            #     image1 = random.choice(images_list)
            #     image2 = random.choice(images_list)
            #     image = (image1, image2)
            # else:
            image = random.choice(images_list)
            coin = arcade.Sprite(image, SPRITE_SCALING_COIN)

        # answer = 2
        # def generate_number_set(answer):
        #     number_set = {answer}
        #     for i in range(NUMBER_OF_COINS-1):
        #         number_set.add(random.randrange(0, answer + 11))
        #     return number_set

        # def clear_number_set(number_set):
        #     number_set.clear()

            # --- IMPORTANT PART ---

            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(SCREEN_WIDTH)
                coin.center_y = random.randrange(SCREEN_HEIGHT)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            # Add the coin to the lists
            # MAKE SURE THAT THERE ARE NO DUPLICATES 
            # if coin not in self.coin_list:
            self.coin_list.append(coin)

            # --- END OF IMPORTANT PART ---

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.COOL_BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_sprite.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 65, 10, arcade.color.BLACK, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.coin_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            self.score += 1
            coin.remove_from_sprite_lists()

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()