import tkinter
# create a simple file reader which displays file contents in a gui window using tkinter
# the window should have a text box for the file name, a button to read the file, and a text box to display the file contents
# the file name should be passed to the read_file function


def read_file():
    # read the file and display the contents in the label
    global label
    # destroy the label if it exists
    label.destroy()
    # get the file name from the input box
    file_name = input1.get()
    # try to open the file and display the contents in the label
    try:
        with open(file_name, 'r') as file:
            label = tkinter.Label(root, text=file.read())
            label.grid(row=2, column=1)
    # if the file is not found, display an error message
    except FileNotFoundError:
        label = tkinter.Label(root, text="File not found")
        label.grid(row=2, column=1)


# create the gui
root = tkinter.Tk(className="File Reader")
# create the label, input box, and button
label = tkinter.Label(root, text="")
input1 = tkinter.Entry(root)
submit = tkinter.Button(root, text="Read File", command=read_file)

# place the label, input box, and button in the window
input1.grid(row=1, column=1)
submit.grid(row=1, column=2)

# run the gui
if __name__ == "__main__":
    root.mainloop()
