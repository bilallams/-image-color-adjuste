import tkinter as tk
from tkinter import filedialog, Label, Button, Scale, HORIZONTAL
from PIL import Image, ImageTk
from image_processing import process_image

class ImageEditor:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Image Color Adjuster")
        self.root.geometry("600x700")  # Set an average size for the window

        self.image_label = Label(self.root)
        self.image_label.pack(pady=10)

        self.upload_button = Button(self.root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.red_scale = self.create_scale("Red")
        self.green_scale = self.create_scale("Green")
        self.blue_scale = self.create_scale("Blue")

    def create_scale(self, color):
        scale = Scale(self.root, from_=-255, to=255, orient=HORIZONTAL, label=color, command=self.update_image)
        scale.set(0)  # Set initial position to the middle
        scale.pack(fill=tk.X, padx=20, pady=5)
        return scale

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path).convert('RGB')
            self.display_image(self.image)

    def display_image(self, image):
        # Resize image to fit the window while maintaining aspect ratio
        max_size = (500, 500)
        image.thumbnail(max_size, Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(image)
        self.image_label.config(image=self.tk_image)
        self.image_label.image = self.tk_image

    def update_image(self, event=None):
        if hasattr(self, 'image'):
            red = self.red_scale.get()
            green = self.green_scale.get()
            blue = self.blue_scale.get()
            blended_image = process_image(self.image, red, green, blue)
            self.display_image(blended_image)
