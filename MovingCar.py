from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

def myInit():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60,1,1,60)
	gluLookAt(
	8,9,10,
	0,0,0,
	0,1,0)
	
	glClearColor(1,1,1,1)
	
def triangularPrism():
	global step
	glLoadIdentity()
	glColor3f(0.196,0.196,0.196)
	#glTranslate(step,0,0)
	glTranslate(-0.2,-0.1,-1)
	glScale(0.1,0.2,0.275)
	
	glBegin(GL_POLYGON)
	glVertex(0,0,5)
	glVertex(0,5,5)
	glVertex(5,0,5)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex(0,0,-5)
	glVertex(0,5,-5)
	glVertex(5,0,-5)
	glEnd()
	
	glBegin(GL_POLYGON)
	glVertex(0,0,5)
	glVertex(0,0,-5)
	glVertex(5,0,-5)
	glVertex(5,0,5)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex(0,0,5)
	glVertex(0,0,-5)
	glVertex(0,5,-5)
	glVertex(0,5,5)
	glEnd()

	glBegin(GL_POLYGON)
	glVertex(0,5,5)
	glVertex(0,5,-5)
	glVertex(5,0,-5)
	glVertex(5,0,5)
	glEnd()
	
def wheel(x,y,z,r=0,rx=0,ry=0,rz=0):
	global step
	glLoadIdentity()
	#glTranslate(step,0,0)
	glRotate(r,rx,ry,rz)
	glColor3f(0.345,0.346,0.319)
	glTranslate(x,y,z)
	glutSolidSphere(0.37,10,10)	
	
	glLoadIdentity()
	glColor3f(0.196,0.196,0.196)	
	#glTranslate(step,0,0)
	glRotate(r,rx,ry,rz)
	glTranslate(x,y,z)
	glutSolidTorus(0.125,0.5,10,10)	

def carBody():
	glLoadIdentity()	
	glColor3f(0.753,0.149,0.176)
	#glTranslate(step,0,0)
	glScale(1,0.25,0.5)
	glutSolidCube(5)

	glColor3f(0.753,0.149,0.176)	
	glTranslate(-1,5,0)
	glScale(0.6,1,1)
	glutSolidCube(5)

def carLight(x,y,z):
	glLoadIdentity()
	#glTranslate(step,0,0)
	glColor3f(0.988,0.941,0.475)	
	glTranslate(x,y,z)
	glutSolidSphere(0.3,10,10)
	
def window(x1,x2,y,z):
	glLoadIdentity()
	glColor3f(0.196,0.196,0.196)
	glBegin(GL_POLYGON)
	glVertex(x1,y,z)
	glVertex(x1,-y,z)
	glVertex(x2,-y,z)
	glVertex(x2,y,z)
	glEnd()
	
def block(x,z):
	glLoadIdentity()
	glColor3f(0.89,0.5,0.06)
	glScale(2,0.75,0.75)
	glTranslate(x,0,z)
	glutSolidCube(1)

	glLoadIdentity()
	glColor3f(0,0,0)
	glScale(2,0.75,0.75)
	glTranslate(x+1,0,z)
	glutSolidCube(1)
	
def square(r,g,b,x1,x2,y,z):
	glLoadIdentity()
	glColor3f(r,g,b)	
	glBegin(GL_POLYGON)
	glVertex(x1,y,z)
	glVertex(x1,y,-z)
	glVertex(x2,y,-z)
	glVertex(x2,y,z)
	glEnd()	
	
def star(x,y):
	glColor3f(0.992,0.992,0.859)
	glLoadIdentity()
	glBegin(GL_POINTS)
	glVertex(x,y)
	glEnd()

def moon():
	glColor3f(0.996,0.996,0.858)
	glLoadIdentity()
	glTranslate(-2,6,-7)
	glutSolidSphere(1,20,20)
	
def tower(x,sy):
	glColor3f(0.067,0.110,0.114)
	glLoadIdentity()
	glTranslate(5+x,0,-5)
	glScale(1,sy,1)
	glutSolidCube(2)	
	
def sphere(r,g,b,x,y,z,radius):
	glLoadIdentity()
	glColor3f(r,g,b)
	glLoadIdentity()
	glTranslate(x,y,z)
	glutSolidSphere(radius,20,20)

angle = 0
step = 0
forward = True

randomListx=[]
randomListy=[]

for i in range(100):
	randomListx.append(random.uniform(-25,15))
	randomListy.append(random.uniform(5,10))
	
def draw():
	global angle
	global step
	global forward
	glMatrixMode(GL_MODELVIEW)
	glClear(GL_COLOR_BUFFER_BIT)
	glClearColor(0.031,0.196,0.224,1)

	#sky
	for i in range(100):
		star(randomListx[i],randomListy[i])
	moon()	
	
	#view
	tower(-2,7)	
	tower(-15,5)
	tower(-18,6)
	tower(-20,7)
	tower(-12,8)
	tower(-24,4.5)
	tower(-30,5)
	tower(-9,6)
	tower(-5,5)
	tower(-3,6)
	tower(-7,4)
	tower(0,5.5)
	tower(2,6.5)
	sphere(0.008,0.137,0,4,4,0,1.5)
	sphere(0.008,0.071,0,5,5.5,5,1.5)
	sphere(0.016,0.258,0,5,3.5,-2,1.5)
		
	#road
	square(0.102,0.173,0,10,-60,0,10)
	square(0.251,0.216,0.184,10,-60,0,4)

	for i in range(-15,15,6):
		square(1,1,1,i,i-4,0,0.5)
	for i in range(-15,6,2):
		block(i,-6)
		block(i,5)

	#car
	wheel(-0.5*5+1,-0.5*0.25*5,-0.5*0.5*5)
	wheel(0.5*5-1,-0.5*0.25*5,-0.5*0.5*5)
	window(-2.15,-0.9,0.5,-2.5)
	window(-3.7,-2.45,0.5,-2.5)
	carBody()
	wheel(0.5*5-1,-0.5*0.25*5,0.5*0.5*5)
	wheel(-0.5*5+1,-0.5*0.25*5,0.5*0.5*5)
	window(-2.15,-0.9,0.5,0)
	window(-3.7,-2.45,0.5,0)
	carLight(2.2,0.2,0.9)
	carLight(2.2,0.2,-1.4)
	triangularPrism()
	glutSwapBuffers()
 
	if forward:
		angle -= 0.5
		step += 0.01
		if step > 5:
			forward = False
	else:
		angle += 0.5
		step -= 0.01
		if step < -7:
			forward = True			


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()