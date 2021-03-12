import tkinter
from tkinter import messagebox
from tkinter import filedialog
import Functions

# Variables
Usuario = ""
Palabra = ""
Suplente = bool(False)

# Window
gui = tkinter.Tk()
gui.title("Harper")
gui.iconbitmap("favicon.ico")
gui.resizable(Suplente, Suplente)
gui.geometry("655x445")
gui.config(bg="grey")


# Functions

# Función revisar user/contraseña y  desplegar menú

def get_usname(username, password):
    user = username.get()
    psword = password.get()
    if user == Usuario and psword == Palabra:
        barramenu.add_cascade(label="File", menu=filemenu)
        barramenu.add_cascade(label="Tools", menu=toolsmenu)
        barramenu.add_cascade(label="Console", menu=consolemenu)
        barramenu.add_cascade(label="Functions", menu=functionmenu)
        barramenu.add_cascade(label="Harper", menu=HarperMenu)
        gui.resizable(True, True)
        frametwo.destroy()
        frameone.destroy()
        framethree.pack(fill="both", expand=True)
    else:
        messagebox.showwarning("Alerta de seguridad",
                               "Un sujeto desconocido ha tratado de accesar, notificando a Cedarium...")


# Abrir Archivo

def open_file():
    global route
    route = filedialog.askopenfilename(
        initialdir=".",
        filetype=(("Open", "*.txt"),),
        title="Open File"
    )
    if route != "":
        fichero = open(route, "r")
        content = fichero.read()
        TextoArchivo.delete(1.0, "end")
        TextoArchivo.insert("insert", content)
        fichero.close()
    elif route == "":
        pass


# Guardar Archivo

def save_file():
    global route
    if route != "":
        content = TextoArchivo.get(1.0, "end - 1c")
        fichero = open(route, "w")
        fichero.write(content)
        fichero.close()
    else:
        save_file_as()


# Guardar archivo como

def save_file_as():
    global route
    fichero = filedialog.asksaveasfile(title="Save as...", mode="w", defaultextension=".txt")
    if fichero is not None:
        route = fichero.name
        content = TextoArchivo.get(1.0, "end - 1c")
        fichero = open(route, "w")
        fichero.write(content)
        fichero.close()
    else:
        route = ""


# Funcion Cambio de frame

def show_frame(frame):
    frame.tkraise()


# Función mostrar texto

def show_text():
    SwitchPest = True
    global route
    scrollbar.pack(side="right", fill="both")
    scrollbar.config(orient="vertical")
    scrollbar.config(command=TextoArchivo.yview)
    TextoArchivo.pack(fill="both", expand=1)
    TextoArchivo.config(yscrollcommand=scrollbar.set)
    TextoArchivo.delete(1.0, "end")
    route = ""


def hide_text():
    SwitchPest = False
    TextoArchivo.pack_forget()
    scrollbar.pack_forget()


# Frames
frameone = tkinter.Frame(gui)
frameone.config(bg="black")
frameone.config(width="700", height="500")
frameone.config(bd="3")
frameone.config(relief="groove")
frametwo = tkinter.Frame(gui)
frametwo.config(bg="#04140E")
framethree = tkinter.Frame(gui)
framethree.config(bg="#04140E")

# Ciclo de cambio para frames

for frame in (frameone, frametwo):
    frame.grid(row=0, column=0, sticky="nsew")

show_frame(frametwo)

# Labels & entrys
ent = tkinter.Entry(frameone, bg="black", fg="white", )
ent.place(x=85, y=14)
labeltwo = tkinter.Label(frametwo, text="LOG IN")
labeltwo.pack(fill="x")
labeltwo.config(bg="#000903", fg="white")
usernamelabel = tkinter.Label(frametwo, text="Username", bg="#04140E", fg="white")
usernamelabel.place(x=230, y=120)
username = tkinter.Entry(frametwo)
username.place(x=300, y=121)
passwordlabel = tkinter.Label(frametwo, text="Password", bg="#04140E", fg="white")
password = tkinter.Entry(frametwo, show="*")
passwordlabel.place(x=230, y=160)
password.place(x=300, y=161)

# Menus

barramenu = tkinter.Menu(gui)
gui.config(menu=barramenu)

# File

filemenu = tkinter.Menu(barramenu, tearoff=0)
filemenu.add_command(label="New", activebackground="grey", command=lambda: show_text())
filemenu.add_command(label="Open", activebackground="grey", command=lambda: open_file())
filemenu.add_command(label="Save", activebackground="grey", command=lambda: save_file())
filemenu.add_command(label="Save as...", activebackground="grey", command=lambda: save_file_as())
filemenu.add_separator()
filemenu.add_command(label="Close", activebackground="grey", command=lambda: hide_text())

# Tools

toolsmenu = tkinter.Menu(barramenu, tearoff=0)
toolsmenu.add_command(label="Fabricator", activebackground="grey")

# Console. Here is where I'll start adding stuff from my library, just for the lulz

consolemenu = tkinter.Menu(barramenu, tearoff=0)
consolemenu.add_command(label="Open", activebackground="grey", command=lambda: Functions.MiCMD())

#Functions

functionmenu = tkinter.Menu(barramenu, tearoff=0)
functionmenu.add_command(label="#BruteForceDecoder", activebackground="grey")

# Buttons
buttonone = tkinter.Button(frameone, bg="black", fg="white", text="Enter", height=3, width=10)
buttonone.config(activebackground="green", command=lambda: show_frame(frametwo))
buttonone.place(x=285, y=180)
buttonpass = tkinter.Button(frametwo, bg="grey", text="Log In", font="Helvetica")
buttonpass.place(x=315, y=218)
buttonpass.config(command=lambda: get_usname(username, password))

#Harper

HarperMenu = tkinter.Menu(barramenu, tearoff=0)
HarperMenu.add_radiobutton(label="On", activebackground="grey")
HarperMenu.add_radiobutton(label="Off", activebackground="grey")

# Texts

scrollbar = tkinter.Scrollbar(framethree)
TextoArchivo = tkinter.Text(framethree)
TextoArchivo.config(bg="#04140E", fg="white", font=("Consolas", 12))
TextoArchivo.config()

# Mainloop
gui.mainloop()
