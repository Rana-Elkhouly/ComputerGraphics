from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def myInit():
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(60,1,1,60)
	gluLookAt(
	8,9,10,
	0,0,0,
	0,1,0)
	
	glClearColor(0.9,0.9,0,1)

def draw_xyz():
	glBegin(GL_LINES)
	glColor3f(1,0,0)	
	glVertex(0,0)
	glVertex(10,0)
	glColor3f(0,1,0)
	glVertex(0,0)
	glVertex(0,10)
	glColor3f(0,0,1)
	glVertex(0,0)
	glVertex(0,0,10)
	glEnd()
	
angle = 0
step = 0
zStep = 0 
forward = True
Rotation = -90 
	
def draw():
	global angle
	global step
	global forward
	global zStep
	global Rotation
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	glClear(GL_COLOR_BUFFER_BIT)
	#draw_xyz()
	

	
	
	glLoadIdentity()
	glColor3f(0.5,0.5,0.5)
	glBegin(GL_POLYGON)
	glVertex(-4,0,10)
	glVertex(4,0,10)
	glVertex(4,0,-60)
	glVertex(-4,0,-60)
	glEnd()

	glLoadIdentity()
	glColor3f(0,0,0)
	glRotate(Rotation,0,1,0)
	glTranslate(-step,0,-zStep)
	glutSolidSphere(1,10,10)
	
	glLoadIdentity()
	glColor3f(0.753,0.149,0.176)
	glRotate(Rotation,0,1,0)
	glTranslate(step,0,zStep)
	glScale(1,0.25,0.5)
	glutSolidCube(5)
		
	
	glTranslate(0,5,0)		#or	#glLoadIdentity()
	glScale(0.5,1,1)			#glTranslate(0,5*0.25,0)
								#glScale(0.5,0.25,0.5)
	glutSolidCube(5)	
	
	glLoadIdentity()
	glColor3f(0,0,1)
	glRotate(Rotation,0,1,0)	
	glTranslate(step,0,zStep)
	glTranslate(0.5*5,-0.5*0.25*5,0.5*0.5*5)
	glRotate(angle,0,0,1)
	glutWireTorus(0.125,0.5,10,10)

	glLoadIdentity()
	glRotate(Rotation,0,1,0)	
	glTranslate(step,0,zStep)
	glTranslate(-0.5*5,-0.5*0.25*5,0.5*0.5*5)
	glRotate(angle,0,0,1)		
	glutWireTorus(0.125,0.5,10,10)

	glLoadIdentity()
	glRotate(Rotation,0,1,0)	
	glTranslate(step,0,zStep)
	glTranslate(-0.5*5,-0.5*0.25*5,-0.5*0.5*5)
	glRotate(angle,0,0,1)	
	glutWireTorus(0.125,0.5,10,10)

	glLoadIdentity()
	glRotate(Rotation,0,1,0)	
	glTranslate(step,0,zStep)
	glTranslate(0.5*5,-0.5*0.25*5,-0.5*0.5*5)
	glRotate(angle,0,0,1)	
	glutWireTorus(0.125,0.5,10,10)	
	

	
	glutSwapBuffers()	#instead of flush in 2D
 
	if forward:
		angle -= 0.5
		step += 0.01
		if step > 10:
			forward = False
	else:
		angle += 0.5
		step -= 0.01
		if step < -5:
			forward = True			
			
def arrowHandler(key,x,y):	#x,y is the position of the mouse at t we press a key
	global zStep
	if key == GLUT_KEY_RIGHT:		
		zStep -= 0.1 
	elif key == GLUT_KEY_LEFT:
		zStep += 0.1	
	draw()	
			
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"Moving Car")
myInit()	
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutSpecialFunc(arrowHandler)	#to handle the special keyboard keys
glutMainLoop()
