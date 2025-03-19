from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.state("zoomed")# for full screen can change to preferred size

# Frames to keep Entry boxes lined up!!! Pain in the ass without
frame = Frame(root, width=500, height=500, bg="white")
frame.grid(row=2, column=1, padx=10, columnspan=2, pady=20)

frame2 = Frame(root, width=500, height=500, bg="white")
frame2.grid(row=2, column=4, columnspan=2, padx=20, sticky='e')

frame3 = Frame(root)
frame3.grid(row=4, column=1, sticky='w')  

frame4 = Frame(root)
frame4.grid(row=5, column=1, sticky='w')



# Global variables to store image objects
global_image = None
global_resized_image = None
img_to_filter = None
global_rotate_image = None
greyscale_img = None
rotated_img = None
re_sized_img = None


def open_file_explorer():
    
    global global_image, img_to_filter  # Prevent garbage collection
    
    file_path = filedialog.askopenfilename()
    
    if file_path:  # Check if the user selected a file
        # Open the image file and store it
        img_to_filter = Image.open(file_path)
        
        # Create a Tkinter-compatible image for display
        global_image = ImageTk.PhotoImage(img_to_filter)
        
        # Clear previous content in the frame and display the new image
        for widget in frame.winfo_children():
            widget.destroy()
        
        image_label = Label(frame, image=global_image, width=500, height=500, bg="white") # create holder label for pic
        image_label.pack()

def greyscale():
    global img_to_filter, filtered_image, greyscale_img # Prevent garbage collection
    
    if img_to_filter is not None:  # Check if there is an image to process
        # Convert to greyscale
        gs = img_to_filter.convert('L')
        filtered_image = ImageTk.PhotoImage(gs)
        greyscale_img = gs
        # Clear previous content in frame2 and display the greyscale image
        for widget in frame2.winfo_children():
            widget.destroy()
        
        f_image_label = Label(frame2, image=filtered_image, width=500, height=500,  bg="white")
        f_image_label.image = filtered_image # Save reference to prevent garbage collection
        
        f_image_label.pack()

def resize():
    global img_to_filter, global_resized_image, re_sized_img  # Prevent garbage collection
    
    imgw = rswidth.get()
    imgh = rsheight.get()
    
    if img_to_filter is not None:  # Check if there is an image to process
        # Resize the image
        rs = img_to_filter.resize((int(imgw), int(imgh)), Image.Resampling.LANCZOS)
        global_resized_image = ImageTk.PhotoImage(rs)
        re_sized_img = rs
        
        # Clear previous content in frame2 and display the resized image
        for widget in frame2.winfo_children():
            widget.destroy()
        
        f_image_label = Label(frame2, image=global_resized_image, bg="white")
        f_image_label.image = global_resized_image  # Save reference to prevent garbage collection
        f_image_label.pack()
        rsheight.delete(0, END) # clear box after processing
        rswidth.delete(0, END) # clear box after processing

def rotateimage():
    
    global img_to_filter, global_rotate_image , rotated_img # Prevent garbage collection
    degrot = rtamount.get()
    if img_to_filter is not None:  # Check if there is an image to process
        
        rt = img_to_filter.rotate(int(degrot))
        global_rotate_image = ImageTk.PhotoImage(rt)
        rotated_img = rt
        # Clear previous content
        for widget in frame2.winfo_children():
            widget.destroy()
        
        f_image_label = Label(frame2, image=global_rotate_image, width=500, height=500, bg="white")#force label not to resize
        f_image_label.image = global_rotate_image  # Save reference to prevent garbage collection
        f_image_label.pack()
        
        rtamount.delete(0, END) # empty entry box
        
        
def save_as():
    global rotated_img, re_sized_img, greyscale_img, savepic  # Access the currently modified image
    
    if rotated_img is not None:
        savepic = rotated_img
    if re_sized_img is not None:
        savepic = re_sized_img
    if greyscale_img is not None:
        savepic = greyscale_img        
    
    if savepic is not None:  # Check if there's an image to save
        # Ask the user where to save the image
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",  # Default file format
            filetypes=[
                ("JPEG files", "*.jpg"),
                ("Bitmap files", "*.bmp"),
                ("PNG files", "*.png"),
                ("GIF files", "*.gif"),
                ("TIFF files", "*.tiff")
            ],
        )
        
        if file_path:  # If the user selects a path
            # Save the image to the selected path
            savepic.save(file_path)
            greyscale_img = None
            re_sized_img = None # reset images
            rotated_img = None
    else:
        print("No image to save!")  # Debugging message or replace with a Tkinter messagebox        
        
##--------------------------------GUI BUTTONS---------------------------------------------------#
# file explorer
imagebtn = Button(root, text="Get Image", width=15, height=3, command=open_file_explorer)
imagebtn.grid(row=0, column=1, padx=20, sticky='ns')

# greyscale button
greybtn = Button(root, text="Greyscale", width=15, height=2, command=greyscale)
greybtn.grid(row=3, column=1, padx=10, sticky='w')

# resize button
rsbutton = Button(frame3, text="Resize", width=15, height=2, command=resize)
rsbutton.grid(row=0, column=0, padx=10, pady=15, sticky='w')

# rotate button
rtbutton = Button(frame4, text="Rotate", width=15, height=2, command=rotateimage)
rtbutton.grid(row=0, column=0, padx=10, pady=15, sticky='w')

saveasbutton = Button(root, text="Save Pic", width=15, height=2, command=save_as)
saveasbutton.grid(row=3, column=4, sticky='e')
#----------------Resize-----------------------------------------#
rswidth = Entry(frame3, width=8)
rswidth.grid(row=0, column=1, padx=(0, 5), sticky='w')
  
rslabelw = Label(frame3, text="Width")
rslabelw.grid(row=0, column=1, sticky='n')

rsheight = Entry(frame3, width=8)
rsheight.grid(row=0, column=2, sticky='w')

rslabelh = Label(frame3, text='Height')
rslabelh.grid(row=0, column=2, sticky='n') 

#---------------------ROTATE---------------------------------------------# 

rtamount = Entry(frame4, width=8)
rtamount.grid(row=0, column=1, padx=(0,5), sticky='w')

rtlabel = Label(frame4, text="degrees")
rtlabel.grid(row=0, column=1, sticky='n')

#-----------------------------------------------------------------------------#

root.mainloop()