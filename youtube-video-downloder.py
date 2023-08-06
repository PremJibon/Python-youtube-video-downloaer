import tkinter,customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Youtube link is invalid")
    print("download complete")
#system Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding UI Elements
title = customtkinter.CTkLabel(app,text='Insert a youtube link')
title.pack(padx=10,pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable=url_var)
link.pack()

#download button
download = customtkinter.CTkButton(app,text='Download',command=startDownload)
download.pack(padx=10,pady=10)
#Run app
app.mainloop()