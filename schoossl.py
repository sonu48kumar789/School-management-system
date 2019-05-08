import  wx
from wx import *
import os
cws = "d:/school"

app = App()
root = Frame(None,title="school",size=(800,700))
panel = Panel(root)

panel.SetBackgroundColour("#8FBC8F")
maimbox = BoxSizer(VERTICAL)

brand = StaticBitmap(panel,1,Bitmap("F:/skkk.jpg"))
maimbox.Add(brand,0,ALL|EXPAND)

display = StaticText(panel,1,label="Management",style=ALIGN_CENTER)
font = Font(25,FONTFAMILY_DECORATIVE,FONTSTYLE_NORMAL,FONTWEIGHT_BOLD)
display.SetFont(font)
maimbox.Add(display,0,ALL|EXPAND)
boxsizer = BoxSizer(HORIZONTAL)


rightgrid = GridSizer(7, 2, 10, 10)

name = wx.StaticText(panel, label="Name")
email = wx.StaticText(panel, label="Email")
clas = wx.StaticText(panel, label="Class")
genter = wx.StaticText(panel, label="Genter")
contact = wx.StaticText(panel, label="Contact")
address = wx.StaticText(panel, label="Address")
tc1 = wx.TextCtrl(panel)
tc2 = wx.TextCtrl(panel)
tc3 = wx.TextCtrl(panel)
tc4 = wx.TextCtrl(panel)
tc5 = wx.TextCtrl(panel)
tc6 = wx.TextCtrl(panel)


rightgrid.AddMany([
    (name), (tc1, 0, wx.EXPAND),
    (email), (tc2, 0, wx.EXPAND),
    (clas), (tc3, 0, wx.EXPAND),
    (genter), (tc4, 0, wx.EXPAND),
    (contact), (tc5, 0, wx.EXPAND),
    (address), (tc6, 0, wx.EXPAND),

    ])
btn1 = Button(panel, 0,label="Clear")
btn1.SetForegroundColour("black")
btn1.SetBackgroundColour("red")


def clear(e):
    tc1.SetValue("")
    tc2.SetValue("")
    tc3.SetValue("")
    tc4.SetValue("")
    tc5.SetValue("")
    tc6.SetValue("")

btn1.Bind(EVT_BUTTON,clear,btn1)

rightgrid.Add(btn1, 0, EXPAND | ALL)
btn2 = Button(panel, -1,label="Send")
btn2.SetForegroundColour("black")
btn2.SetBackgroundColour("pink")


def send(event):
    file = open(cws+tc1.GetValue()+".text",'w')
    file.write("Name:\t"+tc1.GetValue()+"\nEmail: \t"+tc2.GetValue()+"\nClass: \t"+tc3.GetValue()+"\nGenter: \t"+tc4.GetValue()+"\nContact: \t"+tc5.GetValue()+"\nAddress: \t"+tc6.GetValue())
    file.close()


btn2.Bind(EVT_BUTTON,send,btn2)


rightgrid.Add(btn2, -1, EXPAND | ALL)
boxsizer.Add(rightgrid,1,ALL|EXPAND)

bos = BoxSizer(VERTICAL)
gridsizer = GridSizer(1,4,10,10)

btn3 = Button(panel, 1,label="Open")

gridsizer.Add(btn3,1,ALL|EXPAND)

def open_file(event):
    file = FileDialog(panel,"Open","d:/",wildcard="txt file|*.txt")
    if file.ShowModal() == ID_OK:
        data = open(file.GetPath(),'r')
        cws.SetValue(data.read())
        root.SetLabel(file.GetFilename() + "- school")
        data.close()
btn3.Bind(EVT_BUTTON,open_file,id=ID_OPEN)


btn4 = Button(panel, 1,label="Save")
gridsizer.Add(btn4,1,ALL|EXPAND)


def save_file(e):
    save = FileDialog(panel,"SAVE","d:/",wildcard="text file(*.txt)|*.txt",style=FD_SAVE)
    save.ShowModal()
    path = save.GetPath()
    file = open(path,'w')
    file.write(cws.GetValue())
    file.close()
btn4.Bind(EVT_BUTTON,save_file,btn4)




btn5 = Button(panel, 1,label="Clear")
gridsizer.Add(btn5,1,ALL|EXPAND)


btn6 = Button(panel, 1,label="Exit")
gridsizer.Add(btn6,1,ALL|EXPAND)


def close(event):
    data = MessageDialog(panel,"are you really want to exit?","Confirm",CANCEL|ICON_WARNING)
    if data.ShowModal() == ID_OK:
        root.Close()

btn6.Bind(EVT_BUTTON,close,btn6)

bos.Add(gridsizer,1,ALL|EXPAND)

a = TextCtrl(panel,1,style=TE_MULTILINE)
bos.Add(a,7,ALL|EXPAND)
boxsizer.Add(bos,1,ALL|EXPAND)


maimbox.Add(boxsizer,1,ALL|EXPAND)





panel.SetSizer(maimbox)

status = root.CreateStatusBar(4)

def set_word_count(e):
    word = a.GetValue()
    length = len(word)
    word_length = len(word.split( ))
    root.StatusBar.SetStatusText("Word : " + str(word_length),0)
    root.StatusBar.SetStatusText("Character : " + str(length),1)
    root.StatusBar.SetStatusText("Time : " + str(wxEVT_TIMER),2)

a.Bind(EVT_TEXT,set_word_count)

root.StatusBar.SetStatusText("this is footer 2",3)


root.Show()
app.MainLoop()