from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

root = Tk()
root.state("zoomed")# for full screen can change to preferred size
root.title("Picture Modifier")

msg = StringVar()
# Frames to keep Entry boxes lined up!!! Pain in the ass without
frame = Frame(root, width=500, height=500, bg="white")
frame.grid(row=2, column=1, padx=10, columnspan=2, pady=20)

frame2 = Frame(root, width=500, height=500, bg="white")
frame2.grid(row=2, column=4, columnspan=2, padx=20, sticky='e')

frame3 = Frame(root)
frame3.grid(row=4, column=1, sticky='w')  

frame4 = Frame(root)
frame4.grid(row=5, column=1, sticky='w')

frame5 = Frame(root, width=100, height=500)
frame5.grid(row=2, column=6, sticky='w')

# Global variables
crop_box_coords = None  # Store crop box coordinates
crop_rectangle = None  # Store the rectangle object
cbvariable = IntVar() #thumbnail checkbox

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
canvas = None
cropped_img = None


def open_file_explorer():
    
    global global_image, img_to_filter # Prevent garbage collection
    
    file_path = filedialog.askopenfilename()
    
    if file_path:  # Check if the user selected a file
        # Open the image file and store it
        img_to_filter = Image.open(file_path)
        
        # Create a Tkinter-compatible image for display
        global_image = ImageTk.PhotoImage(img_to_filter)
        
        # Clear previous content in the frame and display the new image
        for widget in frame.winfo_children():
            widget.destroy()
        
            # Create a canvas to hold the label
    pframe1()

    

def pframe1(): # source picture holder
    global canvas
    canvas = Canvas(frame, width=500, height=500, bg="white", scrollregion=(0, 0, 1000, 1000))
    canvas.pack(fill=BOTH, expand=True)

    # Add vertical scrollbar
    v_scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    v_scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=v_scrollbar.set)

    # Add horizontal scrollbar (optional)
    h_scrollbar = Scrollbar(frame, orient="horizontal", command=canvas.xview)
    h_scrollbar.pack(side="bottom", fill="x")
    canvas.configure(xscrollcommand=h_scrollbar.set)

    canvas.create_image(0, 0, anchor="nw", image=global_image)
    canvas.image = global_image  # Save reference to prevent garbage collection
    
    
def pframe2():  # modified picture holder
    global canvas, filtered_image
    canvas = Canvas(frame2, width=500, height=500, bg="white", scrollregion=(0, 0, 1000, 1000))
    canvas.pack(fill=BOTH, expand=True)

    # Add vertical scrollbar
    v_scrollbar = Scrollbar(frame2, orient="vertical", command=canvas.yview)
    v_scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=v_scrollbar.set)

    # Add horizontal scrollbar (optional)
    h_scrollbar = Scrollbar(frame2, orient="horizontal", command=canvas.xview)
    h_scrollbar.pack(side="bottom", fill="x")
    canvas.configure(xscrollcommand=h_scrollbar.set)

    # Directly display the image on the canvas

    canvas.create_image(0, 0, anchor="nw", image=filtered_image)
    canvas.image = filtered_image  # Save reference to prevent garbage collection    
    
    
    
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
    pframe2()
        
    
def resize():
    global img_to_filter, global_resized_image, re_sized_img, filtered_image, cbvariable  # Prevent garbage collection
    
    tsize = (100, 100)
    imgw = rswidth.get()
    imgh = rsheight.get()
    
    if img_to_filter is not None:  # Check if there is an image to process
        # Resize the image
        if img_to_filter is not None:  # Check if there is an image to process
          if cbvariable.get() == 1:  # Check if the thumbnail checkbox is selected
          # Create a thumbnail
           img_to_filter_copy = img_to_filter.copy()  # Use a copy to avoid modifying the original
           img_to_filter_copy.thumbnail(tsize)
           global_resized_image = ImageTk.PhotoImage(img_to_filter_copy)
           re_sized_img = img_to_filter_copy
           filtered_image = global_resized_image  # Assign the thumbnail to `filtered_image`
          else:
             rs = img_to_filter.resize((int(imgw), int(imgh)), Image.Resampling.LANCZOS)
             filtered_image = ImageTk.PhotoImage(rs)
             re_sized_img = rs
        
   
    for widget in frame2.winfo_children():
        widget.destroy()
        
    pframe2()
    cbvariable = 0
    rswidth.delete(0, END)
    rsheight.delete(0, END)
    
    
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
        
    pframe2()
    
    rtamount.delete(0, END) # empty entry box
        
def sharpinImage():
    global img_to_filter, filtered_image, sharp_img # Prevent garbage collection
    
    if img_to_filter is not None:  # Check if there is an image to process
          # Sharpen image
          sh = img_to_filter.filter(ImageFilter.DETAIL)
          filtered_image = ImageTk.PhotoImage(sh)
          sharp_img = sh
         
          for widget in frame2.winfo_children():
              widget.destroy()
        
    pframe2()
          
          
def imageblur():
      global img_to_filter, filtered_image, blurr_img # Prevent garbage collection
    
      if img_to_filter is not None:  # Check if there is an image to process
          # Blur image
          ib = img_to_filter.filter(ImageFilter.BLUR)
          filtered_image = ImageTk.PhotoImage(ib)
          blurr_img = ib
          # Clear previous content in frame2 and display the greyscale image
          for widget in frame2.winfo_children():
              widget.destroy()
        
          pframe2()
          
          
def enable_crop_box():
      global crop_rectangle, crop_box_coords
      crop_rectangle = None  # Initialize the crop rectangle
      crop_box_coords = None  # Initialize crop box coordinates
    
      if canvas:  
          
         canvas.bind("<Button-1>", create_crop_box)  # Left-click to create crop box
         canvas.bind("<B1-Motion>", update_crop_box)  # Drag mouse to adjust crop box
         msg.set("Crop box enabled. Click and drag to adjust then press crop button to crop")
      else:
         msg.set("Canvas not initialized. Please create or display the canvas first.")
     
def create_crop_box(event):
    global crop_rectangle, crop_box_coords
    x, y = event.x, event.y  
    crop_box_coords = (x, y, x, y)  # Initialize the crop box with starting and ending points being the same
    if crop_rectangle:  # Delete the existing rectangle if there is one
        canvas.delete(crop_rectangle)
    crop_rectangle = canvas.create_rectangle(
        crop_box_coords, outline="red", width=2 
    )
    
    
# Update crop box position
def update_crop_box(event):
    global crop_rectangle, crop_box_coords
    x1, y1, x2, y2 = crop_box_coords  # Unpack current coordinates
    x2, y2 = event.x, event.y  # Update the ending coordinates to the current mouse position
    crop_box_coords = (x1, y1, x2, y2)  # Update the coordinates globally
    canvas.coords(crop_rectangle, crop_box_coords)  # Dynamically adjust the rectangle dimension
    
    

def crop_image():
     global crop_box_coords, img_to_filter, cropped_img
     if img_to_filter is not None and crop_box_coords is not None:
        # Extract the defined crop box coordinates
        x1, y1, x2, y2 = crop_box_coords
        crop_box = (x1, y1, x2, y2)

        # Crop the image based on the crop box
        cropped_img = img_to_filter.crop(crop_box)  # Save as a PIL.Image object

        # Display the cropped image in frame2
        display_cropped_image(cropped_img)
                     
def display_cropped_image(image):
    global cropped_img  
    for widget in frame2.winfo_children():
        widget.destroy()  # Clear previous content in frame2

    # Create a canvas in frame2 to display the cropped image
    cropped_canvas = Canvas(frame2, width=500, height=500, bg="white")
    cropped_canvas.pack(fill=BOTH, expand=True)

    # Convert to Tkinter-compatible image for display
    tk_image = ImageTk.PhotoImage(image)
    cropped_canvas.create_image(0, 0, anchor="nw", image=tk_image)
    cropped_canvas.image = tk_image  # Prevent garbage collection
          
def save_as():
    global rotated_img, re_sized_img, greyscale_img, sharp_img, blurr_img, cropped_img, savepic  # Access the currently modified image
    
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
    if cropped_img is not None: 
        savepic = cropped_img           
    
    if savepic is not None:  # Check if there's an image to save

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
        
        if file_path:  
            # Save the image to the selected path
            savepic.save(file_path)
            greyscale_img = None
            re_sized_img = None # reset images
            rotated_img = None
            sharp_img = None
            blurr_img = None
            cropped_img = None
    else:
        msg.set("No image to save!")  # Debugging message
        
        

def exitprg():
    exit()                
      
##--------------------------------GUI BUTTONS---------------------------------------------------#
# file explorer
imagebtn = Button(root, text="Get Image", width=15, height=3, command=open_file_explorer)
imagebtn.grid(row=0, column=1, padx=180, pady=10, sticky='ns')

# greyscale button
greybtn = Button(frame5, text="Greyscale", width=15, height=2, command=greyscale)
greybtn.grid(row=0, column=0, padx=10, pady=5, sticky='nw')

# resize button
rsbutton = Button(frame5, text="Resize", width=15, height=2, command=resize)
rsbutton.grid(row=1, column=0, padx=10, pady=10, sticky='w')

# rotate button
rtbutton = Button(frame5, text="Rotate", width=15, height=2, command=rotateimage)
rtbutton.grid(row=2, column=0, padx=10, pady=5, sticky='w')

cropimgbtn = Button(frame5, text="CROP", width=15, height=2, command=crop_image)
cropimgbtn.grid(row=6, column=0, padx=10, pady=5, sticky='w')

saveasbutton = Button(root, text="Save Pic", width=15, height=2, command=save_as)
saveasbutton.grid(row=3, column=4, sticky='e')

#----------------Resize-----------------------------------------#
rswidth = Entry(frame5, width=8)
rswidth.grid(row=1, column=1, padx= 40, sticky='w')
  
rslabelw = Label(frame5, text="Width")
rslabelw.grid(row=1, column=1, sticky='w')

rsheight = Entry(frame5, width=8)
rsheight.grid(row=1, column=2, sticky='w')

rslabelh = Label(frame5, text='Height')
rslabelh.grid(row=1, column=1, sticky='e') 

rscheck = Checkbutton(frame5, text="thumbnail (100x100)", variable=cbvariable, onvalue=1, offvalue=0)
rscheck.grid(row=1, column=3, padx=10, sticky='e')

#---------------------ROTATE---------------------------------------------# 

rtamount = Entry(frame5, width=8)
rtamount.grid(row=2, column=1, padx=50, sticky='w')

rtlabel = Label(frame5, text="degrees")
rtlabel.grid(row=2, column=1, padx=1, sticky='w')

#--------------------SharpinBTN--------------------------------------------------#

sharpinbtn = Button(frame5, text='Sharpen', width=15, height=2, command=sharpinImage)
sharpinbtn.grid(row=3, column=0, padx=10, pady=10, sticky='w')

#-----------------------BLUR BTN-------------------------------------------#

blurbtn = Button(frame5, text="BLUR", width=15, height=2, command=imageblur)
blurbtn.grid(row=4, column=0, padx=10, pady=5, sticky='w')

#-------------------CROP BOX-----------------------------------------------#

cropboxbtn = Button(frame5, text="CROP BOX", width=15, height=2, command=enable_crop_box)
cropboxbtn.grid(row=6, column=1, padx=10,pady=10, sticky='w')

#------------------------MSG LABEL--------------------------------------#
msglabel = Label(frame3, textvariable=msg, font='Arial', fg='blue')
msglabel.grid(row=0, column=0, sticky='w')

#---------------------EXIT---------------------------------------------#
exitbtn = Button(frame5, text="EXIT", width=15, height=2, command=exitprg)
exitbtn.grid(row=7, column=0, padx=10)

root.mainloop()
