import tkinter as tk
root = tk.Tk()
frame = tk.Frame(root)


def do_something_with_usr_name(name):
    print(name)
    # ^ replace this with your code. name should be a string containing the username


# create the window
root.title("menu")
frame.pack()

# Make a label telling the user what to do
howto = tk.Label(
    root,
    text="put username below then press button")

# create a writeable box for the name
box_input = tk.Text(root,
                    height=1,
                    width=49)

# create the button that gets the name and runs function
output = tk.Button(root,
                   text="button",
                   command=lambda: do_something_with_usr_name(str(box_input.get("1.0", 'end-1c'))))
#     allows func parameters ^     run the function ^          ^  get the text inside the box   ^

# insert them all into the frame
howto.pack(side=tk.TOP)
box_input.pack(side=tk.TOP)
output.pack(side=tk.BOTTOM)

root.mainloop()