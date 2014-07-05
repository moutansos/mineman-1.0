# mineman-1.0
# ===============================================
# This program is released under public domain
# all code within this program may be used
# anywhere, freely.
# ===============================================
#!/usr/bin/python

import os
import sys
from Tkinter import *
from tkFileDialog import *
import tkMessageBox
import shutil
import ConfigParser

osName="Windows"
homedir=os.path.expanduser("~")
datadir=homedir+"\\AppData\\Roaming\\mineman"
mainCfg=ConfigParser.SafeConfigParser()
mainCfg.read(datadir+"\\main.conf")

class M (object):
	def __init__(self):
		pass

	def empty(self):
		print "Unimplimented option."
		pass

	## GUI RELEVANT FUNCTIONS =====================================

	def addLauncher(self):
		## This function is under construction. Not working at the moment.
		launchertoadd=""
		launchertoadd = askopenfilename()
		print launchertoadd
		if launchertoadd=="":
			pass
		else:
			print "Proceeding to ask the user what launcher to use."
			#launcherSlot=self.askLauncherSlot(nameslot=True)

			def exitALW():
				print "Closing window and getting values."
				print "Getting Name from entry."
				nameforslot=GetSlotEntry.get()
				print nameforslot
				if nameforslot=="":
					print "Not a valid slot name."
				else:
					print "Destroying slot selector window."
					askLS.destroy()
					print "Destroyed."
					print "Proceeding to save values."
					print slotNum.get()
					slotNumLong="<empty>"
					#My long round about way to name the slot variables.
					if slotNum.get()==1:
						slotNumLong="slot1"
					elif slotNum.get()==2:
						slotNumLong="slot2"
					elif slotNum.get()==3:
						slotNumLong="slot3"
					elif slotNum.get()==4:
						slotNumLong="slot4"
					elif slotNum.get()==5:
						slotNumLong="slot5"
					else:
						print "ERROR: Slot number not recognized."

					#Error checking. Failsafe.
					if slotNumLong=="<empty>":
						print "ERROR: Somehow the slotNumLong variable was not set correctly."
					else:
						print "Slot name provided: "+nameforslot
						print "Launcher file to add: "+launchertoadd
						print "Copying launcher to directory."
						shutil.copyfile(launchertoadd, datadir+"\\launchers\\launcher-"+slotNumLong+".jar")
						print "Launcher sucessfuly copied.\nSetting config keys."
						mainCfg.set("launchers", slotNumLong, datadir+"\\launchers\\launcher-"+slotNumLong+".jar")
						mainCfg.set("launchers", slotNumLong+"Name", nameforslot)
						print "Keys set.\n Writing keys to file."
						with open(datadir+"\\main.conf", 'wb') as configfile:
							mainCfg.write(datadir+"\\main.conf")
						print "Keys are written."
						print "Launcher in "+slotNumLong+" is named: "+nameforslot

			print "Creating launcher slot selector."
			askLS=Tk()
			askLS.title("Select Slot")
			slotNum=IntVar()
			print "Before defined slotNum: "
			print slotNum
			Radiobutton(askLS, text="Slot1 ", variable=slotNum, value=1).pack()
			Radiobutton(askLS, text="Slot2 ", variable=slotNum, value=2).pack()
			Radiobutton(askLS, text="Slot3 ", variable=slotNum, value=3).pack()
			Radiobutton(askLS, text="Slot4 ", variable=slotNum, value=4).pack()
			Radiobutton(askLS, text="Slot5 ", variable=slotNum, value=5).pack()
			Label(askLS, text="Please name the slot below: (All one word)").pack()
			GetSlotEntry=Entry(askLS)
			GetSlotEntry.pack(expand=1, padx=10, pady=10)
			Button(askLS, text="OK", command=exitALW).pack(padx=10, pady=10)
			askLS.mainloop()

	def addData(self):
		## This is the add data function that is not working. Under construction.
		print "Adding a new data slot."
		def exitADF():
			pass

		addDataWin=Tk()
		addDataWin.title("Add a data slot.")


	## BACKEND FUNCTIONS ====================================


	def addLauncherSlotSpec1(self):
		self.addLauncherSlotSpec("1")
	def addLauncherSlotSpec2(self):
		self.addLauncherSlotSpec("2")
	def addLauncherSlotSpec3(self):
		self.addLauncherSlotSpec("3")
	def addLauncherSlotSpec4(self):
		self.addLauncherSlotSpec("4")
	def addLauncherSlotSpec5(self):
		self.addLauncherSlotSpec("5")

	## ----- SLOT SPECIFIC FUNCITONS.
	def addLauncherSlotSpec(self, launchnum):
		print "Adding launcher to Slot "+launchnum
		launtoadd=askopenfilename()
		if launtoadd=="":
			print "ERROR: No file specified. Aborting launcher add."
		else:
			print "Launcher file specified: "+launtoadd
			LaunName=""
			def getNameFromDiag():
				LaunName=GNDmainEntry.get()
				getNameDiag.destroy()

				print "Launcher Name: "+LaunName
				if LaunName=="":
					print "ERROR: No name was specified"
				else:
					lauchnumLong="slot"+launchnum
					mainCfg.set("launchers", lauchnumLong, launtoadd)
					mainCfg.set("launchers", lauchnumLong+"Name", LaunName)
					print "Saving changes to config file."
					with open(datadir+"\\main.conf", 'wb') as configfile:
						mainCfg.write(configfile)

			getNameDiag=Tk()
			getNameDiag.title("Input Launcher Name")
			GNDmainLabel=Label(getNameDiag, text="Please input a launcher name: ")
			GNDmainEntry=Entry(getNameDiag, text="")
			GNDmainButton=Button(getNameDiag, text="Ok", command=getNameFromDiag)
			GNDmainLabel.pack()
			GNDmainEntry.pack()
			GNDmainButton.pack()
			getNameDiag.mainloop()

			





	## END SLOT SPECIFIC FUNCTIONS.

	def backupSingleSlot(self):
		print "Backup single slot started."


	def exitProg(self):
		print "Exiting program...."
		mainwin.destroy()

	def rmDataDir(self):
		print "Removing data directory..."
		#os.remove(datadir)
		shutil.rmtree(datadir)
		print "Directory removed."

	def makeDataDir(self):
		print "Creating a new data directory..."
		os.makedirs(datadir)
		os.makedirs(datadir+"\\launchers")
		os.makedirs(datadir+"\\dataslots")
		os.makedirs(datadir+"\\dataslots\slot1")
		os.makedirs(datadir+"\\dataslots\slot2")
		os.makedirs(datadir+"\\dataslots\slot3")
		os.makedirs(datadir+"\\dataslots\slot4")
		os.makedirs(datadir+"\\dataslots\slot5")
		shutil.copyfile("default.conf", datadir+"\\main.conf")
		print "Created sucessfuly.\n"

	#STARTUP FUNCTIONS ==========================================================

	def startupChecks(self):
		if osName == "Windows":
			if not os.path.exists(datadir):
				print "Data directory not found."
				self.makeDataDir()
			else:
				pass
		else:
			print "Error. No data directory could be found due to unknown OS. Data directory being written in program folder."


		print mainCfg.get("startup", "version")
		if mainCfg.get("startup", "debug")=="yes":
			debug1=1
		else:
			debug1=0

		try:
			print "\n Loading launchers from config..."
			launcher1=mainCfg.get("launchers", "slot1")
			launcher1Name=mainCfg.get("launchers", "slot1Name")
			print "Launcher1 Loaded"
			launcher2=mainCfg.get("launchers", "slot2")
			launcher2Name=mainCfg.get("launchers", "slot2Name")
			print "Launcher2 Loaded"
			launcher3=mainCfg.get("launchers", "slot3")
			launcher3Name=mainCfg.get("launchers", "slot3Name")
			print "Launcher3 Loaded"
			launcher4=mainCfg.get("launchers", "slot4")
			launcher4Name=mainCfg.get("launchers", "slot4Name")
			print "Launcher4 Loaded"
			launcher5=mainCfg.get("launchers", "slot5")
			launcer5Name=mainCfg.get("launchers", "slot5Name")
			print "Launcher5 Loaded"
			print " All launchers loaded sucessfuly.\n\n Proceeding to load data slots."

			data1=mainCfg.get("data", "slot1Name")
			print "Dataslot1 Loaded."
			data2=mainCfg.get("data", "slot2Name")
			print "Dataslot2 Loaded."
			data3=mainCfg.get("data", "slot3Name")
			print "Dataslot3 Loaded."
			data4=mainCfg.get("data", "slot4Name")
			print "DataSlot4 Loaded."
			data5=mainCfg.get("data", "slot5Name")
			print "Dataslot5 Loaded.\n All dataslots sucessfuly loaded.\n\n"
		except:
			print "One or more config values was not found. Program will probably crash. Delete datafolder and start over."



m=M()

def exit2():
	sys.exit()

def mainprog():
	print "Starting MineMan 1.0....."
	print ""
	m.startupChecks()
	print ""
	print "Currently this program is a work in progress. \nSome features may not be implimented yet.\n\n"
	mainwin=Tk()
	mainwin.title("MineMan 1.0")
	mainwin.geometry("500x300")


# Menu Funcitons ======================================
	menubar=Menu(mainwin)

	filemenu=Menu(menubar, tearoff=0)
	filemenu.add_command(label="Add a Launcher", command=m.empty)
	filemenu.add_command(label="Save Config", command=m.empty)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=mainwin.destroy)
	menubar.add_cascade(label="File", menu=filemenu)

	# Launcher menu++++++++++++
	launchermenu=Menu(menubar, tearoff=0)

	launcherslot1cascade=Menu(launchermenu, tearoff=0)
	launcherslot1cascade.add_command(label="Add Launcher", command=m.addLauncherSlotSpec1)
	launchermenu.add_cascade(label="Slot 1", menu=launcherslot1cascade)

	launcherslot2cascade=Menu(launchermenu, tearoff=0)
	launcherslot2cascade.add_command(label="Add Launcher", command=m.addLauncherSlotSpec2)
	launchermenu.add_cascade(label="Slot 2", menu=launcherslot2cascade)

	launcherslot3cascade=Menu(launchermenu, tearoff=0)
	launcherslot3cascade.add_command(label="Add Launcher", command=m.addLauncherSlotSpec3)
	launchermenu.add_cascade(label="Slot 3", menu=launcherslot3cascade)

	launcherslot4cascade=Menu(launchermenu, tearoff=0)
	launcherslot4cascade.add_command(label="Add Launcher", command=m.addLauncherSlotSpec4)
	launchermenu.add_cascade(label="Slot 4", menu=launcherslot4cascade)

	launcherslot5cascade=Menu(launchermenu, tearoff=0)
	launcherslot5cascade.add_command(label="Add Launcher", command=m.addLauncherSlotSpec5)
	launchermenu.add_cascade(label="Slot 5", menu=launcherslot5cascade)

	menubar.add_cascade(label="Launchers", menu=launchermenu)

	# Data menu+++++++++++++++
	datamenu=Menu(menubar, tearoff=0)

	dataslot1cascade=Menu(datamenu, tearoff=0)
	dataslot1cascade.add_command(label="Add Data Slot", command=m.empty)
	datamenu.add_cascade(label="Slot 1", menu=dataslot1cascade)

	dataslot2cascade=Menu(datamenu, tearoff=0)
	dataslot2cascade.add_command(label="Add Data Slot", command=m.empty)
	datamenu.add_cascade(label="Slot 2", menu=dataslot2cascade)

	dataslot3cascade=Menu(datamenu, tearoff=0)
	dataslot3cascade.add_command(label="Add Data Slot", command=m.empty)
	datamenu.add_cascade(label="Slot 3", menu=dataslot3cascade)

	dataslot4cascade=Menu(datamenu, tearoff=0)
	dataslot4cascade.add_command(label="Add Data Slot", command=m.empty)
	datamenu.add_cascade(label="Slot 4", menu=dataslot4cascade)

	dataslot5cascade=Menu(datamenu, tearoff=0)
	dataslot5cascade.add_command(label="Add Data Slot", command=m.empty)
	datamenu.add_cascade(label="Slot 5", menu=dataslot5cascade)

	menubar.add_cascade(label="Data Slots", menu=datamenu)

	#Backup menu++++++++++++++++(Some menu options are being replaced.)
	backupmenu=Menu(menubar, tearoff=0)
	#backupmenu.add_command(label="Backup one slot to file", command=m.empty)
	backupmenu.add_command(label="Backup all slots to file", command=m.empty)
	#backupmenu.add_command(label="Save launcher From list", command=m.empty)
	backupmenu.add_separator()
	#backupmenu.add_command(label="Import one slot", command=m.empty)
	backupmenu.add_command(label="Import all slots", command=m.empty)
	menubar.add_cascade(label="Backup", menu=backupmenu)

	optionsmenu=Menu(menubar, tearoff=0)
	optionsmenu.add_command(label="Edit Launchers", command=m.empty)
	#optionsmenu.add_command(label="Edit Data Slots", command=m.empty)
	optionsmenu.add_command(label="Delete Data", command=m.rmDataDir)
	menubar.add_cascade(label="Options", menu=optionsmenu)

	helpmenu=Menu(menubar, tearoff=0)
	helpmenu.add_command(label="About", command=m.empty)
	menubar.add_cascade(label="Help", menu=helpmenu)

# =====================================================

	controlFrame = Frame(mainwin)
	startLauncherBtn1 = Button(controlFrame, text="Start the Launcher")
	exitMineManBtn1 = Button(controlFrame, text="Exit", command = mainwin.destroy)

	launcherFrame= Frame(mainwin)
	launcherLabel = Label(launcherFrame, text="Launchers available:")

	dataFrame = Frame(mainwin)
	dataLabel= Label(dataFrame, text="Data folders available: ")

	controlFrame.pack(side=BOTTOM, fill=X, padx=5, pady=5)
	startLauncherBtn1.pack(side=RIGHT, padx=5)
	exitMineManBtn1.pack(side =RIGHT, padx=5)

	launcherFrame.pack(side=TOP, fill=BOTH, padx=5, pady=5)
	launcherLabel.pack(side=LEFT, pady=5)

	dataFrame.pack(side=TOP, fill=BOTH, padx=5, pady=5)
	dataLabel.pack(side=LEFT, pady=5)

	mainwin.config(menu=menubar)
	mainwin.mainloop()

mainprog()
print "MineMan has exited."
# Autosaving seems to make the config file 
#with open(datadir+"\\main.conf", 'w') as configfile:
#	mainCfg.write(datadir+"\\main.conf")