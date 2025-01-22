import os
import pygame
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

# Initialize the pygame mixer
pygame.mixer.init()

# Main app class
class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x300")

        # Title Label
        self.label = tk.Label(self.root, text="Music Player", font=("Helvetica", 16))
        self.label.pack(pady=10)

        # Buttons
        self.play_button = tk.Button(self.root, text="Play", width=10, command=self.play_music)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", width=10, command=self.stop_music)
        self.stop_button.pack(pady=10)

        self.pause_button = tk.Button(self.root, text="Pause", width=10, command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.resume_button = tk.Button(self.root, text="Resume", width=10, command=self.resume_music)
        self.resume_button.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Select Music File", width=20, command=self.select_music)
        self.select_button.pack(pady=10)

        # Volume control
        self.volume_label = tk.Label(self.root, text="Volume")
        self.volume_label.pack(pady=5)

        self.volume_scale = tk.Scale(self.root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, command=self.change_volume)
        self.volume_scale.set(0.5)  # Default volume level
        self.volume_scale.pack(pady=10)

        # Current music file
        self.current_music = None

    def select_music(self):
        """Open a file dialog to select a music file."""
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.current_music = file_path
            print(f"Selected Music: {self.current_music}")

    def play_music(self):
        """Play selected music file."""
        if self.current_music:
            mixer.music.load(self.current_music)
            mixer.music.play()
            print(f"Playing: {self.current_music}")
        else:
            print("No music file selected.")

    def stop_music(self):
        """Stop the music."""
        mixer.music.stop()
        print("Music stopped.")

    def pause_music(self):
        """Pause the music."""
        mixer.music.pause()
        print("Music paused.")

    def resume_music(self):
        """Resume the music."""
        mixer.music.unpause()
        print("Music resumed.")

    def change_volume(self, val):
        """Change the volume of the music."""
        volume = float(val)
        mixer.music.set_volume(volume)
        print(f"Volume set to {volume * 100}%")


# Set up the Tkinter root window
root = tk.Tk()
app = MusicPlayerApp(root)

# Run the Tkinter event loop
root.mainloop()
