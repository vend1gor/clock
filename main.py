from tkinter import *
root = Tk()

c = Canvas(root, width=300, height=300, bg='white')
c.pack()

c.create_rectangle(10, 10, 290, 290,
                   width=3)
c.create_rectangle(20, 20, 280, 280,
                   width=3)
c.create_oval(20, 20, 280, 280,
              width=3,
              fill='grey70')
c.create_line(150, 150, 150, 50,
              width=3)
c.create_text(150, 30,
              text="12",
              font="Verdana 15")
c.create_text(270, 150,
              text="3",
              font="Verdana 15")
c.create_text(150, 270,
              text="6",
              font="Verdana 15")
c.create_text(30, 150,
              text="9",
              font="Verdana 15")
c.create_text(200, 50,
              text="1",
              font="Verdana 15")
c.create_text(245, 90,
              text="2",
              font="Verdana 15")
c.create_text(245, 210,
              text="4",
              font="Verdana 15")
c.create_text(200, 250,
              text="5",
              font="Verdana 15")
c.create_text(100, 250,
              text="7",
              font="Verdana 15")
c.create_text(50, 210,
              text="8",
              font="Verdana 15")
c.create_text(50, 90,
              text="10",
              font="Verdana 15")
c.create_text(100, 50,
              text="11",
              font="Verdana 15")




root=mainloop()