import Tkinter as tk
import tkFileDialog
import tkMessageBox

from PIL import Image, ImageTk
import redbits

class Application(tk.Frame):
    def browse_files(self):
        try:
            # Open file selection dialog
            filename = tkFileDialog.askopenfilename(filetypes=[('PNG Files', '*.png')])
            # Process image, only
            if filename != None and len(filename) > 0:
                self.process_image(filename)
        except Exception as e:
            # Alert user to error
            tkMessageBox.showerror("Error", "Error choosing file.")
            print(e)
    
    def process_image(self, filename):
        try:
            # Load image
            im = Image.open(filename)
            # Create image processor
            rb = redbits.Redbits()
            # Process the image
            processed_image = rb.process(im)
            # Release loaded image from memory
            im.close()
            # Display the image
            tkimage = ImageTk.PhotoImage(processed_image)
            self.panel.configure(image = tkimage)
            self.panel.image = tkimage
            self.panel.pack(side="left", fill="both", expand="yes")
        except Exception as e:
            # Alert user to error
            tkMessageBox.showerror("Error", "Error processing image file.")   
            print(e)       

    def create_widgets(self):
        # Create browse button
        self.btn_browse_files = tk.Button(self)
        self.btn_browse_files["text"] = "Browse"
        self.btn_browse_files["command"] = self.browse_files
        self.btn_browse_files.pack(side="left", expand=1)

        # Create image panel
        self.panel = tk.Label(self.master)
        self.panel.pack(side="left", fill="both", expand="yes")
    
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        if master != None:
            master.title("Redbits")
            master.minsize(500, 600)
            master.resizable(width=False, height=False)

        self.pack()
        self.create_widgets()

root = tk.Tk()
app = Application(master=root)
app.mainloop()

try:
    # TODO: Using the exit button causes and error. Why>
    root.destroy()
except:
    pass