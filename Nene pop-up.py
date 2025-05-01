import tkinter as tk
from PIL import Image, ImageTk
import os
import random

# === Initialize Tkinter FIRST ===
root = tk.Tk()
root.geometry("500x400")
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# === Load image frames AFTER root is initialized ===
frame_dir = "D:/Python_Programs/Program"
frame_files = sorted([f for f in os.listdir(frame_dir) if f.startswith("frame_") and f.endswith(".png")])
frames = [ImageTk.PhotoImage(Image.open(os.path.join(frame_dir, f)).convert("RGBA")) for f in frame_files]

# === Setup character animation ===
sprite = canvas.create_image(200, 150, image=frames[0], anchor='nw')
popup_images = []
index = 0

def animate():
    global index
    canvas.itemconfig(sprite, image=frames[index])
    index = (index + 1) % len(frames)
    root.after(100, animate)

def on_click(event):
    popup = Image.open("D:/Python_Programs/Program/Nene_Kusanagi.png").convert("RGBA").resize((100, 100))
    popup_photo = ImageTk.PhotoImage(popup)
    popup_images.append(popup_photo)

    x = random.randint(0, 400)
    y = random.randint(0, 300)
    popup_id = canvas.create_image(x, y, image=popup_photo, anchor='nw')

    def remove():
        canvas.delete(popup_id)
        popup_images.remove(popup_photo)

    root.after(3000, remove)

canvas.bind("<Button-1>", on_click)

animate()
root.mainloop()
