#!/usr/bin/env python
from pyglet import options as a
a["debug_gl"]=False
from pyglet.gl import GLfloat,glColor3fv,glBegin,glEnd,glVertex2f,glClear,GL_COLOR_BUFFER_BIT
from pyglet.clock import set_fps_limit as a,tick
a(30)
from pyglet.window import Window as W
from os import listdir as LvL
LvL=iter(sorted(LvL for LvL in LvL("./") if LvL.endswith(".txt"))).next
from random import random,choice
W=W(fullscreen=True)
W.maximize()
Hei=W.height
Wid=W.width
GLfloat*=3
Col=GLfloat(0.,0.,0.),GLfloat(0.,0.,1.),GLfloat(0.,1.,0.),GLfloat(0.,1.,1.),GLfloat(1.,0.,0.),GLfloat(1.,0.,1.),GLfloat(1.,1.,0.),GLfloat(1.,1.,1.)
GLfloat.Hit=True
GLfloat.C=property(lambda s:s)
class Nil:Hit=False
class Ply:
	def __init__(s,*x):
		s.x,s.y,s.d=x or (P.x,P.y,P.d)
		if x:
			globals()["P"]=s
			@W.event
			def on_mouse_press(x,y,X,Y,D={(-1,-1):s.lwd,(-1,0):s.lwd,(-1,1):s.ltr,(0,-1):s.bwd,(0,0):s.fwd,(0,1):s.fwd,(1,-1):s.rwd,(1,0):s.rwd,(1,1):s.rtr}):
				if X==4:return kenter()
				X=s.x,s.y
				D[-(x<Wid/3) or x>(Wid<<1)/3,-(y<Hei/3) or y>(Hei<<1)/3]()
				if not(0<=s.y<len(L) and 0<=s.x<len(L[0])) or L[s.y][s.x].Hit:s.x,s.y=X
	def ltr(s):s.d=(3,0,1,2)[s.d]
	def rtr(s):s.d=(1,2,3,0)[s.d]
	def fwd(s):
		s.x+=(+1,00,-1,00)[s.d]
		s.y+=(00,-1,00,+1)[s.d]
	def bwd(s):
		s.x+=(-1,00,+1,00)[s.d]
		s.y+=(00,+1,00,-1)[s.d]
	def lwd(s):
		s.x+=(00,+1,00,-1)[s.d]
		s.y+=(+1,00,-1,00)[s.d]
		return s
	def rwd(s):
		s.x+=(00,-1,00,+1)[s.d]
		s.y+=(-1,00,+1,00)[s.d]
		return s
class Win:
	C=property(lambda s:choice(Col))
	Hit=property(lambda s:not mkL())
Win=Win()
def mkL(Lv=None):
	if Lv is None:Lv=LvL()
	globals()["kenter"]=lambda:mkL(Lv)
	L=open(Lv).read().split("\n")
	mL=max(len(L) for L in L)
	globals()["L"]=[[Nil if L in " 0" else Win if L=="!" else
                         (Nil,Ply(x,y,">^<v".index(L)))[0] if L in ">^<v" else
                         Col[int(L)] if L in "1234567" else
                         GLfloat(random(),random(),random())
                         for x,L in enumerate(L)]+[Nil]*(mL-len(L)) for y,L in enumerate(L)]
	for mL in reversed(Col):
		glColor3fv(mL)
		glBegin(7)
		glVertex2f(0,0)
		glVertex2f(Wid,0)
		glVertex2f(Wid,Hei)
		glVertex2f(0,Hei)
		glEnd()
		W.flip()
		tick()
W.dispatch_events()
mkL()
while not W.has_exit:
	tick()
	W.dispatch_events()
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(7)
	for b,a in enumerate((Ply().lwd().lwd(),Ply().lwd(),Ply(),Ply().rwd(),Ply().rwd().rwd())):
			while 0<=a.y<len(L) and 0<=a.x<len(L[0]) and L[a.y][a.x] is Nil:a.fwd()
			glColor3fv(L[a.y][a.x].C if 0<=a.y<len(L) and 0<=a.x<len(L[0]) else Col[0])
			glVertex2f(Wid/5*b,Hei/3)
			glVertex2f(Wid/5*(b+1),Hei/3)
			glVertex2f(Wid/5*(b+1),(Hei<<1)/3)
			glVertex2f(Wid/5*b,(Hei<<1)/3)
	glEnd()
	glColor3fv(choice(Col))
	glBegin(1)
	glVertex2f(Wid/3,0)
	glVertex2f(Wid/3,Hei)
	glVertex2f((Wid<<1)/3,0)
	glVertex2f((Wid<<1)/3,Hei)
	glVertex2f(Wid/3,Hei/3)
	glVertex2f((Wid<<1)/3,Hei/3)
	glVertex2f(0,(Hei<<1)/3)
	glVertex2f(Wid/3,(Hei<<1)/3)
	glVertex2f((Wid<<1)/3,(Hei<<1)/3)
	glVertex2f(Wid,(Hei<<1)/3)
	glEnd()
	W.flip()
W.close()
