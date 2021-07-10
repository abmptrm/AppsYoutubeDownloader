from tkinter import * 
import tkinter.messagebox
from pytube import YouTube


class AppYtDown():
    def __init__(self, root):
        self.root = root
        self.root.title("Youtube Downloader")

        canvas = Canvas(root, width=600, height=590)
        canvas.grid(columnspan=5, rowspan=5)

        # logo
        poto = PhotoImage(file="logo.png")
        potoLabel = Label(image=poto,  )
        potoLabel.image = poto
        potoLabel.grid(row=0, column=2)

        # var 
        url = StringVar()
        vid360 = StringVar()
        vid480 = StringVar()
        vid720 = StringVar()

        #intruksi
        intruksi = Label(root, text="Masukan Link Video", font=("Raleway",13, "bold"))
        # intruksi.grid(column=2, row=1)
        intruksi.place(x=200, y= 420)

        # func
        def iReset():
            url.set("")
            return

        def iExit():
            Exit = tkinter.messagebox.askyesno(
                "Youtube Downloader", "Kamu Yakin Mau Keluar ?")
            if Exit > 0:
                root.destroy()
                return           

        def Urlink():
            item = url.get()
            res1 = vid360.get()
            res2 = vid480.get()
            res3 = vid720.get()

            if res1:

                if item.isascii():

                    #item
                    yt = YouTube(item)
                    print(yt.title)
                    stream = yt.streams.filter(res="360p").first()
                    stream.download("VideoDownload")

                else:
                    tkinter.messagebox.showwarning(
                    "Youtube Downloader", "Goblok :v")
                    vid360.set("")
                    vid480.set("")
                    vid720.set("")

            elif res2:

                if item.isascii():

                    #item
                    yt = YouTube(item)
                    print(yt.title)
                    stream = yt.streams.filter(res="480p").first()
                    stream.download("VideoDownload")
                
                else:
                    tkinter.messagebox.showwarning(
                    "Youtube Downloader", "Goblok :v")
                    vid360.set("")
                    vid480.set("")
                    vid720.set("")
            
            elif res3:

                if item.isascii():

                    #item
                    yt = YouTube(item)
                    print(yt.title)
                    stream = yt.streams.filter(res="720p").first()
                    stream.download("VideoDownload")
                
                else:
                    tkinter.messagebox.showwarning(
                    "Youtube Downloader", "Goblok :v")
                    vid360.set("")
                    vid480.set("")
                    vid720.set("")
            
            else:
                tkinter.messagebox.showwarning(
                "Youtube Downloader", "Goblok :v")
                vid360.set("")
                vid480.set("")
                vid720.set("")


                
            tkinter.messagebox.showinfo("Youtube Downloader", "  Mantap :)  ")
                
            # else:
            #     tkinter.messagebox.showwarning(
            #     "Youtube Downloader", "Goblok :v")
            #     url.set("")
            #     return False

        #Link Entry
        self.linkUrl = Entry(root, 
            textvariable=url, width=25)
        self.linkUrl.grid(row=2, column=2 )

        #CheckButton
        self.check360 = Checkbutton(root, text="360", variable=vid360).place(x= 200, y=490)
        self.check480 = Checkbutton(root, text="480", variable=vid480).place(x= 280, y=490)
        self.check720 = Checkbutton(root, text="720", variable=vid720).place(x= 350, y=490)


        #Button Sumbit 
        self.btnSumbit = Button(root, text="Sumbit", command=Urlink,font=("Raleway", 10))
        self.btnSumbit.place(x=200, y=520)

        # Button Reset 
        self.ResetButton = Button(root, text="Reset",command=iReset,font=("Raleway", 10))
        self.ResetButton.place(x=280, y=520)

        #Button exit
        self.btnExit = Button(root, text="Exit", command=iExit,font=("Raleway", 10))
        self.btnExit.place(x=350, y=520)


if __name__ == "__main__":
    root = Tk()
    app = AppYtDown(root)
    root.mainloop()