from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

root = Tk()
root.state("zoomed")# for full screen can change to preferred size
root.title("Picture Modifier")

cbthumbnail = IntVar()
# Frames to keep Entry boxes lined up!!! Pain in the ass without
frame = Frame(root, width=500, height=500, bg="white")
frame.grid(row=2, column=1, padx=10, columnspan=2, pady=20)

frame2 = Frame(root, width=500, height=500, bg="white")
frame2.grid(row=2, column=4, columnspan=2, padx=20, sticky='e')

frame5 = Frame(root, width=100, height=500)
frame5.grid(row=2, column=6, sticky='w')

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
sharp_img = None
blurr_img = None
tnail_image = None


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

        # Create a Canvas for the image
        canvas = Canvas(frame, bg="white", width=500, height=500)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Add scrollbars to the Canvas
        h_scroll = Scrollbar(frame, orient=HORIZONTAL, command=canvas.xview)
        h_scroll.grid(row=1, column=0, sticky="ew")
        v_scroll = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        v_scroll.grid(row=0, column=1, sticky="ns")

        canvas.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

        # Set the scrollable region to match the image size
        canvas.config(scrollregion=(0, 0, img_to_filter.width, img_to_filter.height))

        # Display the image on the Canvas
        canvas.create_image(0, 0, anchor=NW, image=global_image)

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
        
         # Create a Canvas for the image
        canvas = Canvas(frame2, bg="white", width=500, height=500)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Add scrollbars to the Canvas
        h_scroll = Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
        h_scroll.grid(row=1, column=0, sticky="ew")
        v_scroll = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
        v_scroll.grid(row=0, column=1, sticky="ns")

        canvas.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

        # Set the scrollable region to match the image size
        canvas.config(scrollregion=(0, 0, img_to_filter.width, img_to_filter.height))

        # Display the image on the Canvas
        canvas.create_image(0, 0, anchor=NW, image=filtered_image)


def resize():
    global img_to_filter, global_resized_image, re_sized_img, tnail_image  # Prevent garbage collection
   
    if img_to_filter is not None:  # Check if there is an image to process
        if cbthumbnail.get() == 1:  # Check if the thumbnail checkbox is checked
            tsize = (100, 100)  # Thumbnail dimensions
            img_to_filter.thumbnail(tsize)  # Modify the image in place
            global_resized_image = ImageTk.PhotoImage(img_to_filter)  # Prepare thumbnail for display
            tnail_image = img_to_filter  # Save the thumbnail image reference
        else:
            # If checkbox is not checked, resize to given dimensions
            imgw = rswidth.get()
            imgh = rsheight.get()
            rs = img_to_filter.resize((int(imgw), int(imgh)), Image.Resampling.LANCZOS)
            global_resized_image = ImageTk.PhotoImage(rs)
            re_sized_img = rs
      
        
        # Clear previous content in frame2 and display the resized image
        for widget in frame2.winfo_children():
            widget.destroy()
        
         # Create a Canvas for the image
        canvas = Canvas(frame2, bg="white", width=500, height=500)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Add scrollbars to the Canvas
        h_scroll = Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
        h_scroll.grid(row=1, column=0, sticky="ew")
        v_scroll = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
        v_scroll.grid(row=0, column=1, sticky="ns")

        canvas.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

        # Set the scrollable region to match the image size
        canvas.config(scrollregion=(0, 0, img_to_filter.width, img_to_filter.height))

        # Display the image on the Canvas
        canvas.create_image(0, 0, anchor=NW, image=global_resized_image)

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
        
         # Create a Canvas for the image
        canvas = Canvas(frame2, bg="white", width=500, height=500)
        canvas.grid(row=0, column=0, sticky="nsew")

        # Add scrollbars to the Canvas
        h_scroll = Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
        h_scroll.grid(row=1, column=0, sticky="ew")
        v_scroll = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
        v_scroll.grid(row=0, column=1, sticky="ns")

        canvas.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

        # Set the scrollable region to match the image size
        canvas.config(scrollregion=(0, 0, img_to_filter.width, img_to_filter.height))

        # Display the image on the Canvas
        canvas.create_image(0, 0, anchor=NW, image=global_rotate_image)

        
        rtamount.delete(0, END) # empty entry box
        
def sharpinImage():
       global img_to_filter, filtered_image_sharp, sharp_img # Prevent garbage collection
    
       if img_to_filter is not None:  # Check if there is an image to process
          # Convert to greyscale
          sh = img_to_filter.filter(ImageFilter.DETAIL)
          filtered_image_sharp = ImageTk.PhotoImage(sh)
          sharp_img = sh
          # Clear previous content in frame2 and display the greyscale image
          for widget in frame2.winfo_children():
              widget.destroy()
        
          # Create a Canvas for the image
          canvas = Canvas(frame2, bg="white", width=500, height=500)
          canvas.grid(row=0, column=0, sticky="nsew")

          # Add scrollbars to the Canvas
          h_scroll = Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
          h_scroll.grid(row=1, column=0, sticky="ew")
          v_scroll = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
          v_scroll.grid(row=0, column=1, sticky="ns")

          canvas.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

        # Set the scrollable region to match the image size
          canvas.config(scrollregion=(0, 0, img_to_filter.width, img_to_filter.height))

        # Display the image on the Canvas
          canvas.create_image(0, 0, anchor=NW, image=filtered_image_sharp)

          
          
def imageblur():
      global img_to_filter, filtered_image_blur, blurr_img # Prevent garbage collection
    
      if img_to_filter is not None:  # Check if there is an image to process
          # Blur image
          ib = img_to_filter.filter(ImageFilter.BLUR)
          filtered_image_blur = ImageTk.PhotoImage(ib)
          blurr_img = ib
          # Clear previous content in frame2 and display the greyscale image
          for widget in frame2.winfo_children():
              widget.destroy()
        
           # Create a Canvas for the image
          canvas = Canvas(frame2, bg="white", width=500, height=500)
          canvas.grid(row=0, column=0, sticky="nsew")

          # Add scrollbars to the Canvas
          h_scroll = Scrollbar(frame2, orient=HORIZONTAL, command=canvas.xview)
          h_scroll.grid(row=1, column=0, sticky="ew")
          v_scroll = Scrollbar(frame2, orient=VERTICAL, command=canvas.yview)
          v_scroll.grid(row=0, column=1, sticky="ns")

          canvas.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

          # Set the scrollable region to match the image size
          canvas.config(scrollregion=(0, 0, img_to_filter.width, img_to_filter.height))

          # Display the image on the Canvas
          canvas.create_image(0, 0, anchor=NW, image=filtered_image_blur)
      
          
def save_as():
    global rotated_img, re_sized_img, greyscale_img, sharp_img, blurr_img, tnail_image, savepic  # Access the currently modified image
    
    if rotated_img is not None:
        savepic = rotated_img
    if re_sized_img is not None:
        savepic = re_sized_img
    if greyscale_img is not None:
        savepic = greyscale_img 
    if sharp_img is not None:
        savepic = sharp_img
    if blurr_img is not None:
        savepic = blurr_img    
    if tnail_image is not None:
        savepic = tnail_image           
    
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
            sharp_img = None
            blurr_img = None
            tnail_image = None
    else:
        print("No image to save!")  # Debugging message or replace with a Tkinter messagebox        
        
##--------------------------------GUI BUTTONS---------------------------------------------------#
# file explorer
imagebtn = Button(root, text="Get Image", width=15, height=3, command=open_file_explorer)
imagebtn.grid(row=0, column=1, padx=20, sticky='ns')

# greyscale button
greybtn = Button(frame5, text="Greyscale", width=15, height=2, command=greyscale)
greybtn.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# resize button
rsbutton = Button(frame5, text="Resize", width=15, height=2, command=resize)
rsbutton.grid(row=1, column=0, padx=10, pady=10, sticky='w')

# rotate button
rtbutton = Button(frame5, text="Rotate", width=15, height=2, command=rotateimage)
rtbutton.grid(row=2, column=0, padx=10, pady=0, sticky='w')

saveasbutton = Button(root, text="Save Pic", width=10, height=2, command=save_as)
saveasbutton.grid(row=3, column=4, sticky='e')
#----------------Resize-----------------------------------------#
rswidth = Entry(frame5, width=8)
rswidth.grid(row=1, column=1, sticky='w')
  
rslabelw = Label(frame5, text="Width")
rslabelw.grid(row=1, column=1, sticky='n')

rsheight = Entry(frame5, width=8)
rsheight.grid(row=1, column=2, padx=5, sticky='w')

rslabelh = Label(frame5, text='Height')
rslabelh.grid(row=1, column=2, sticky='n')

checkthumbnail = Checkbutton(frame5, text="Thumbnail (100x100)", variable=cbthumbnail, onvalue=1, offvalue=0)
checkthumbnail.grid(row=1, column=3, sticky='w')

#---------------------ROTATE---------------------------------------------# 

rtamount = Entry(frame5, width=8)
rtamount.grid(row=2, column=1, pady=25, sticky='w')

rtlabel = Label(frame5, text="degrees")
rtlabel.grid(row=2, column=1, pady=0, sticky='n')

#--------------------SharpinBTN--------------------------------------------------#

sharpinbtn = Button(frame5, text='Sharpen', width=15, height=2, command=sharpinImage)
sharpinbtn.grid(row=3, column=0, padx=10, pady=15, sticky='w')

#-----------------------BLUR BTN-------------------------------------------#

blurbtn = Button(frame5, text="BLUR", width=15, height=2, command=imageblur)
blurbtn.grid(row=4, column=0, padx=10, pady=10, sticky='w')




root.mainloop()