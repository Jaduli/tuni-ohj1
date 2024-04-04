"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Xxxx Yyyyyy
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        self.__main_window = Tk()

        self.__value = 0
        self.__value_var = StringVar()
        self.__value_var.set(self.__value)

        self.__current_value_label = Label(self.__main_window, textvariable=self.__value_var) # Label displaying the current value of the counter.
        self.__current_value_label.pack(side="top")

        self.__reset_button = Button(self.__main_window, text="Reset", command=self.reset)         # Button which resets counter to zero.
        self.__reset_button.pack(side="left")

        self.__increase_button = Button(self.__main_window, text="Increase", command=self.increase)     # Button which increases the value of the counter by one.
        self.__increase_button.pack(side="left")

        self.__decrease_button = Button(self.__main_window, text="Decreace", command=self.decrease)     # Button which decreases the value of the counter by one.
        self.__decrease_button.pack(side="left")

        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)         # Button which quits the program.
        self.__quit_button.pack(side="left")

        self.__main_window.mainloop()
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

    # TODO: Implement the rest of the needed methods here.
    def reset(self):
        self.__value = 0
        self.update_var()

    def increase(self):
        self.__value += 1
        self.update_var()

    def decrease(self):
        self.__value -= 1
        self.update_var()

    def quit(self):
        self.__main_window.destroy()

    def update_var(self):
        self.__value_var.set(str(self.__value))


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
