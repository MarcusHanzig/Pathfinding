

import battlecode as bc
import random
import sys
import traceback
import time

import os

import Global



def fuzzygoto(uid,mlocation,dest):
    toward=umlocation.direction_to(dest)
    if toward==bc.Direction.Center:
        toward=random.choice(Global.directions)
    for tilt in Global.tryRotate:
        d=rotate(toward,tilt)
        if gc.can_move(uid,d):
            gc.move_robot(uid,d)
            break

def fuzzygoto_small(uid,mlocation,dest):
    toward=mlocation.direction_to(dest)
    if toward==bc.Direction.Center:
        toward=random.choice(Global.directions)
    for tilt in Global.tryRotate_small:
        d=rotate(toward,tilt)
        if gc.can_move(uid,d):
            gc.move_robot(uid,d)
            break

def fuzzygoto_direction(uid,toward):
    #toward=unit.location.map_location().direction_to(dest)
    for tilt in Global.tryRotate:
        d=rotate(toward,tilt)
        if gc.can_move(uid,d):
            gc.move_robot(uid,d)
            break

def fuzzygoorthogonal(uid,mlocation,dest):
    toward=dest.direction_to(mlocation)
    if toward==bc.Direction.Center:
        toward=random.choice(Global.directions)
    for tilt in tryRotate_ortho:
        d=rotate(toward,tilt)
        if gc.can_move(uid,d):
            gc.move_robot(uid,d)
            break

def fuzzygoaway(uid,mlocation,dest):
    toward=dest.direction_to(mlocation)
    for tilt in Global.tryRotate:
        d=rotate(toward,tilt)
        if gc.can_move(uid,d):
            gc.move_robot(uid,d)
            break

def touch_point(x,y,n,x2,y2,n2):
    x_new=int((x+1.0*n/2)+int((x2-x+(n2-n)/2)*1.0*n2/(n+n2)))
    y_new=int((y+1.0*n/2)+int((y2-y+(n2-n)/2)*1.0*n2/(n+n2)))
    #y_new=int((y+1.0*n/2)+int((y2-y+(n2-n)/2)*1.0*n2/(n+n2))
    return([x_new,y_new])

def is_in_square(new_pos,x_edge,y_edge,n):
    x=new_pos.x
    y=new_pos.y
    if (x>=x_edge) and (y>=y_edge) and (x<x_edge+n) and (y<y_edge+n):
        return(True)
    else:
        return(False)




def move(uid,mlocation,target):
    Notmoved=True
    target2=target
    try:
        next_targ=next_target[uid]
    except :
        next_targ=mlocation
        
        
    x2,y2=target.x,target.y
    x,y=mlocation.x,mlocation.y
    xn,yn=next_targ.xn,next_targ.yn
    if Field_square[x][y]==Field_square[xn][yn]:
        if Field_square[x][y]!=Field_square[x2][y2]:
            ############MISSING
            for point in Edges_circle[Field_square[x][y]]:
                if Matrix_way[(x,y,x2,y2)]==Matrix_way[(x,y,x,y)]+Matrix_way[(point[0],point[1],x2,y2)]:
                    


                    break
        else:
            fuzzygoto_small(uid,mlocation,next_targ)
    else:
        fuzzygoto_small(uid,mlocation,next_targ)




   # mlocation=unit.location.map_location()
    if Field_square[x2][y2]!=0 and Matrix_way(x,y,x2,y2)<1000:
        if Field_square[x][y]!=Field_square[x2][y2]:
            [x_edge,y_edge,n,Edges_index]=Global.Field_square[x][y]
            [x_edge2,y_edge2,n2,Edges_index2]=Global.Field_square[x2][y2]
            mat=Matrix_way2[Edges_index][Edges_index2]
            Neighbor_square=circle3(x_edge,y_edge,n)
            if len(Neighbor_square)==0:
                fuzzygoto(unit,target2)
                return()
            point_best=Neighbor_square[0]
            p_b=point_best[3]
            way_best= Matrix_way2[p_b][Edges_index2]#+Matrix_way2[p_b][p_b]
           
            for point in Neighbor_square:
                p=point[3]
                if Matrix_way2[p][Edges_index2]<way_best: #+Matrix_way2[p][p]
                    point_best=point
                    way_best=Matrix_way2[p][Edges_index2]#+Matrix_way2[p][p]
            x_nextsquare=point_best[0]
            y_nextsquare=point_best[1]
            n_next_square=point_best[2]
            target2=bc.MapLocation(this_planet,x_nextsquare+int(n_next_square/2),y_nextsquare+int(n_next_square/2))


            toward=mlocation.direction_to(target2)
            if toward==bc.Direction.Center:
                toward=random.choice(directions)
            for tilt in tryRotate:
                d=rotate(toward,tilt)
                if gc.can_move(unit.id,d):
                    new_pos=mlocation.add(d)
                    if is_in_square(new_pos,x_edge,y_edge,n) or is_in_square(new_pos,x_nextsquare,y_nextsquare,n_next_square) :
                        gc.move_robot(unit.id,d)
                        Notmoved=False
                        break
            if Notmoved:
                fuzzygoto_small(unit,target2)
        else:
            fuzzygoto(unit,target2)
    else:
         fuzzygoto(unit,target2)    
    return()






