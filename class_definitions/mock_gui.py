"""Used to mock up and test gui look, feel, and positioning"""
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
# set the initial window size (width, height)
win.minsize(300, 250)
win.attributes("-topmost", True)
win.title("EDMA")

# label to change on click
f_label = ttk.Label(win, text="first (Top) Label")
f_label.grid(row=0, sticky=tk.W, column=0)


def click_action():
    """
    handles button click actions to change label text
    """
    f_label.configure(text='Hello ' + name.get() + ' ' + chosen.get())


# input field
name = tk.StringVar()
name_entry = ttk.Entry(win, width=30, textvariable=name)
name_entry.grid(row=1, sticky=tk.W, column=0)
name_entry.focus()

# combo box selection label
comb_box = ttk.Label(win, text='Choose:')
comb_box.grid(row=2, sticky=tk.W, column=0)

# combo box selection
choice = tk.StringVar()
chosen = ttk.Combobox(win, width=15, textvariable=choice, state='readonly')
# tuple of values to choose from
chosen['values'] = (
    ', U goof!', ', Mr. Smarty', ', U Nerd', ', U poo poo face.')
chosen.grid(row=2, column=0)
chosen.current(0)

# button to call click_action to change label with textvariable/StringVar
action_btn = ttk.Button(win, text='Submit', command=click_action)
action_btn.grid(row=3, column=0)

# radio buttons global values
# COLOR1 = '#44bcd8'
# COLOR2 = '#195e83'
# COLOR3 = '#1979a9'
colors = ['#44bcd8', '#195e83', '#1979a9']


# radio btn callback
def radCall():
    rad_select = radVar.get()
    if rad_select == 0:
        win.configure(background=colors[0])
    elif rad_select == 1:
        win.configure(background=colors[1])
    elif rad_select == 2:
        win.configure(background=colors[2])


# 3 radio btn's using one var
radVar = tk.IntVar()
# set to non-existing index value
radVar.set(99)
"""
rad1 = tk.Radiobutton(win, text='Blue ' + COLOR1, variable=radVar, value=1,
                      command=radCall)
rad1.grid(row=4, column=0, sticky=tk.W)

rad2 = tk.Radiobutton(win, text='Blue ' + COLOR2, variable=radVar, value=2,
                      command=radCall)
rad2.grid(row=5, column=0, sticky=tk.W)

rad3 = tk.Radiobutton(win, text='Blue ' + COLOR3, variable=radVar, value=3,
                      command=radCall)
rad3.grid(row=6, column=0, sticky=tk.W)"""
# re-create the radio btn's with one loop
for color in range(3):
    curRad = 'rad' + str(color )
    curRad = tk.Radiobutton(win, text='Blue ' + colors[color], variable=radVar,
                            value=color,
                            command=radCall)
    # place the radio btn in the next row by adding the col to the row number
    curRad.grid(row=4+color, sticky=tk.W, column=0)

# scroll text control wrap by word not char
scrollW = 25
scrollH = 5
scroll = scrolledtext.ScrolledText(win, width=scrollW, height=scrollH,
                                   wrap=tk.WORD)
scroll.grid(row=7, column=0)

# container to hold multiple labels
labels_frame = ttk.LabelFrame(win, text='Labels in a frame')
labels_frame.grid(row=8, sticky=tk.W, column=0, padx=7, pady=7)

# place the labels in the parent 'labels_frame' not 'win'  - vert
ttk.Label(labels_frame, text='Label A').grid(row=0, sticky=tk.W, column=0)
ttk.Label(labels_frame, text='Label B').grid(row=1, sticky=tk.W, column=0)
ttk.Label(labels_frame, text='Label C').grid(row=2, sticky=tk.W, column=0)
# place the labels in the parent 'labels_frame' not 'win'  - horz
ttk.Label(labels_frame, text='').grid(row=3, sticky=tk.W, column=0)  # empty
ttk.Label(labels_frame, text='Label D').grid(row=4, sticky=tk.W, column=0)
ttk.Label(labels_frame, text='Label E').grid(row=4, sticky=tk.W, column=1)
ttk.Label(labels_frame, text='Label F').grid(row=4, sticky=tk.W, column=2)
ttk.Label(labels_frame, text='Label G').grid(row=4, sticky=tk.W, column=3)
ttk.Label(labels_frame, text='Label H').grid(row=4, sticky=tk.W, column=4)

win.mainloop()
