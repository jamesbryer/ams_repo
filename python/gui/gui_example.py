import tkinter


def strip_vowels():
    global label
    label.destroy()
    string = input1.get()
    label = tkinter.Label(root, text=''.join(
        char for char in string if char not in "aeiouAEIUO"))
    label.grid(row=2, column=1)


root = tkinter.Tk(className="Vowel Stripper 3000")

label = tkinter.Label(root, text="Hello, World!")
input1 = tkinter.Entry(root)
input1.grid(row=1, column=1)

submit = tkinter.Button(root, text="Remove Vowels", command=strip_vowels)
submit.grid(row=1, column=2)

if __name__ == "__main__":
    root.mainloop()
