from numpy import *
from turtle import *
from tkinter import *
from math import *
from random import randint

bgcolor("white")
color("black")
ht()
colormode(255)
title("Python Turtle Rubik's Cube Simulator")

OF = [matrix([[150],[150],[150]]), matrix([[50],[150],[150]]), matrix([[50],[50],[150]]), matrix([[150],[50],[150]]),
	  matrix([[50],[150],[150]]), matrix([[-50],[150],[150]]), matrix([[-50],[50],[150]]), matrix([[50],[50],[150]]),
	  matrix([[-50],[150],[150]]), matrix([[-150],[150],[150]]), matrix([[-150],[50],[150]]), matrix([[-50],[50],[150]]),
	  matrix([[150],[50],[150]]), matrix([[50],[50],[150]]), matrix([[50],[-50],[150]]), matrix([[150],[-50],[150]]),
	  matrix([[50],[50],[150]]), matrix([[-50],[50],[150]]), matrix([[-50],[-50],[150]]), matrix([[50],[-50],[150]]),
	  matrix([[-50],[50],[150]]), matrix([[-150],[50],[150]]), matrix([[-150],[-50],[150]]), matrix([[-50],[-50],[150]]),
	  matrix([[150],[-50],[150]]), matrix([[50],[-50],[150]]), matrix([[50],[-150],[150]]), matrix([[150],[-150],[150]]),
	  matrix([[50],[-50],[150]]), matrix([[-50],[-50],[150]]), matrix([[-50],[-150],[150]]), matrix([[50],[-150],[150]]),
	  matrix([[-50],[-50],[150]]), matrix([[-150],[-50],[150]]), matrix([[-150],[-150],[150]]), matrix([[-50],[-150],[150]])]
RF = [matrix([[150],[150],[-150]]), matrix([[50],[150],[-150]]), matrix([[50],[50],[-150]]), matrix([[150],[50],[-150]]),
	  matrix([[50],[150],[-150]]), matrix([[-50],[150],[-150]]), matrix([[-50],[50],[-150]]), matrix([[50],[50],[-150]]),
	  matrix([[-50],[150],[-150]]), matrix([[-150],[150],[-150]]), matrix([[-150],[50],[-150]]), matrix([[-50],[50],[-150]]),
	  matrix([[150],[50],[-150]]), matrix([[50],[50],[-150]]), matrix([[50],[-50],[-150]]), matrix([[150],[-50],[-150]]),
	  matrix([[50],[50],[-150]]), matrix([[-50],[50],[-150]]), matrix([[-50],[-50],[-150]]), matrix([[50],[-50],[-150]]),
	  matrix([[-50],[50],[-150]]), matrix([[-150],[50],[-150]]), matrix([[-150],[-50],[-150]]), matrix([[-50],[-50],[-150]]),
	  matrix([[150],[-50],[-150]]), matrix([[50],[-50],[-150]]), matrix([[50],[-150],[-150]]), matrix([[150],[-150],[-150]]),
	  matrix([[50],[-50],[-150]]), matrix([[-50],[-50],[-150]]), matrix([[-50],[-150],[-150]]), matrix([[50],[-150],[-150]]),
	  matrix([[-50],[-50],[-150]]), matrix([[-150],[-50],[-150]]), matrix([[-150],[-150],[-150]]), matrix([[-50],[-150],[-150]])]
WF = [matrix([[150],[150],[150]]), matrix([[50],[150],[150]]), matrix([[50],[150],[50]]), matrix([[150],[150],[50]]),
	  matrix([[50],[150],[150]]), matrix([[-50],[150],[150]]), matrix([[-50],[150],[50]]), matrix([[50],[150],[50]]),
	  matrix([[-50],[150],[150]]), matrix([[-150],[150],[150]]), matrix([[-150],[150],[50]]), matrix([[-50],[150],[50]]),
	  matrix([[150],[150],[50]]), matrix([[50],[150],[50]]), matrix([[50],[150],[-50]]), matrix([[150],[150],[-50]]),
	  matrix([[50],[150],[50]]), matrix([[-50],[150],[50]]), matrix([[-50],[150],[-50]]), matrix([[50],[150],[-50]]),
	  matrix([[-50],[150],[50]]), matrix([[-150],[150],[50]]), matrix([[-150],[150],[-50]]), matrix([[-50],[150],[-50]]),
	  matrix([[150],[150],[-50]]), matrix([[50],[150],[-50]]), matrix([[50],[150],[-150]]), matrix([[150],[150],[-150]]),
	  matrix([[50],[150],[-50]]), matrix([[-50],[150],[-50]]), matrix([[-50],[150],[-150]]), matrix([[50],[150],[-150]]),
	  matrix([[-50],[150],[-50]]), matrix([[-150],[150],[-50]]), matrix([[-150],[150],[-150]]), matrix([[-50],[150],[-150]])]
YF = [matrix([[150],[-150],[150]]), matrix([[50],[-150],[150]]), matrix([[50],[-150],[50]]), matrix([[150],[-150],[50]]),
	  matrix([[50],[-150],[150]]), matrix([[-50],[-150],[150]]), matrix([[-50],[-150],[50]]), matrix([[50],[-150],[50]]),
	  matrix([[-50],[-150],[150]]), matrix([[-150],[-150],[150]]), matrix([[-150],[-150],[50]]), matrix([[-50],[-150],[50]]),
	  matrix([[150],[-150],[50]]), matrix([[50],[-150],[50]]), matrix([[50],[-150],[-50]]), matrix([[150],[-150],[-50]]),
	  matrix([[50],[-150],[50]]), matrix([[-50],[-150],[50]]), matrix([[-50],[-150],[-50]]), matrix([[50],[-150],[-50]]),
	  matrix([[-50],[-150],[50]]), matrix([[-150],[-150],[50]]), matrix([[-150],[-150],[-50]]), matrix([[-50],[-150],[-50]]),
	  matrix([[150],[-150],[-50]]), matrix([[50],[-150],[-50]]), matrix([[50],[-150],[-150]]), matrix([[150],[-150],[-150]]),
	  matrix([[50],[-150],[-50]]), matrix([[-50],[-150],[-50]]), matrix([[-50],[-150],[-150]]), matrix([[50],[-150],[-150]]),
	  matrix([[-50],[-150],[-50]]), matrix([[-150],[-150],[-50]]), matrix([[-150],[-150],[-150]]), matrix([[-50],[-150],[-150]])]
BF = [matrix([[-150],[150],[150]]), matrix([[-150],[50],[150]]), matrix([[-150],[50],[50]]), matrix([[-150],[150],[50]]),
	  matrix([[-150],[50],[150]]), matrix([[-150],[-50],[150]]), matrix([[-150],[-50],[50]]), matrix([[-150],[50],[50]]),
	  matrix([[-150],[-50],[150]]), matrix([[-150],[-150],[150]]), matrix([[-150],[-150],[50]]), matrix([[-150],[-50],[50]]),
	  matrix([[-150],[150],[50]]), matrix([[-150],[50],[50]]), matrix([[-150],[50],[-50]]), matrix([[-150],[150],[-50]]),
	  matrix([[-150],[50],[50]]), matrix([[-150],[-50],[50]]), matrix([[-150],[-50],[-50]]), matrix([[-150],[50],[-50]]),
	  matrix([[-150],[-50],[50]]), matrix([[-150],[-150],[50]]), matrix([[-150],[-150],[-50]]), matrix([[-150],[-50],[-50]]),
	  matrix([[-150],[150],[-50]]), matrix([[-150],[50],[-50]]), matrix([[-150],[50],[-150]]), matrix([[-150],[150],[-150]]),
	  matrix([[-150],[50],[-50]]), matrix([[-150],[-50],[-50]]), matrix([[-150],[-50],[-150]]), matrix([[-150],[50],[-150]]),
	  matrix([[-150],[-50],[-50]]), matrix([[-150],[-150],[-50]]), matrix([[-150],[-150],[-150]]), matrix([[-150],[-50],[-150]])]
GF = [matrix([[150],[150],[150]]), matrix([[150],[50],[150]]), matrix([[150],[50],[50]]), matrix([[150],[150],[50]]),
	  matrix([[150],[50],[150]]), matrix([[150],[-50],[150]]), matrix([[150],[-50],[50]]), matrix([[150],[50],[50]]),
	  matrix([[150],[-50],[150]]), matrix([[150],[-150],[150]]), matrix([[150],[-150],[50]]), matrix([[150],[-50],[50]]),
	  matrix([[150],[150],[50]]), matrix([[150],[50],[50]]), matrix([[150],[50],[-50]]), matrix([[150],[150],[-50]]),
	  matrix([[150],[50],[50]]), matrix([[150],[-50],[50]]), matrix([[150],[-50],[-50]]), matrix([[150],[50],[-50]]),
	  matrix([[150],[-50],[50]]), matrix([[150],[-150],[50]]), matrix([[150],[-150],[-50]]), matrix([[150],[-50],[-50]]),
	  matrix([[150],[150],[-50]]), matrix([[150],[50],[-50]]), matrix([[150],[50],[-150]]), matrix([[150],[150],[-150]]),
	  matrix([[150],[50],[-50]]), matrix([[150],[-50],[-50]]), matrix([[150],[-50],[-150]]), matrix([[150],[50],[-150]]),
	  matrix([[150],[-50],[-50]]), matrix([[150],[-150],[-50]]), matrix([[150],[-150],[-150]]), matrix([[150],[-50],[-150]])]
couples = [[(0, 1), (1, 2), (2, 3), (3, 0)],
		   [(4, 5), (5, 6), (6, 7), (7, 4)],
		   [(8, 9), (9, 10), (10, 11), (11, 8)],
		   [(12, 13), (13, 14), (14, 15), (15, 12)],
		   [(16, 17), (17, 18), (18, 19), (19, 16)],
		   [(20, 21), (21, 22), (22, 23), (23, 20)],
		   [(24, 25), (25, 26), (26, 27), (27, 24)],
		   [(28, 29), (29, 30), (30, 31), (31, 28)],
		   [(32, 33), (33, 34), (34, 35), (35, 32)]]

MainLoop = True
LEFT = False
RIGHT = False
UP = False
DOWN = False
SHIFT = False
PosX = 225.0
PosY = 45.0
WriteLetter = False

CubesW = {'1':'white','2':'white','3':'white','4':'white','5':'white','6':'white','7':'white','8':'white','9':'white'}
CubesY = {'1':'yellow','2':'yellow','3':'yellow','4':'yellow','5':'yellow','6':'yellow','7':'yellow','8':'yellow','9':'yellow'}
CubesR = {'1':'red','2':'red','3':'red','4':'red','5':'red','6':'red','7':'red','8':'red','9':'red'}
CubesO = {'1':'orange','2':'orange','3':'orange','4':'orange','5':'orange','6':'orange','7':'orange','8':'orange','9':'orange'}
CubesG = {'1':'green','2':'green','3':'green','4':'green','5':'green','6':'green','7':'green','8':'green','9':'green'}
CubesB = {'1':'blue','2':'blue','3':'blue','4':'blue','5':'blue','6':'blue','7':'blue','8':'blue','9':'blue'}

# CubesW = {'1':'white','2':'yellow','3':'orange','4':'red','5':'white','6':'purple','7':'blue','8':'green','9':'black'}
# CubesY = {'1':'white','2':'yellow','3':'orange','4':'red','5':'yellow','6':'purple','7':'blue','8':'green','9':'black'}
# CubesR = {'1':'white','2':'yellow','3':'orange','4':'red','5':'red','6':'purple','7':'blue','8':'green','9':'black'}
# CubesO = {'1':'white','2':'yellow','3':'orange','4':'red','5':'orange','6':'purple','7':'blue','8':'green','9':'black'}
# CubesG = {'1':'white','2':'yellow','3':'orange','4':'red','5':'green','6':'purple','7':'blue','8':'green','9':'black'}
# CubesB = {'1':'white','2':'yellow','3':'orange','4':'red','5':'blue','6':'purple','7':'blue','8':'green','9':'black'}

def mat_rotx(t):
	t = radians(t)
	return matrix([[1, 0, 0], [0, cos(t), -sin(t)], [0, sin(t), cos(t)]])
def mat_roty(t):
	t = radians(t)
	return matrix([[cos(t), 0, sin(t)], [0, 1, 0], [-sin(t), 0, cos(t)]])
def mat_rotz(t):
	t = radians(t)
	return matrix([[cos(t), -sin(t), 0], [sin(t), cos(t), 0], [0, 0, 1]])
def mat_hom(k):
	return matrix([[k, 0, 0], [0, k, 0], [0, 0, k]])
def transforme3D(mat, cube):
	return [mat*m for m in cube]

def dessine_proj(LP, LC, color):
	pen(fillcolor=color, pencolor="black")
	begin_fill()
	for (i, j) in LC:
		pu()
		goto(LP[i][0, 0], LP[i][1, 0])
		pd()
		goto(LP[j][0, 0], LP[j][1, 0])
	end_fill()

def write_proj(coord, l, col):
	pu()
	goto(coord[0][0, 0], coord[0][1, 0])
	color(col)
	begin_fill()
	write(l, font=('Arial', 20, 'normal'))
	end_fill()

def update_cube():
	clear()
	tracer(0)
	if PosY > 270 or PosY < 90:
		if PosX > 270 or PosX < 90: 
			for pos, color in CubesO.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), OF), couples[int(pos)-1], color) # ---- Faces ---- #
		if PosX < 270 and PosX > 90:
			for pos, color in CubesR.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), RF), couples[int(pos)-1], color)
		if PosX > 0 and PosX < 180:
			for pos, color in CubesB.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), BF), couples[int(pos)-1], color)
		if PosX < 0 or PosX > 180:
			for pos, color in CubesG.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), GF), couples[int(pos)-1], color)
	if PosY < 270 and PosY > 90: 
		if PosX < 270 and PosX > 90:
			for pos, color in CubesO.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), OF), couples[int(pos)-1], color)
		if PosX > 270 or PosX < 90: 
			for pos, color in CubesR.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), RF), couples[int(pos)-1], color)
		if PosX < 0 or PosX > 180:
			for pos, color in CubesB.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), BF), couples[int(pos)-1], color)
		if PosX > 0 and PosX < 180:
			for pos, color in CubesG.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), GF), couples[int(pos)-1], color)
	if PosY > 0 and PosY < 180: 
		for pos, color in CubesW.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), WF), couples[int(pos)-1], color) 
	if PosY < 0 or PosY > 180: 
		for pos, color in CubesY.items(): dessine_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), YF), couples[int(pos)-1], color)

	if WriteLetter:
		if PosY > 270 or PosY < 90:
			if PosX > 270 or PosX < 90: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[0], [0], [200]])]), 'O', 'purple')
			if PosX < 270 and PosX > 90: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[0], [0], [-200]])]), 'R', 'purple')
			if PosX > 0 and PosX < 180: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[-200], [0], [0]])]), 'B', 'purple')
			if PosX < 0 or PosX > 180: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[200], [0], [0]])]), 'G', 'purple')
		if PosY < 270 and PosY > 90:
			if PosX < 270 and PosX > 90: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[0], [0], [200]])]), 'O', 'purple')
			if PosX > 270 or PosX < 90: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[0], [0], [-200]])]), 'R', 'purple')
			if PosX < 0 or PosX > 180: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[-200], [0], [0]])]), 'B', 'purple')
			if PosX > 0 and PosX < 180:write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[200], [0], [0]])]), 'G', 'purple')
		if PosY > 0 and PosY < 180: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[0], [200], [0]])]), 'W', 'purple')
		if PosY < 0 or PosY > 180: write_proj(transforme3D(mat_rotx(PosY)*mat_roty(PosX), [matrix([[0], [-200], [0]])]), 'Y', 'purple')
	
	update()

def LeftPressed(): # ---- Tourner le cube quand appuie de touche ---- #
	global LEFT
	LEFT = True
def RightPressed():
	global RIGHT
	RIGHT = True
def UpPressed():
	global UP
	UP = True
def DownPressed():
	global DOWN
	DOWN = True
def LeftRelease(): # ---- Arreter de faire tourner quand touche relachée ---- #
	global LEFT
	LEFT = False
def RightRelease():
	global RIGHT
	RIGHT = False
def UpRelease():
	global UP
	UP = False
def DownRelease():
	global DOWN
	DOWN = False

def MoveLeftW(): # ---- Faire tourner les faces dans un sens ---- #
	global CubesW, CubesR, CubesG, CubesO, CubesB
	todel = dict(CubesR)
	CubesR['1'] = CubesB['7']
	CubesR['2'] = CubesB['4']
	CubesR['3'] = CubesB['1']
	CubesB['7'] = CubesO['2']
	CubesB['4'] = CubesO['2']
	CubesB['1'] = CubesO['1']
	CubesO['3'] = CubesG['1']
	CubesO['2'] = CubesG['4']
	CubesO['1'] = CubesG['7']
	CubesG['1'] = todel['1']
	CubesG['4'] = todel['2']
	CubesG['7'] = todel['3']

	todel = dict(CubesW)
	CubesW['1'] = todel['7']
	CubesW['2'] = todel['4']
	CubesW['3'] = todel['1']
	CubesW['4'] = todel['8']
	CubesW['6'] = todel['2']
	CubesW['7'] = todel['9']
	CubesW['8'] = todel['6']
	CubesW['9'] = todel['3']
	del todel

def MoveLeftY():
	global CubesY, CubesR, CubesG, CubesO, CubesB
	todel = dict(CubesR)
	CubesR['7'] = CubesB['9']
	CubesR['8'] = CubesB['6']
	CubesR['9'] = CubesB['3']
	CubesB['9'] = CubesO['9']
	CubesB['6'] = CubesO['8']
	CubesB['3'] = CubesO['7']
	CubesO['9'] = CubesG['3']
	CubesO['8'] = CubesG['6']
	CubesO['7'] = CubesG['9']
	CubesG['3'] = todel['7']
	CubesG['6'] = todel['8']
	CubesG['9'] = todel['9']

	todel = dict(CubesY)
	CubesY['1'] = todel['7']
	CubesY['2'] = todel['4']
	CubesY['3'] = todel['1']
	CubesY['4'] = todel['8']
	CubesY['6'] = todel['2']
	CubesY['7'] = todel['9']
	CubesY['8'] = todel['6']
	CubesY['9'] = todel['3']
	del todel

def MoveLeftR():
	global CubesR, CubesW, CubesG, CubesO, CubesB
	todel = dict(CubesY)
	CubesY['9'] = CubesB['7']
	CubesY['8'] = CubesB['8']
	CubesY['7'] = CubesB['9']
	CubesB['7'] = CubesW['7']
	CubesB['8'] = CubesW['8']
	CubesB['9'] = CubesW['9']
	CubesW['7'] = CubesG['9']
	CubesW['8'] = CubesG['8']
	CubesW['9'] = CubesG['7']
	CubesG['9'] = todel['9']
	CubesG['8'] = todel['8']
	CubesG['7'] = todel['7']

	todel = dict(CubesR)
	CubesR['1'] = todel['7']
	CubesR['2'] = todel['4']
	CubesR['3'] = todel['1']
	CubesR['4'] = todel['8']
	CubesR['6'] = todel['2']
	CubesR['7'] = todel['9']
	CubesR['8'] = todel['6']
	CubesR['9'] = todel['3']
	del todel

def MoveLeftO():
	global CubesO, CubesW, CubesG, CubesR, CubesB
	todel = dict(CubesY)
	CubesY['3'] = CubesB['1']
	CubesY['2'] = CubesB['2']
	CubesY['1'] = CubesB['3']
	CubesB['1'] = CubesW['1']
	CubesB['2'] = CubesW['2']
	CubesB['3'] = CubesW['3']
	CubesW['1'] = CubesG['3']
	CubesW['2'] = CubesG['2']
	CubesW['3'] = CubesG['1']
	CubesG['3'] = todel['3']
	CubesG['2'] = todel['2']
	CubesG['1'] = todel['1']

	todel = dict(CubesO)
	CubesO['1'] = todel['7']
	CubesO['2'] = todel['4']
	CubesO['3'] = todel['1']
	CubesO['4'] = todel['8']
	CubesO['6'] = todel['2']
	CubesO['7'] = todel['9']
	CubesO['8'] = todel['6']
	CubesO['9'] = todel['3']
	del todel

def MoveLeftG():
	global CubesG, CubesR, CubesW, CubesO, CubesY
	todel = dict(CubesR)
	CubesR['1'] = CubesY['7']
	CubesR['4'] = CubesY['4']
	CubesR['7'] = CubesY['1']
	CubesY['7'] = CubesO['7']
	CubesY['4'] = CubesO['4']
	CubesY['1'] = CubesO['1']
	CubesO['7'] = CubesW['1']
	CubesO['4'] = CubesW['4']
	CubesO['1'] = CubesW['7']
	CubesW['1'] = todel['1']
	CubesW['4'] = todel['4']
	CubesW['7'] = todel['7']

	todel = dict(CubesG)
	CubesG['1'] = todel['7']
	CubesG['2'] = todel['4']
	CubesG['3'] = todel['1']
	CubesG['4'] = todel['8']
	CubesG['6'] = todel['2']
	CubesG['7'] = todel['9']
	CubesG['8'] = todel['6']
	CubesG['9'] = todel['3']
	del todel

def MoveLeftB():
	global CubesB, CubesR, CubesW, CubesO, CubesY
	todel = dict(CubesR)
	CubesR['3'] = CubesY['9']
	CubesR['6'] = CubesY['6']
	CubesR['9'] = CubesY['3']
	CubesY['9'] = CubesO['9']
	CubesY['6'] = CubesO['6']
	CubesY['3'] = CubesO['3']
	CubesO['9'] = CubesW['3']
	CubesO['6'] = CubesW['6']
	CubesO['3'] = CubesW['9']
	CubesW['3'] = todel['3']
	CubesW['6'] = todel['6']
	CubesW['9'] = todel['9']

	todel = dict(CubesB)
	CubesB['1'] = todel['7']
	CubesB['2'] = todel['4']
	CubesB['3'] = todel['1']
	CubesB['4'] = todel['8']
	CubesB['6'] = todel['2']
	CubesB['7'] = todel['9']
	CubesB['8'] = todel['6']
	CubesB['9'] = todel['3']
	del todel

def MoveRightW(): # ---- Faire tourner les faces dans l'autre sens ---- #
	global CubesW, CubesR, CubesG, CubesO, CubesB
	todel = dict(CubesR)
	CubesR['1'] = CubesG['1']
	CubesR['2'] = CubesG['4']
	CubesR['3'] = CubesG['7']
	CubesG['1'] = CubesO['3']
	CubesG['4'] = CubesO['2']
	CubesG['7'] = CubesO['1']
	CubesO['3'] = CubesB['7']
	CubesO['2'] = CubesB['4']
	CubesO['1'] = CubesB['1']
	CubesB['7'] = todel['1']
	CubesB['4'] = todel['2']
	CubesB['1'] = todel['3']

	todel = dict(CubesW)
	CubesW['1'] = todel['3']
	CubesW['2'] = todel['6']
	CubesW['3'] = todel['9']
	CubesW['4'] = todel['2']
	CubesW['6'] = todel['8']
	CubesW['7'] = todel['1']
	CubesW['8'] = todel['4']
	CubesW['9'] = todel['7']
	del todel

def MoveRightY():
	global CubesY, CubesR, CubesG, CubesO, CubesB
	todel = dict(CubesR)
	CubesR['9'] = CubesG['9']
	CubesR['8'] = CubesG['6']
	CubesR['7'] = CubesG['3']
	CubesG['9'] = CubesO['7']
	CubesG['6'] = CubesO['8']
	CubesG['3'] = CubesO['9']
	CubesO['7'] = CubesB['3']
	CubesO['8'] = CubesB['6']
	CubesO['9'] = CubesB['9']
	CubesB['3'] = todel['9']
	CubesB['6'] = todel['8']
	CubesB['9'] = todel['7']

	todel = dict(CubesY)
	CubesY['1'] = todel['3']
	CubesY['2'] = todel['6']
	CubesY['3'] = todel['9']
	CubesY['4'] = todel['2']
	CubesY['6'] = todel['8']
	CubesY['7'] = todel['1']
	CubesY['8'] = todel['4']
	CubesY['9'] = todel['7']
	del todel

def MoveRightR():
	global CubesR, CubesW, CubesG, CubesO, CubesB
	todel = dict(CubesY)
	CubesY['7'] = CubesG['7']
	CubesY['8'] = CubesG['8']
	CubesY['9'] = CubesG['9']
	CubesG['7'] = CubesW['9']
	CubesG['8'] = CubesW['8']
	CubesG['9'] = CubesW['7']
	CubesW['9'] = CubesB['9']
	CubesW['8'] = CubesB['8']
	CubesW['7'] = CubesB['7']
	CubesB['9'] = todel['7']
	CubesB['8'] = todel['8']
	CubesB['7'] = todel['9']

	todel = dict(CubesR)
	CubesR['1'] = todel['3']
	CubesR['2'] = todel['6']
	CubesR['3'] = todel['9']
	CubesR['4'] = todel['2']
	CubesR['6'] = todel['8']
	CubesR['7'] = todel['1']
	CubesR['8'] = todel['4']
	CubesR['9'] = todel['7']
	del todel

def MoveRightO():
	global CubesO, CubesW, CubesG, CubesR, CubesB
	todel = dict(CubesY)
	CubesY['3'] = CubesG['3']
	CubesY['2'] = CubesG['2']
	CubesY['1'] = CubesG['1']
	CubesG['3'] = CubesW['1']
	CubesG['2'] = CubesW['2']
	CubesG['1'] = CubesW['3']
	CubesW['1'] = CubesB['1']
	CubesW['2'] = CubesB['2']
	CubesW['3'] = CubesB['3']
	CubesB['1'] = todel['3']
	CubesB['2'] = todel['2']
	CubesB['3'] = todel['1']

	todel = dict(CubesO)
	CubesO['1'] = todel['3']
	CubesO['2'] = todel['6']
	CubesO['3'] = todel['9']
	CubesO['4'] = todel['2']
	CubesO['6'] = todel['8']
	CubesO['7'] = todel['1']
	CubesO['8'] = todel['4']
	CubesO['9'] = todel['7']
	del todel

def MoveRightG():
	global CubesG, CubesR, CubesW, CubesO, CubesY
	todel = dict(CubesR)
	CubesR['7'] = CubesW['7']
	CubesR['4'] = CubesW['4']
	CubesR['1'] = CubesW['1']
	CubesW['7'] = CubesO['1']
	CubesW['4'] = CubesO['4']
	CubesW['1'] = CubesO['7']
	CubesO['1'] = CubesY['1']
	CubesO['4'] = CubesY['4']
	CubesO['7'] = CubesY['7']
	CubesY['1'] = todel['7']
	CubesY['4'] = todel['4']
	CubesY['7'] = todel['1']

	todel = dict(CubesG)
	CubesG['1'] = todel['3']
	CubesG['2'] = todel['6']
	CubesG['3'] = todel['9']
	CubesG['4'] = todel['2']
	CubesG['6'] = todel['8']
	CubesG['7'] = todel['1']
	CubesG['8'] = todel['4']
	CubesG['9'] = todel['7']
	del todel

def MoveRightB():
	global CubesB, CubesR, CubesW, CubesO, CubesY
	todel = dict(CubesR)
	CubesR['9'] = CubesW['9']
	CubesR['6'] = CubesW['6']
	CubesR['3'] = CubesW['3']
	CubesW['9'] = CubesO['3']
	CubesW['6'] = CubesO['6']
	CubesW['3'] = CubesO['9']
	CubesO['3'] = CubesY['3']
	CubesO['6'] = CubesY['6']
	CubesO['9'] = CubesY['9']
	CubesY['3'] = todel['9']
	CubesY['6'] = todel['6']
	CubesY['9'] = todel['3']

	todel = dict(CubesB)
	CubesB['1'] = todel['3']
	CubesB['2'] = todel['6']
	CubesB['3'] = todel['9']
	CubesB['4'] = todel['2']
	CubesB['6'] = todel['8']
	CubesB['7'] = todel['1']
	CubesB['8'] = todel['4']
	CubesB['9'] = todel['7']

def showLetters():
	global WriteLetter
	WriteLetter = False if WriteLetter else True

rot_list = [MoveLeftW, MoveLeftY, MoveLeftR, MoveLeftO, MoveLeftG, MoveLeftB, MoveRightW, MoveRightY, MoveRightR, MoveRightO, MoveRightG, MoveRightB]
def shuffle():
	L = []
	for i in range(20): L.append(rot_list[randint(0, len(rot_list)-1)])
	for fonc in L: fonc()

def solve():
	global CubesW, CubesY, CubesR, CubesO, CubesG, CubesB
	CubesW = {'1':'white','2':'white','3':'white','4':'white','5':'white','6':'white','7':'white','8':'white','9':'white'}
	CubesY = {'1':'yellow','2':'yellow','3':'yellow','4':'yellow','5':'yellow','6':'yellow','7':'yellow','8':'yellow','9':'yellow'}
	CubesR = {'1':'red','2':'red','3':'red','4':'red','5':'red','6':'red','7':'red','8':'red','9':'red'}
	CubesO = {'1':'orange','2':'orange','3':'orange','4':'orange','5':'orange','6':'orange','7':'orange','8':'orange','9':'orange'}
	CubesG = {'1':'green','2':'green','3':'green','4':'green','5':'green','6':'green','7':'green','8':'green','9':'green'}
	CubesB = {'1':'blue','2':'blue','3':'blue','4':'blue','5':'blue','6':'blue','7':'blue','8':'blue','9':'blue'}

def quit(): # ---- Quitter ---- #
	global MainLoop
	MainLoop = False

class Interface(Frame):    
	def __init__(self, fenetre, **kwargs):
		Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
		self.pack(fill=BOTH)

		self.button_shuffle = Button(self, text="Mélanger", command=shuffle)
		self.button_shuffle.grid(row=1, column=1)

		self.button_resolve = Button(self, text="Résoudre", command=solve)
		self.button_resolve.grid(row=7, column=1)

		self.button_quit = Button(self, text="Quitter", command=quit)
		self.button_quit.grid(row=14, column=1)

pannel = Interface(Tk())

while MainLoop:
	listen()
	onkeypress(LeftPressed, "Left") # ---- Tourner le cube --- #
	onkeypress(RightPressed, "Right")
	onkeypress(UpPressed, "Up")
	onkeypress(DownPressed, "Down")
	onkeyrelease(LeftRelease, "Left")
	onkeyrelease(RightRelease, "Right")
	onkeyrelease(UpRelease, "Up")
	onkeyrelease(DownRelease, "Down")

	onkey(MoveLeftW, 'w') # ---- Tourner les faces dans un sens ---- #
	onkey(MoveLeftY, 'y')
	onkey(MoveLeftR, 'r')
	onkey(MoveLeftO, 'o')
	onkey(MoveLeftG, 'g')
	onkey(MoveLeftB, 'b')
	onkey(MoveRightW, 'W') # ---- Tourner les faces dans l'autre sens ---- #
	onkey(MoveRightY, 'Y')
	onkey(MoveRightR, 'R')
	onkey(MoveRightO, 'O')
	onkey(MoveRightG, 'G')
	onkey(MoveRightB, 'B')

	onkey(showLetters, 'l') # ---- Afficher les touches ---- #
	onkey(showLetters, 'L')

	onkey(quit, "Escape") # ---- Quitter ---- #

	if LEFT: PosX -= 2
	if RIGHT: PosX += 2
	if UP: PosY -= 2
	if DOWN: PosY += 2
	if PosX >= 361: PosX = 1
	if PosY >= 361: PosY = 1
	if PosX <= -1: PosX = 359
	if PosY <= -1: PosY = 359
	update_cube()
	# print(PosX, PosY)

pannel.destroy()
bye()
