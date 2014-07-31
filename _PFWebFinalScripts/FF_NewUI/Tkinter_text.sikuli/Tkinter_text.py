#http://stackoverflow.com/questions/21840133/how-to-display-text-on-the-screen-without-a-window-using-python
import Tkinter
label = Tkinter.Label(text='Text on the screen', font=('Times','30'), fg='black', bg='white')
label.master.overrideredirect(True)
label.master.geometry("+250+250")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()