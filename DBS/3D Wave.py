from OpenGL import *
import os, sys, math, random
import pygame
from pygame.locals import *


if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'

import GL
pygame.init()

try:

    f_read = open('/Users/shenxenrv/Documents/Projects/DBS/Waves.txt','r')
    data = f_read.readlines()
    data2 = []

    for line in data:

        if line.endswith('\n'):
            line = line[:-1]
        line = line.split(', ')

        data2.append(line)

    resolution = int((data2[:1])[0][0])
    data2 = data2[1:]

    AnglePlus = int((data2[:1])[0][0])

    data2 = data2[1:]
    input("Load Successful!  Press ENTER to continue. >> ")

except:

    print ("ERROR!  The file could not be found, or is possiby corrupt.")
    print ("Check the Readme file for syntax.")
    input("Press ENTER to exit"); sys.exit()

Screen = [800, 600]
pygame.display.set_caption('3D Wave Interference Simulator - Superio, KC - 2011')

width = Screen[0]
height = Screen[1]

pygame.display.set_mode(Screen,OPENGL|DOUBLEBUF)

GL.resize(width, height)
GL.init(resolution)

PointSourceLocations = []

for line in data2:

    XYData = line[1].split(',')
    XYData = [float(XYData[0]),float(XYData[1])]

    FunctionData = line[0].split(',')
    FunctionData[0] = float(FunctionData[0])

    FunctionData[1] = float(FunctionData[1])
    FunctionData[2] = float(FunctionData[2])

    PointSourceLocations.append([FunctionData,XYData])
Angle = 0

MaxAmplitude = 0

for Wave in PointSourceLocations:
    MaxAmplitude += Wave[0][0]

Data = []
NormalData = []

ColorData = []

for z in range(resolution):
    for x in range(resolution):
        Data.append([x,0,z])
        NormalData.append([0,1,0])
        ColorData.append([0,0,0])
view = [-resolution/2,-6,-60,0,0] #x,y,z,xrot,yrot

viewtype = ['Line','Quads','No Texture','No Light']

glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
glDisable(GL_TEXTURE_2D)
glDisable(GL_LIGHTING)

keypress = [False,False,False,False]

def GetInput():

    global view, viewtype, keypress
    keystate = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == QUIT or keystate[K_ESCAPE]:
            pygame.quit(); sys.exit()

    if keystate[K_UP]: view[2] -= 0.1
    if keystate[K_DOWN]: view[2] += 0.1

    if keystate[K_LEFT]: view[0] -= 0.1
    if keystate[K_RIGHT]: view[0] += 0.1

    if keystate[K_KP2] or keystate[K_2]: view[3] -= 1
    if keystate[K_KP8] or keystate[K_8]: view[3] += 1

    if keystate[K_KP4] or keystate[K_4]: view[4] -= 1
    if keystate[K_KP6] or keystate[K_6]: view[4] += 1

    if keystate[K_F1]:

        if not keypress[0]:

            if viewtype[0] == 'Fill':       viewtype[0] = 'Line';       glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

            elif viewtype[0] == 'Line':     viewtype[0] = 'Point';      glPolygonMode(GL_FRONT_AND_BACK, GL_POINT)
            elif viewtype[0] == 'Point':    viewtype[0] = 'Fill';       glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

            print (viewtype[0])

        keypress[0] = True

    else: keypress[0] = False

    if keystate[K_m]:
        if not keypress[1]:
            if viewtype[1] == 'Quads':      viewtype[1] = 'Triangles'
            else:                           viewtype[1] = 'Quads'
            print (viewtype[1])
            keypress[1] = True
    else: keypress[1] = False

    if keystate[K_F2]:

        if not keypress[2]:

            if viewtype[2] == 'Texture':                viewtype[2] = 'No Texture'; glDisable(GL_TEXTURE_2D)

            elif viewtype[2] == 'No Texture':           viewtype[2] = 'Single Color Height'
            elif viewtype[2] == 'Single Color Height':  viewtype[2] = 'Rainbow Color Height'
            elif viewtype[2] == 'Rainbow Color Height': viewtype[2] = 'Texture'; glEnable(GL_TEXTURE_2D)
            print (viewtype[2])
            keypress[2] = True
    else: keypress[2] = False

    if keystate[K_F3]:

        if not keypress[3]:

            if viewtype[3] == 'Light':      viewtype[3] = 'No Light';   glDisable(GL_LIGHTING)

            else:                           viewtype[3] = 'Light';      glEnable(GL_LIGHTING)
            print (viewtype[3])

            keypress[3] = True

    else: keypress[3] = False

def UpdateNormalMap():

    global NormalData
    Vertex = 0

    for z in range(resolution):

        for x in range(resolution):

            try:

                y2 = Data[Vertex]
                y1 = Data[Vertex-1]
                y3 = Data[Vertex+1]

                Theta1 = math.atan(y2-y1)
                Theta2 = math.atan(y2-y1)
                Angle1 = 3.142+Theta2+Theta2

                y2 = Data[Vertex]
                y1 = Data[Vertex-resolution]
                y3 = Data[Vertex+resolution]

                Theta1 = math.atan(y2-y1)
                Theta2 = math.atan(y2-y1)
                Angle2 = 3.142+Theta2+Theta2

                x = math.sin(Angle1)
                z = math.sin(Angle2)
                y = 1

                NormalData[Vertex] = [x,y,z]

            except: pass
            Vertex += 1

def UpdateColorMap(Mode):

    global ColorData
    Vertex = 0

    if Mode == 'Single':

        for z in range(resolution):

            for x in range(resolution):
                Height = ((Data[Vertex]/MaxAmplitude)/2.0)+0.5
                ColorData[Vertex] = [Height,Height,Height]
                Vertex += 1
    if Mode == 'Rainbow':

        for z in range(resolution):

            for x in range(resolution):
                ColorData[Vertex] = GetColor(Data[Vertex])
                Vertex += 1

ColorPalette = [[1.00, 0.00, 0.00],[1.00, 0.05, 0.00],[1.00, 0.10, 0.00],[1.00, 0.15, 0.00],[1.00, 0.20, 0.00],[1.00, 0.25, 0.00],[1.00, 0.30, 0.00],[1.00, 0.35, 0.00],[1.00, 0.40, 0.00],[1.00, 0.45, 0.00],[1.00, 0.50, 0.00],[1.00, 0.55, 0.00],[1.00, 0.60, 0.00],[1.00, 0.65, 0.00],[1.00, 0.70, 0.00],[1.00, 0.75, 0.00],[1.00, 0.80, 0.00],[1.00, 0.85, 0.00],[1.00, 0.90, 0.00],[1.00, 0.95, 0.00],
                [1.00, 1.00, 0.00],[0.95, 1.00, 0.00],[0.90, 1.00, 0.00],[0.85, 1.00, 0.00],[0.80, 1.00, 0.00],[0.75, 1.00, 0.00],[0.70, 1.00, 0.00],[0.65, 1.00, 0.00],[0.60, 1.00, 0.00],[0.55, 1.00, 0.00],[0.50, 1.00, 0.00],[0.45, 1.00, 0.00],[0.40, 1.00, 0.00],[0.35, 1.00, 0.00],[0.30, 1.00, 0.00],[0.25, 1.00, 0.00],[0.20, 1.00, 0.00],[0.15, 1.00, 0.00],[0.10, 1.00, 0.00],[0.05, 1.00, 0.00],
                [0.00, 1.00, 0.00],[0.00, 1.00, 0.05],[0.00, 1.00, 0.10],[0.00, 1.00, 0.15],[0.00, 1.00, 0.20],[0.00, 1.00, 0.25],[0.00, 1.00, 0.30],[0.00, 1.00, 0.35],[0.00, 1.00, 0.40],[0.00, 1.00, 0.45],[0.00, 1.00, 0.50],[0.00, 1.00, 0.55],[0.00, 1.00, 0.60],[0.00, 1.00, 0.65],[0.00, 1.00, 0.70],[0.00, 1.00, 0.75],[0.00, 1.00, 0.80],[0.00, 1.00, 0.85],[0.00, 1.00, 0.90],[0.00, 1.00, 0.95],
                [0.00, 1.00, 1.00],[0.00, 0.95, 1.00],[0.00, 0.90, 1.00],[0.00, 0.85, 1.00],[0.00, 0.80, 1.00],[0.00, 0.75, 1.00],[0.00, 0.70, 1.00],[0.00, 0.65, 1.00],[0.00, 0.60, 1.00],[0.00, 0.55, 1.00],[0.00, 0.50, 1.00],[0.00, 0.45, 1.00],[0.00, 0.40, 1.00],[0.00, 0.35, 1.00],[0.00, 0.30, 1.00],[0.00, 0.25, 1.00],[0.00, 0.20, 1.00],[0.00, 0.15, 1.00],[0.00, 0.10, 1.00],[0.00, 0.05, 1.00],
                [0.00, 0.00, 1.00],[0.05, 0.00, 1.00],[0.10, 0.00, 1.00],[0.15, 0.00, 1.00],[0.20, 0.00, 1.00],[0.25, 0.00, 1.00],[0.30, 0.00, 1.00],[0.35, 0.00, 1.00],[0.40, 0.00, 1.00],[0.45, 0.00, 1.00],[0.50, 0.00, 1.00],[0.55, 0.00, 1.00],[0.60, 0.00, 1.00],[0.65, 0.00, 1.00],[0.70, 0.00, 1.00],[0.75, 0.00, 1.00],[0.80, 0.00, 1.00],[0.85, 0.00, 1.00],[0.90, 0.00, 1.00],[0.95, 0.00, 1.00],
                [1.00, 0.00, 1.00],[1.00, 0.00, 0.95],[1.00, 0.00, 0.90],[1.00, 0.00, 0.85],[1.00, 0.00, 0.80],[1.00, 0.00, 0.75],[1.00, 0.00, 0.70],[1.00, 0.00, 0.65],[1.00, 0.00, 0.60],[1.00, 0.00, 0.55],[1.00, 0.00, 0.50],[1.00, 0.00, 0.45],[1.00, 0.00, 0.40],[1.00, 0.00, 0.35],[1.00, 0.00, 0.30],[1.00, 0.00, 0.25],[1.00, 0.00, 0.20],[1.00, 0.00, 0.15],[1.00, 0.00, 0.10],[1.00, 0.00, 0.05],
                [0.00, 1.00, 0.00]]

def GetColor(Height):

    Height /= MaxAmplitude #Height in range -1 to 1
    Height = (Height+1.0)/2.0 #Height in range 0 to 1
    return ColorPalette[int(Height*120.0)]

def Update():

    global Angle,Data
    Angle -= AnglePlus
    if Angle == -360: Angle = 0

    Vertex = 0

    for z in range(resolution):

        for x in range(resolution):
            Height = 0

            for PointSourceLocation in PointSourceLocations:
                #[FunctionData,XYData]
                #[[Amplitude,Frequency,Shift],[xcoordinate,zcoordinate]]
                Height += GetHeight(x,z,PointSourceLocation)
            Data[Vertex] = Height
            Vertex += 1

    if viewtype[3] == 'Light': #If lighting enabled, update normal map.
        UpdateNormalMap()

    if viewtype[2] == 'Single Color Height':
        UpdateColorMap('Single')

    if viewtype[2] == 'Rainbow Color Height':
        UpdateColorMap('Rainbow')

def GetHeight(x,z,PointSourceLocation):
    FunctionData = PointSourceLocation[0]
    Coordinates = PointSourceLocation[1]
    XDifference = x - Coordinates[0]
    ZDifference = z - Coordinates[1]
    Distance = math.sqrt(XDifference**2 + ZDifference**2)
    Theta = FunctionData[1]*Distance
    Height = FunctionData[0]*math.sin(Theta+math.radians(Angle+FunctionData[2]))
    return Height

def Textures():

    global Textures
    Surface = pygame.image.load('Water.jpg')

    Data = pygame.image.tostring(Surface, "RGBA", 1)
    Textures = glGenTextures(2)

    glBindTexture(GL_TEXTURE_2D, Textures[0])
    glTexImage2D( GL_TEXTURE_2D, 0, GL_RGBA, Surface.get_width(), Surface.get_height(), 0,
                  GL_RGBA, GL_UNSIGNED_BYTE, Data )

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

def Draw():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(view[0],-6,view[2])
    glRotatef(view[3],1,0,0)

    glRotatef(view[4],0,1,0)
    Vertex = 0

    glBindTexture(GL_TEXTURE_2D, Textures[0])

    for z in range(resolution-1):

        if viewtype[1] == 'Quads':  glBegin(GL_QUAD_STRIP)
        else:                       glBegin(GL_TRIANGLE_STRIP)

        for x in range(resolution):

            glColor3f(1,1,1)

            if viewtype[3] == 'Light':
                Normal = NormalData[Vertex]
                glNormal3f(Normal[0],Normal[1],Normal[2])

            if viewtype[2] == 'Texture':
                glTexCoord2f(float(x)/float(resolution),float(z)/float(resolution))

            if viewtype[2] == 'Single Color Height' or viewtype[2] == 'Rainbow Color Height':
                Color = ColorData[Vertex]
                glColor3f(Color[0],Color[1],Color[2])
            glVertex3f(x,Data[Vertex],z)

            if viewtype[3] == 'Light':
                Normal = NormalData[Vertex+resolution]
                glNormal3f(Normal[0],Normal[1],Normal[2])

            if viewtype[2] == 'Texture':
                glTexCoord2f(float(x)/float(resolution),float(z+1)/float(resolution))

            if viewtype[2] == 'Single Color Height' or viewtype[2] == 'Rainbow Color Height':
                Color = ColorData[Vertex+resolution]

                glColor3f(Color[0],Color[1],Color[2])
            glVertex3f(x,Data[Vertex+resolution],z+1)

            Vertex += 1
        glEnd()

    for PointSourceLocation in PointSourceLocations:

        #[FunctionData,XYData]
        #[[Amplitude,Frequency,Shift],[xcoordinate,zcoordinate]]

        Coordinates = PointSourceLocation[1]

        glBegin(GL_LINES)
        glVertex3f(Coordinates[0],5,Coordinates[1])

        glVertex3f(Coordinates[0],-5,Coordinates[1])
        glEnd()
    pygame.display.flip()

def main():

    Textures()

    while True:

        GetInput()
        Update()
        Draw()

if __name__ == '__main__': main()
