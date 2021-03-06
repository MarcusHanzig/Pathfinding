from collections import namedtuple

class WrongMapSize(ValueError):
    pass

class LinesOfArrayNotEquallyLong(ValueError):
    pass

class NotAnArray(ValueError):
    pass

class ArrayContainsNonInteger(ValueError):
    pass

class NumberHasToBe0Or1(ValueError):
    pass

def validateMapSize(array):
    # has to be an 2-dimensional array containing 0's and 1's and size between 20x20 and 50x50
    if not isinstance(array, list):
        raise NotAnArray(array)
    for line in array:
        if not isinstance(line, list):
            raise NotAnArray(line)
        for number in line:
            if not isinstance(number, int):
                raise ArrayContainsNonInteger(number)
            if number not in [0,1]:
                raise NumberHasToBe0Or1(number)

    height=len(array)
    width=len(array[0])
    if height < 10 or \
       height > 50 or \
       width  < 10 or \
       width  > 50: 
        raise WrongMapSize(height,width)
    for line in array:
        if len(line)!=width:
            raise LinesOfArrayNotEquallyLong(len(line), 'length of the line',line)


PointTuple=namedtuple('PointTuple', 'xsquare ysquare sizesquare indexsquare'#number,  #orignial Value of the Field, -1 not passable, 0 passable
                                    #xsquare, #x-coordinate of the left bottom cornerstone of the square containing the field
                                    #ysquare, #y-cordinate of the right top ... (see above)
                                    #sizesquare, #size of the square containing the point
                                    #indexsquare, #Index of the square containing the point
                                              )

Square=namedtuple('Square', 'x y n')#x, # coordinate of left side
                            #y, # coordinate of bottom side
                            #n, # size of the Square
                            #])

def arrayWithSquareInfo(array):
    arraySquareInfo=array
    h,w=len(array),len(array[0])                    
    Edges=[]
    SqIndex=0
    for y in range(h):
        for x in range(w):
    
            if len(arraySquareInfo[x][y])>0:
                continue
            if arraySquareInfo[x][y]==-1:
                arraySquareInfo[x][y]=PointTuple(arraySquareInfo[x][y],x,y,0,-1)
                continue
            SqSize=1
            Bool=True
            while  Bool:# n+1<min(w-x,h-y) and    if n+1=min: n=w-1-x
                if SqSize==w-x or SqSize==h-y:#    min(w-x,h-y):
                    Bool=False
                    break

                for j in range(SqSize+1): #step one: 0,1
                    if arraySquareInfo[x+j][y+SqSize]!=0 or \
                       arraySquareInfo[x+SqSize][y+j]!=0 :
                        Bool=False
                        break  
                if Bool:
                    SqSize+=1 
            
            Edges=Edges+[Square(x,y,SqSize)]   
            
            for y2 in range(SqSize):
                for x2 in range(SqSize):
                    arraySquareInfo[x+x2][y+y2]=PointTuple(x,y,SqSize,SqIndex)#[x,y,n,Edges_index] # n=size arraySquareInfo[x+x2][y+y2],
                    
            SqIndex=SqIndex +1
    return(Edges,arraySquareInfo)
####    ######################

def NeighborSquares(arraySquare):
    height,width=len(arraySquare),len(arraySquare[0])

    def Update(Set,xn,yn):
        #def Square(PointInfo):
        #    return(Square(PointInfo.x,PointInfo.y,PointInfo.sizesquare)

        if 0 <= xn < height and \
           0 <= yn < width :
            #LongSquare=Square(arraySquare[xn][yn])
            #Set.add(Square(LongSquare.x, LongSquare.y, Longsquare.sizesquare) #Set.add(Square(arraySquare[xn][yn]))
            point=arraySquare[xn][yn]
            Set.add(Square(point.xsquare,point.ysquare,point.sizesquare))
        return(Set)

    neighborSquare=[[0 for x in arraySquare] for y in arraySquare[0]]#[[0 for x in range(len(arraySquare))] for y in range(len(arraySquare[0]))]
    for x in range(len(arraySquare)): 
        for y in range(len(arraySquare[0])):  
            if x != arraySquare.xsquare or \
               y != arraySquare.ysquare:
                neighborSquare[x][y]=neighborSquare[neighborSquare[x][y].x][neighborSquare[x][y].y]
                continue

            SetNeighbor=set()
            size=arraySquare.sizesquare
            # Update Squares of all points that are neighbor of the square containing (x,y):
            for n in range(1+arraySquare.sizesquare): 
                for x_,y_ in [[x-1,y+n],[x+size,y+n],[x+n,y-1],[x+n,y+size],]:
                    SetNeighbor=Update(SetNeighbor,x_,y_)
            neighborSquare[x][y]=SetNeighbor

    return(neighborSquare)


def DistancesOfSquares(edges,arraySquare,neighborSquares):
    
    Matrix_way2=[[0 for point2 in edges] for point1 in edges]
    Way3min=[[0 for way in range(180)] for y in range(min(len(edges)**2,15000))] 
    Number_way=[0 for way in range(180)]
    Number_way_length=180
    open_ways=0


    for x in range(len(edges)):
        way_self=Edges[x].SqSize
        Matrix_way2[x][x]=way_self  #corresponts to edges[x] to edges[x] points
        Way3min[Number_way[way_self]][way_self]=[x,x]
        Number_way[way_self]=1+Number_way[way_self]
        open_ways=open_ways+1

    count=0
    way=0


    #while open_ways>0 and way<2 and count<10:
    for way in range(180):

        if Number_way[way]>0:
            for n in range(Number_way[way]):



                [p1,p2]=Way3min[n][way]


                open_ways=open_ways-1

                #neighbor=circle3(Edges[p2][0],Edges[p2][1],Edges[p2][2]) #list of [x,y,n,Edges_index], now: number xsquare, ysquare, sizesquare, SquareIndex
                neighbors=neighborSquares
            #way12=Matrix_way2[p1][p2]


                for p3_pointway in neighbors:
                
                    p3=p3_pointway.SquareIndex
                    if Matrix_way2[p1][p3] ==0:
                        mat=way+p3_pointway.sizesquare
                        open_ways=open_ways+1
                        Matrix_way2[p1][p3]=mat
                        Way3min[Number_way[mat]][mat]=[p1,p3]
                        Number_way[mat]=1+Number_way[mat]
    return(Matrix_way2)     


class Map:
    def __init__(self, array):
        validateMapSize(array)
        self.array=array
        self.height=len(array)
        self.width=len(array[0])

    def get(self,x,y):
        return(self.array[x][y])

    def __repr__(self):
        pass
        #return (f'{self.__class__.__name__}('
        #        f'{self.array!r})')

class StructuredMap():#Map

    def __init__(self, array):
        validateMapSize(array)
        self.array=array
        self.height=len(array)
        self.width=len(array[0])
        self.edges , \
        self.arraySquare=arrayWithSquareInfo(array)
        self.neighborSquares=NeighborSquares(self.arraySquare)

        #not ready:
        self.distancesOfSquares=DistancesOfSquares(self.edges,self.arraySquare,self.neighborSquares)

    def getSquare(self,x,y):
        return(self.arraySquare[x][y])

    def getEdges(self):
        return(self.edges) 

    def getNeighborSquares(self,x,y):
        return(self.neighborSquares[x][y])
                    
    def __str__(self):
        arrayprint=[['' for _ in self.array[0]] for _ in self.array]
        for x in range(self.width):
            for y in range(self.hight): 
                arrayprint[x][y]=str(self.arraySquare[x][y].sizesquareSqSize)+'-'+str(self.arraySquare[x][y].indexsquare)
                if arraySquareInfo[x][y].SqSize==0:
                    arrayprint[x][y]='XXX'
        print(arrayprint)
        

    def __repr__(self):
        pass
        #return (f'{self.__class__.__name__}('
        #        f'{self.array!r})')     
                    
                    
class Path:
    def __init__(self, StructuredMap,x_start,y_start,x_goal,y_goal):
        self.map=StructuredMap
        self.x_start=x_start
        self.y_start=y_start
        self.x_goal=x_goal
        self.y_goal=y_goal
        self.path=self.pathfinding()#list of square-indexes
        self.pathset=set(self.path)
                    
    def pathfinding(self):
        path=[]
        location=self.map.arraySquareInfo[self.x_start][self.y_start]
        goal=self.map.arraySquareInfo[self.x_goal][self.y_goal]
        while true:
            path.add(location) #PointTuple(x,y,SqSize,SqIndex)
            if location==goal:
                break
            for loc in self.map.neighborSquares[location.x][location.y]:
                #a,b=loc.indexsquasre,goal.indexsquare
                if self.distancesOfSquares[loc.indexsquare][goal.indexsquare] < self.distancesOfSquares[loc.indexsquare][goal.indexsquare] :
                    location=loc
        
                    path.add(location)
        return(path)
        
         
    def __str__(self):
        arrayprint=[['' for _ in self.map.array[0]] for _ in self.map.array]
        for x in range(self.width):
            for y in range(self.hight): 
                if (x,y) in self.pathset:
                    arrayprint[x][y]=self.path.index((x,y))
                    continue
                if arraySquareInfo[x][y].sizesquare==0:
                    arrayprint[x][y]='X'
                    continue
                arrayprint[x][y]=' '
        print(arrayprint)
        print(self.path)
        
                    
                    
    def __repr__(self):
        pass
        #return (f'{self.__class__.__name__}('
        #        f'{self.path!r})')  





Field=[
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,1,1,1,1,0,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        
MapF=StructuredMap(Field)




























#class Point:
#    def __init__(self, x,y,number):
#        self.x=x
#        self.y=y
#        self.number=number#

#    #def setNumber(number):
#    #    self.number=number#

#    def __repr__(self):
#        return (f'{self.__class__.__name__}('
#                f'{self.x!r},{self.y!r})')

#class detailedPoint(Point):
#    def __init__(self,*args,**kwargs):
#        super().__init__(*args,**kwargs)
#        self.SquarePoint=Point(0,0)
#        self.SquareSize=0
#    def setSquare(Point,size):
#        self.SquarePoint=Point
#        self.SquareSize=size

#    def __repr__(self):
#        return (f'{self.__class__.__name__}('
#                f'{self.x!r},{self.y!r})'
#                f'{self.SquarePoint!r},{self.SquareSize!r})')

    
                
