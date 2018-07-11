from distutils.core import setup, sys

from decimal import *
import time
import random


import tkinter, tkinter.constants
from tkinter import *

buttonMaster = Tk()
buttonMaster.title("DnD Combat")
buttonMaster.geometry("712x700")

pCharName = "Human Paladin"
eCharName = "Orc"

turnCounter = 0
turnGlob = StringVar()
turnGlob.set = ('Its ' + pCharName + 's turn!')






pArmorClass = 18
pHealth = 12
pHitDice = random.randint(1,10) 
pHitDiceMod = 5
pHitDiceNumber = 1
# pAttackCheck = random.randint (1,20)
pAttackCheck = 0
pTreasureType = "gold"
pNumberOfAttacks = 1
# pDamagePerAttack = random.randint(1,8)
pDamagePerAttack = 0
pDamageMod = 3
#pUseWeaponYN = true
pWeapon = "Longsword"
pHit = 0
pGlob = StringVar()
pArmorGlob = StringVar()
pHealthGlob = StringVar()
#pHitDiceHeal = random.randint (1,10)
pHitDiceHeal = 0
pHitDiceGlob = StringVar ()
#pImageFile = PhotoImage(file = 'pimage.png') 





eArmorClass = 13 
eHealth = 15
# eAttackCheck = random.randint(1,20)
eAttackCheck = 0
eAttackCheckMod = 5
eTreasureType = "salvage"
eNumberOfAttacks = 1	
# eDamagePerAttack = random.randint (1,12)
eDamagePerAttack = 0
eDamageMod = 3
#eUseWeaponYN = true
eWeapon = "Greataxe"
eHit = 0
eGlob = StringVar()
eArmorGlob = StringVar()
eHealthGlob = StringVar()
#eImageFile = PhotoImage(file = 'pimage.png') 




def pHit():
	global pAttackCheck
	global pDamagePerAttack
	global pDamageMod
	global turnCounter
	global eArmorClass
	
	
	
	pAttackCheck = random.randint (1,20)

	if(turnCounter == 0 and pHit == 0):	
		if (pAttackCheck >= eArmorClass):
		
			pHit = pHit + 1;
			pGlob.set('HIT!: you may now roll for damage')
		
			print(pGlob.get())
			print("Can Damage")
		
		if(pAttackCheck < eArmorClass):
			
			pGlob.set('Miss: its now the orcs turn')
			turnCoutner = turnCounter + 1;
			turnGlob.set = ('Its ' + eCharName + 's turn!')
	if(turnCounter == 1):
		pGlob.set('its not your turn')

def pDamage():
	global pHit
	global pDamagePerAttack
	global eHealth
	global turnCounter
	
	pDamagePerAttack = random.randint(1,8)

	if (pHit == 1 and turnCounter == 0):
		
		eHealth = eHealth - pDamagePerAttack
		pGlob.set ('You did ' + str(pDamagePerAttack + ' to ' + eCharName))
		eHealthGlob.set('Enemy Health is : ' + str(eHealth))
		turnCounter = turnCounter + 1
		turnGlob.set = ('Its ' + eCharName + 's turn!')
		pHit = pHit - 1		

		if (eHealth <= 0):
			turnGlob.set = (eCharName + 'is DEAD you win!')
	
	if (turnCounter == 1):
		turnGlob.set = ('Its not your turn! its ' + eCharName + 's turn!')




				

def eHit():
	global eAttackCheck
	global eDamagePerAttack
	global eDamageMod
	global turnCounter
	global pArmorClass
	
	
	
	eAttackCheck = random.randint (1,20)

	if(turnCounter == 1 and eHit == 0):	
		if (eAttackCheck >= pArmorClass):
		
			eHit = eHit + 1;
			eGlob.set('HIT!: you may now roll for damage')
		
			print(eGlob.get())
			print("Can Damage")
		
		if(pAttackCheck < pArmorClass):
			
			eGlob.set('Miss: its now the orcs turn')
			turnCoutner = turnCounter + 1;
			turnGlob.set = ('Its ' + pCharName + 's turn!')
	if(turnCounter == 0):
		eGlob.set('its not your turn')





	




def eDamage():
	global eHit
	global eDamagePerAttack
	global pHealth
	global turnCounter
	
	eDamagePerAttack = random.randint (1,12)

	if (eHit == 1 and turnCounter == 1):
		
		pHealth = pHealth - pDamagePerAttack
		eGlob.set ('Enemy did ' + str(pDamagePerAttack + ' to ' + pCharName))
		pHealthGlob.set('Your Health is : ' + str(pHealth))
		turnCounter = turnCounter - 1
		turnGlob.set = ('Its ' + pCharName + 's turn!')
		eHit = eHit - 1		

		if (pHealth <= 0):
			turnGlob.set = (pCharName + 'You Have Died, You Lose')
	
	if (turnCounter == 0):
		turnGlob.set = ('Its not The Enemys turn! its ' + pCharName + 's turn!')



def reset():
	global pHealth
	global pHitDiceNumber
	global eHealth
	global eGlob
	global pGlob
	
	pHealth = 12
	pHitDiceNumber = 1
	eHealth = 15
	eGlob.set ('Not the Enemys Turn!')
	pGlob.set ('Ready to Attack!')
	eHealthGlob.set("Enemy health is " + str(eHealth))
	pHealthGlob.set("Your health is " + str(pHealth))
	turnGlob.set('Its ' + pCharName + 'turn!')

def heal():
	global pHealth
	global pHitDiceNumber
	global pHitDiceHeal

	pHitDiceHeal = random.randint (1,10)
	if (pHitDiceNumber > 0 and pHealth < 12):
		pHealth = pHealth + (pHitDiceHeal)
		pHitDiceNumber = pHitDiceNumber - 1
		pHealthGlob.set ('Your Health is ' + str(pHealth))
		pHitDiceGlob.set ('Heal Dice Remaining: ' + str(pHitDiceNumber))

#player labels
Label(buttonMaster, text = "You are a Human Paladin ", height = 5).grid(row = 0, column = 0, columnspan = 1)
Label(buttonMaster, text = pHealthGlob, height = 5).grid(row = 1, column = 0, columnspan = 1)
Label(buttonMaster, text =( "Your Armor Class is " + str(pArmorClass)), height = 5).grid(row = 2, column = 0, columnspan = 1)

#Enemy Labels
Label(buttonMaster, text = ("He is a " + str(eCharName)) , height = 5).grid(row = 0, column = 2, columnspan = 1)
Label(buttonMaster, text = eHealthGlob, height = 5).grid(row = 1, column = 2, columnspan = 1)
Label(buttonMaster, text =( "His Armor Class is " + str(eArmorClass)), height = 5).grid(row = 2, column = 2, columnspan = 1)


#turnLabel
Label(buttonMaster, text = turnGlob , height = 2, width = 50).grid(row = 3, columnspan = 4)


#buttonText
Label(buttonMaster, text = pGlob, height = 5).grid(row = 4, column = 0, columnspan = 1)
Label(buttonMaster, text = eGlob, height = 5).grid(row = 4, column = 2, columnspan = 1)

#buttons
Button(buttonMaster, text = "Attack!", command = pHit, height = 2, width = 10).grid(row = 5, column = 0)
Button(buttonMaster, text = "Roll For Damage!", command = pDamage, height = 2, width = 20).grid(row = 5, column = 1)
Button(buttonMaster, text = "Attack!", command = eHit, height = 2, width = 10).grid(row = 5, column = 2)
Button(buttonMaster, text = "Roll For Damage!", command = eDamage, height = 2, width = 20).grid(row = 5, column = 3)

#hitDice

Label(buttonMaster, text = pHitDiceGlob, height = 5).grid(row = 6, column = 0)
Button(buttonMaster, text = "Roll for heals", command = heal, height = 10, width = 20).grid(row = 7, column = 0)

#reset and close buttons
Button(buttonMaster, text = "Try Again!", command = reset, height = 5, width = 20).grid(row = 8, column = 0, columnspan = 3)
Button(buttonMaster, text = "End Encounter", command=sys.exit, height = 5, width = 20).grid(row = 9, column = 0, columnspan = 3)

buttonMaster.mainloop()
