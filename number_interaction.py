# https://arcade.academy/examples/sprite_collect_rotating.html
# https://arcade.academy/arcade.html 
# https://arcade.academy/examples/sprite_no_numbers_on_walls.html
# http://programarcadegames.com/index.php?chapter=introduction_to_sprites

import arcade
import random
import os
from PIL import Image

SPRITE_SCALING = 0.75
SPRITE_SCALING_NUMBER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite No numbers on Walls Example"

NUMBER_OF_NUMBERS = 7

MOVEMENT_SPEED = 5

class Number(arcade.Sprite):

    def __init__(self):
        super().__init__()
        

    images_list = [r"0.png",r"1.png",r"2.png",r"3.png",r"4.png",r"5.png",r"6.png",r"7.png",r"8.png",r"9.png"]
        
    answer = "12"
    
    def generate_double_image(number, images_list):
        # Generates answer image.
        if len(str(number)) == 2 and (f"{number}.png" not in images_list):
            images = [Image.open(x) for x in [f"{number[0]}.png", f"{number[1]}.png"]]
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
            new_image.save(f"{number}.png")
        new_image = (f"{number}.png")
        return new_image

    def create_double_number():
        first_number = random.randint(1,9)
        second_number = random.randint(0,9)
        number = str(f"{first_number}" + f"{second_number}")
        return number

    #TODO: get to recognize answer number when hit (can access inside of Sprite?)
    #TODO: get points to work
    #TODO: make function to hold large for loop for if len 1 and 2

    def create_double_digit_images_list(images_list):
        double_number_list = []
        for _ in range(1, NUMBER_OF_NUMBERS-1):
            double_number_list.append(create_double_number())
        double_digit_images_list = []
        for number in double_number_list:
            double_digit_images_list.append(generate_double_image(number, images_list))
        return double_digit_images_list
    
    if len(answer) == 2:
        answer_image = generate_double_image(answer, images_list)
        answer_number = arcade.Sprite(answer_image, SPRITE_SCALING_NUMBER)
        self.number_list.append(answer_number)
        double_digit_images_list = create_double_digit_images_list(images_list)
    
    if len(answer) == 1:
        answer_image = f"{answer}.png"
        answer_number = arcade.Sprite(answer_image, SPRITE_SCALING_NUMBER)
        self.number_list.append(answer_number)

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
        self.number_list = None

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
        self.number_list = arcade.SpriteList()
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
        
        

        if len(answer) == 2:
            answer_image = generate_double_image(answer, images_list)
            answer_number = arcade.Sprite(answer_image, SPRITE_SCALING_NUMBER)
            self.number_list.append(answer_number)
            double_digit_images_list = create_double_digit_images_list(images_list)
            
            for image in double_digit_images_list:
                number = arcade.Sprite(image, SPRITE_SCALING_NUMBER)
                self.number_list.append(number)

                # --- IMPORTANT PART ---

                # Boolean variable if we successfully placed the number
                number_placed_successfully = False

                # Keep trying until success
                while not number_placed_successfully:
                    # Position the number
                    number.center_x = random.randrange(SCREEN_WIDTH)
                    number.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the number is hitting a wall
                    wall_hit_list = arcade.check_for_collision_with_list(number, self.wall_list)

                    # See if the number is hitting another number
                    number_hit_list = arcade.check_for_collision_with_list(number, self.number_list)

                    if len(wall_hit_list) == 0 and len(number_hit_list) == 0:
                        number_placed_successfully = True

                # Add the number to the list and ensure that there are no duplicates.
                # if number not in self.number_list:
                self.number_list.append(number)
                # else:
                #     image = random.choice(images_list)
                #     number = arcade.Sprite(image, SPRITE_SCALING_NUMBER)
                #     self.number_list.append(number)

        if len(answer) == 1:
            answer_image = f"{answer}.png"

        # -- Randomly place numbers where there are no walls
        # Create the numbers
            answer_number = arcade.Sprite(answer_image, SPRITE_SCALING_NUMBER)
            self.number_list.append(answer_number)

        # Selects a random image from the images.
            for i in range(NUMBER_OF_NUMBERS-1):
                image = random.choice(images_list)
                number = arcade.Sprite(image, SPRITE_SCALING_NUMBER)

                # --- IMPORTANT PART ---

                # Boolean variable if we successfully placed the number
                number_placed_successfully = False

                # Keep trying until success
                while not number_placed_successfully:
                    # Position the number
                    number.center_x = random.randrange(SCREEN_WIDTH)
                    number.center_y = random.randrange(SCREEN_HEIGHT)

                    # See if the number is hitting a wall
                    wall_hit_list = arcade.check_for_collision_with_list(number, self.wall_list)

                    # See if the number is hitting another number
                    number_hit_list = arcade.check_for_collision_with_list(number, self.number_list)

                    if len(wall_hit_list) == 0 and len(number_hit_list) == 0:
                        number_placed_successfully = True

                # Add the number to the list and ensure that there are no duplicates.
                # if number not in self.number_list:
                self.number_list.append(number)
                # else:
                #     image = random.choice(images_list)
                #     number = arcade.Sprite(image, SPRITE_SCALING_NUMBER)
                #     self.number_list.append(number)


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
        self.number_list.draw()
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
        self.number_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.number_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for number in hit_list:
            self.score += 1
            number.remove_from_sprite_lists()

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()