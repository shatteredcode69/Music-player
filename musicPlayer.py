import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player By Abbas Qureshi")
canvas.geometry("600x500")
canvas.config(bg='black')

rootpath = "C:\\Users\w312\Downloads\Music"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file="previous.png")
stop_img = tk.PhotoImage(file="stop.png")
play_img = tk.PhotoImage(file="play.png")
pause_img = tk.PhotoImage(file="pause.png")
next_img = tk.PhotoImage(file="next.png")
volume_up_img = tk.PhotoImage(file="volumeup.png")
volume_down_img = tk.PhotoImage(file="volumedown.png")

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()
    print("Music started.")

def stop():
    mixer.music.stop()
    print("Music stopped.")
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    print("Next song started.")

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text=prev_song_name)

    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()
    print("Previous song started.")

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def pause_song():
    if mixer.music.get_busy():
        mixer.music.pause()
        print("Music paused.")
    else:
        print("No music is playing.")

def volume_up():
    current_volume = mixer.music.get_volume()
    if current_volume < 1.0:
        new_volume = current_volume + 0.1
        mixer.music.set_volume(new_volume)
        print("Volume increased.")

def volume_down():
    current_volume = mixer.music.get_volume()
    if current_volume > 0.0:
        new_volume = current_volume - 0.1
        mixer.music.set_volume(new_volume)
        print("Volume decreased.")

listBox = tk.Listbox(canvas, fg="orange", bg="black", width=100, font=('Foglihten', 16))
listBox.pack(padx=5, pady=5)
label = tk.Label(canvas, text='Music is the language of soul \U0001f600', bg='black', fg='orange', font=(('Foglihten'), 14))
label.pack(pady=5)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=10, anchor='center')

volumeDownButton = tk.Button(canvas, text='volume down', image=volume_down_img, bg='black', borderwidth=0, command=volume_down)
volumeDownButton.pack(pady=15, in_=top, side="left")

prevButton = tk.Button(canvas, text='prev', image=prev_img, bg='black', borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_=top, side="left")

stopbutton = tk.Button(canvas, text='stop', image=stop_img, bg='black', borderwidth=0, command=stop)
stopbutton.pack(pady=15, in_=top, side="left")

playButton = tk.Button(canvas, text='prev', image=play_img, bg='black', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side="left")

pauseButton = tk.Button(canvas, text='prev', image=pause_img, bg='black', borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side="left")

nextButton = tk.Button(canvas, text='prev', image=next_img, bg='black', borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side="left")

volumeUpButton = tk.Button(canvas, text='volume up', image=volume_up_img, bg='black', borderwidth=0, command=volume_up)
volumeUpButton.pack(pady=15, in_=top, side="left")

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()