from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def drawRect(w=0.4,h=0.4,xc=0,yc=0,r=0,g=0,b=0,rf=0,gf=0,bf=0,lineWidth=5):
	glColor3f(rf,gf,bf)
	glBegin(GL_POLYGON)
	glVertex(w/2-w+xc,h/2-h+yc)
	glVertex(w/2-w+xc,h/2+yc)
	glVertex(w/2+xc,h/2+yc)
	glVertex(w/2+xc,h/2-h+yc)
	glEnd()
	
	glColor3f(r,g,b)
	glLineWidth(GLfloat(lineWidth))
	glBegin(GL_LINE_LOOP)
	glVertex(w/2-w+xc,h/2-h+yc)
	glVertex(w/2-w+xc,h/2+yc)
	glVertex(w/2+xc,h/2+yc)
	glVertex(w/2+xc,h/2-h+yc)
	glEnd()
	
def drawCircle(radius=0.05,xt=0,yt=0,r=0,g=0,b=0,rf=0,gf=0,bf=0,lineWidth=0.015):
	glColor3f(r,g,b)
	glBegin(GL_POLYGON)
	for theta in np.arange(0,2*pi,0.1):
		x = radius*cos(theta)
		y = radius*sin(theta)
		glVertex(x+xt,y+yt)
	glEnd()
	
	glColor3f(rf,gf,bf)
	glBegin(GL_POLYGON)
	for theta in np.arange(0,2*pi,0.1):
		x = (radius-lineWidth)*cos(theta)
		y = (radius-lineWidth)*sin(theta)
		glVertex(x+xt,y+yt)
	glEnd()		
	
def drawBody():
	drawRect(r=0.145,g=0.275,b=0.454,rf=0.984,gf=0.812,bf=0.302)	
	drawRect(0.1,0.1,0,0.25,0.145,0.275,0.454,rf=0.984,gf=0.812,bf=0.302)		
	
	drawCircle(radius=0.035,xt=-0.05,yt=0.4,r=0.145,g=0.275,b=0.454,rf=1,gf=1,bf=1,lineWidth=0.01)
	drawCircle(radius=0.035,xt=0.05,yt=0.4,r=0.145,g=0.275,b=0.454,rf=1,gf=1,bf=1,lineWidth=0.01)
	
	drawCircle(radius=0.06,yt=0.42,r=0.145,g=0.275,b=0.454,rf=0.984,gf=0.812,bf=0.302)
	drawRect(0.08,0.08,0,0.34,0.145,0.275,0.454,rf=0.984,gf=0.812,bf=0.302)	

	drawCircle(radius=0.035,yt=0.435,r=0.145,g=0.275,b=0.454,rf=0.984,gf=0.812,bf=0.302)	
	
def drawEye(reflected=1,xtraslate=0):
	
	drawCircle(radius=0.07,xt=reflected*0.115,yt=0.428,r=0.145,g=0.275,b=0.454,rf=0.773,gf=0.890,bf=0.918)
	drawCircle(radius=0.045,xt=reflected*0.05,yt=0.48,r=0.145,g=0.275,b=0.454,rf=0.773,gf=0.890,bf=0.918)
	drawCircle(radius=0.065,xt=reflected*0.08,yt=0.45,r=0.145,g=0.275,b=0.454,rf=0.263,gf=0.369,bf=0.510)
	
	glColor3f(0.145,0.275,0.454)	
	glBegin(GL_LINES)
	glVertex(reflected*0.052,0.52)
	glVertex(reflected*0.135,0.492)
	glEnd()
	
	drawCircle(radius=0.018,xt=xtraslate+0.09,yt=0.465,r=0.839,g=0.859,b=0.894,rf=0.839,gf=0.859,bf=0.894)
	drawCircle(radius=0.01,xt=xtraslate+0.06,yt=0.435,r=0.643,g=0.702,b=0.725,rf=0.643,gf=0.702,bf=0.725)

def drawArm(reflected=1):
	drawRect(w=0.03,h=0.06,xc=reflected*0.215,yc=0.155,r=0.145,g=0.275,b=0.454,rf=0.984,gf=0.812,bf=0.302)
	drawRect(w=0.13,h=0.15,xc=reflected*0.185,yc=0.045,r=0.145,g=0.275,b=0.454,rf=0.580,gf=0.584,bf=0.596)
	drawRect(w=0.155,h=0.065,xc=reflected*0.18,yc=0.095,r=0.145,g=0.275,b=0.454,rf=0.773,gf=0.890,bf=0.918)
	drawRect(w=0.155,h=0.065,xc=reflected*0.18,yc=-0.005,r=0.145,g=0.275,b=0.454,rf=0.773,gf=0.890,bf=0.918)
	drawRect(w=0.03,h=0.095,xc=reflected*0.245,yc=0.045,r=0.145,g=0.275,b=0.454,rf=0.773,gf=0.890,bf=0.918)

	glColor3f(0.145,0.275,0.454)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex(reflected*0.185,0.1275)
	glVertex(reflected*0.185,0.0625)
	glVertex(reflected*0.185,0.0275)
	glVertex(reflected*0.185,-0.0375)
	glEnd()

def drawDetails():
	glColor3f(0.145,0.275,0.454)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex(0.2,0.09)
	glVertex(-0.2,0.09)
	glVertex(0.12,0.2)
	glVertex(0.12,0.08)
	glVertex(-0.12,0.2)
	glVertex(-0.12,0.08)
	glVertex(-0.12,0.165)
	glVertex(-0.2,0.165)
	glVertex(0.12,0.165)
	glVertex(0.2,0.165)
	glEnd()

	glLineWidth(2.5)
	glBegin(GL_LINES)
	glVertex(0.05,0.23)
	glVertex(-0.05,0.23)
	glVertex(0.05,0.27)
	glVertex(-0.05,0.27)
	glVertex(0.03,0.435)
	glVertex(-0.03,0.435)
	glEnd()	
	
	drawRect(w=0.15,h=0.17,xc=-0.095,yc=-0.01,r=0.996,g=0.878,b=0.541,rf=0.996,gf=0.878,bf=0.541)
	
def drawLeg(reflected=1):
	drawRect(w=0.12,h=0.12,xc=reflected*0.17,yc=-0.17,r=0.145,g=0.275,b=0.454,rf=0.494,gf=0.502,bf=0.518)
	drawRect(w=0.09,h=0.06,xc=reflected*0.155,yc=-0.26,r=0.145,g=0.275,b=0.454,rf=0.643,gf=0.702,bf=0.725)
	drawRect(w=0.16,h=0.27,xc=reflected*0.31,yc=-0.2,r=0.145,g=0.275,b=0.454,rf=0.494,gf=0.502,bf=0.518)
	drawCircle(radius=0.01,xt=reflected*0.155,yt=-0.26,r=0.145,g=0.275,b=0.454,rf=0.145,gf=0.275,bf=0.454)
	drawCircle(radius=0.02,xt=reflected*0.215,yt=-0.26,r=0.145,g=0.275,b=0.454,rf=0.494,gf=0.502,bf=0.518)
	drawCircle(radius=0.02,xt=reflected*0.215,yt=-0.23,r=0.145,g=0.275,b=0.454,rf=1,gf=1,bf=1)

	
	glColor3f(0.145,0.275,0.454)
	glLineWidth(2.5)
	glBegin(GL_LINES)
	glVertex(reflected*0.39,-0.10)
	glVertex(reflected*0.23,-0.10)
	glVertex(reflected*0.39,-0.135)
	glVertex(reflected*0.23,-0.135)	
	glVertex(reflected*0.39,-0.17)
	glVertex(reflected*0.23,-0.17)	
	glVertex(reflected*0.39,-0.207)
	glVertex(reflected*0.23,-0.207)
	glVertex(reflected*0.39,-0.240)
	glVertex(reflected*0.23,-0.240)
	glVertex(reflected*0.39,-0.274)
	glVertex(reflected*0.23,-0.274)
	glVertex(reflected*0.39,-0.308)
	glVertex(reflected*0.23,-0.308)
	glEnd()
	
	drawCircle(radius=0.045,xt=reflected*0.095,yt=-0.305,r=1,g=1,b=1,rf=1,gf=1,bf=1,lineWidth=0.065)

	glColor3f(0.145,0.275,0.454)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex(reflected*0.108,-0.26)
	glVertex(reflected*0.14,-0.29)
	glEnd()
	
def draw():
	glClearColor(1,1,1,1)
	glClear(GL_COLOR_BUFFER_BIT)
	
	drawLeg()	
	drawLeg(-1)	

	drawBody()	
	drawEye()
	drawEye(-1,-0.16)
		
	drawCircle(radius=0.01,yt=0.495,r=1,g=1,b=1,rf=1,gf=1,bf=1)
	
	drawDetails()
	
	drawArm()
	drawArm(-1)
	
	#drawMoreDetailes:
	drawRect(w=0.06,h=0.05,xc=-0.045,yc=0.145,r=0.145,g=0.275,b=0.454,rf=0.643,gf=0.702,bf=0.725)
	drawCircle(radius=0.025,xt=0.05,yt=0.145,r=0.145,g=0.275,b=0.454,rf=0.824,gf=0.678,bf=0.275)

	glColor3f(0.145,0.275,0.454)
	glLineWidth(5)
	glBegin(GL_LINES)
	glVertex(-1,-0.335)
	glVertex(1,-0.335)
	glVertex(0.25,-0.375)
	glVertex(0.08,-0.375)	
	glVertex(-0.25,-0.375)
	glVertex(-0.06,-0.375)
	glVertex(0.1,-0.415)
	glVertex(-0.08,-0.415)
	glEnd()

	drawCircle(radius=0.005,xt=-0.04,yt=-0.375,r=0.145,g=0.275,b=0.454,rf=0.145,gf=0.275,bf=0.454)
	
	glFlush()
	
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Test")
glutDisplayFunc(draw)
glutMainLoop()