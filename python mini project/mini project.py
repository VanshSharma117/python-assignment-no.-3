import tkinter as tk
import random

WIDTH = 500 
HEIGHT = 500  
CELL_SIZE = 20 

class SnakeGame:
    def init(self, root):
        """Initialize the game window and variables."""
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]

        self.food = self.create_food()

        self.direction = "Right"
        self.running = True

        self.root.bind("<KeyPress>", self.change_direction)

        self.update_game()

    def create_food(self):
        """Generate a new food position at a random location on the grid."""
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        return (x, y)

    def change_direction(self, event):
        """Change the direction of the snake based on user input."""
        if event.keysym in ["Left", "Right", "Up", "Down"]:

            opposite_directions = {"Left": "Right", "Right": "Left", "Up": "Down", "Down": "Up"}
            if opposite_directions.get(event.keysym) != self.direction:
                self.direction = event.keysym

    def move_snake(self):
        """Move the snake in the current direction and handle collisions."""
        head_x, head_y = self.snake[0]

        if self.direction == "Left":
            head_x -= CELL_SIZE
        elif self.direction == "Right":
            head_x += CELL_SIZE
        elif self.direction == "Up":
            head_y -= CELL_SIZE
        elif self.direction == "Down":
            head_y += CELL_SIZE

        new_head = (head_x, head_y)

        if (
            new_head in self.snake or
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT
        ):
            self.running = False
            return
        
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.create_food() 
        else:
            self.snake.pop() 

    def draw_elements(self):
        """Render the snake and food on the canvas."""
        self.canvas.delete("all")  

        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="green")

        food_x, food_y = self.food
        self.canvas.create_oval(food_x, food_y, food_x + CELL_SIZE, food_y + CELL_SIZE, fill="red")

    def update_game(self):
        """Update the game state and refresh the screen."""
        if self.running:
            self.move_snake()
            self.draw_elements()
            self.root.after(100, self.update_game)
        else:
            self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", fill="white", font=("Arial", 20))

if name == "main":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()