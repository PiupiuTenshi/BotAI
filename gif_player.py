import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def show_gif(path, duration=4000):
    root = tk.Tk()
    
    # Setting window
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    
    #! Notes:  GIFs shouldn't be black, otherwise they will be corrupted.
    root.config(bg='black') 
    root.wm_attributes("-transparentcolor", "black")

    # Setting position of GIF
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    gif_w, gif_h = 200, 200
    x = screen_width - gif_w - 20
    y = screen_height - gif_h - 60
    root.geometry(f"{gif_w}x{gif_h}+{x}+{y}")

    try:
        img = Image.open(path)
        frames = [ImageTk.PhotoImage(frame.copy().resize((gif_w, gif_h))) 
                  for frame in ImageSequence.Iterator(img)]
        
        label = tk.Label(root, bg='black', borderwidth=0) 
        label.pack()

        def update(ind):
            frame = frames[ind]
            label.configure(image=frame)
            root.after(100, update, (ind + 1) % len(frames))

        root.after(0, update, 0)
        root.after(duration, root.destroy)
        root.mainloop()
        
    except Exception as e:
        print(f"Lỗi: {e}")
        root.destroy()