
#import the XML parsers
from xml.dom.minidom import parse
import xml.dom.minidom
#import the GUI stuff
from tkinter import *
from tkinter.ttk import *
#import the thread classes
import threading

#UNIMPLEMENTED
def runScript(s):
	

#get the tree and get the document root
Tree = xml.dom.minidom.parse(input("Enter the file path: "))
doc = Tree.documentElement

#Get all the elements inside the root element
elements = doc.childNodes

#set up the frame
root = Tk()
if doc.hasAttribute("title"):
	root.title(doc.getAttribute("title"))
else:
	root.title("Carrot Interpreter")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

controls = {}
scripts = []

for element in elements:
	#label element parser
	if element.prefix == None and element.localName == "label":
		lbl = Label(root, text=element.childNodes[0].data)
		lbl.grid(column=int(element.getAttribute("x")), row=int(element.getAttribute("y")))
		if element.hasAttribute("id"):
			controls[element.getAttribute("id")] = [element, lbl]

	#input element
	if element.prefix == None and element.localName == "input":
		if element.hasAttribute("width"):
			w = int(element.getAttribute("width"))
			input = Entry(root, width=w)
		else:
			input = Entry(root)
		input.grid(column=int(element.getAttribute("x")), row=int(element.getAttribute("y")))
		if element.hasAttribute("id"):
			controls[element.getAttribute("id")] = [element, input]

    #script element
	if element.prefix == None and element.localName == "script":
		s = str(element.childNodes[0].data)
		script = threading.Thread(target=runScript, args=(s,))
		scripts.append(script)

for script in scripts:
    script.start()

root.mainloop()
