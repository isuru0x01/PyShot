from tkinter import *
from mss import mss
import crop_and_save


root = Tk()
root.title('PyShot 1.0')
root.iconbitmap('favicon.ico')
root.geometry("500x200")

def shot():
    with mss() as sct:
        # Designate the filename
        filename = sct.shot(output="input\output.png")
        # Confirm message
        notification_label.config(text="Screenshot has been saved!")
        crop_and_save.crop_save()
        #ocr.extract_text()


screenshot_button = Button(root, text="Take A Screenshot!", font=("Helvetica", 24), command=shot)
screenshot_button.pack(pady=40)

notification_label = Label(root, text="")
notification_label.pack(pady=10)

root.mainloop()