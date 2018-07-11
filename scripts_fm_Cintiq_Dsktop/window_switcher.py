from distutils.core import setup, sys
import tkinter, tkinter.constants
from tkinter import *
import win32gui, win32con

# i think it takes the enum array functions returns and puts them into the windows open array
def windowEnumArrayHandler(hwnd, windowsOpen):
	windowsOpen.append((hwnd, win32gui.GetWindowText(hwnd)))

	
#populates the open window array with enum window function and the array handler
def findWindow():
	windowsOpen = []
	results = []
	win32gui.EnumWindows(windowEnumArrayHandler, windowsOpen)
	# looks through the windows open array
	for x in windowsOpen:
		#looks for notepad in the araay
		if "unreal editor" in x[1].lower():
			# sets the windows  to the globally active window and shows it
			win32gui.ShowWindow(x[0],win32con.SW_MAXIMIZE)
			win32gui.SetForegroundWindow(x[0])
			break
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	


window = Tk()
window.title("new app")
window.geometry("500x500")

labelText = "go to unreal engine window"

Button(window, text=labelText, height = 3, command = findWindow).grid(row=1,column =1, columnspan=1)
Button(window, text = 'import file in unreal', height = 3).grid(row=2,column=1, columnspan = 1)
Button(window, text = 'close window', command = 'sys.exit')

window.mainloop()