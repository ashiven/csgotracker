import tkinter as tk
import subprocess
import os


def plot():
    subprocess.call(["python", "plot.py"])

def run():
    subprocess.call(["python", "scraper.py"])

def edit_config():
    subprocess.call(["notepad", "config.ini"])

def plotfile():
    if not os.path.isfile('output.csv'):
        open('output.csv', "w").close()
    subprocess.call(["notepad", "output.csv"])



window = tk.Tk()
window.title("CSGOTracker")
window.geometry("400x400")

label = tk.Label(window, text="Welcome to CSGO Tracker!")
label.grid(column=0, row=0, pady=50, sticky="NSEW")

run_button = tk.Button(window, text = "Run!", command = run)
edit_button = tk.Button(window, text = "Edit Config", command = edit_config)
plot_button = tk.Button(window, text = "Show History(Chart)", command = plot)
plotfile_button = tk.Button(window, text = "Show History(File)", command = plotfile)


run_button.grid(row=1, column=0, pady=10, sticky="NSEW")
edit_button.grid(row=2, column=0, pady=10, sticky="NSEW")
plot_button.grid(row=3, column=0, pady=10, sticky="NSEW")
plotfile_button.grid(row=4, column=0, pady=10, sticky="NSEW")

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
label.grid_configure(sticky="NSEW")
run_button.grid_configure(sticky="NSEW")
edit_button.grid_configure(sticky="NSEW")
plot_button.grid_configure(sticky="NSEW")
plotfile_button.grid_configure(sticky="NSEW")


window.mainloop()