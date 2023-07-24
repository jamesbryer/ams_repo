import tkinter
# create a simple file reader which displays file contents in a gui window using tkinter
# the window should have a text box for the file name, a button to read the file, and a text box to display the file contents
# the file name should be passed to the read_file function

import traceback


def read_file():
    global labels_frame
    labels_frame.destroy()
    labels_frame = tkinter.Frame(root)
    labels_frame.grid(row=2, column=1)

    file_name = input1.get()
    with open(file_name, 'r') as file:
        for idx, line in enumerate(file):
            label = tkinter.Label(
                labels_frame, text=str(idx + 1) + ": " + line.strip())
            label.grid(row=idx, column=0)


# create the gui
root = tkinter.Tk(className="File Reader")
# create the label, input box, and button
labels_frame = tkinter.Label(root, text="")
input1 = tkinter.Entry(root)
submit = tkinter.Button(root, text="Read File", command=read_file)

# place the label, input box, and button in the window
input1.grid(row=1, column=1)
submit.grid(row=1, column=2)

# run the gui
if __name__ == "__main__":
    root.mainloop()
