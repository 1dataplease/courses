# calculate distance b/w points p - q
# python list of coordinantes
    # [p[0], p[1]],  [q[0], q[1]]

#pythag thm
# math
# dist(p,q)^2 == (p[0] - q[0])^2 + (p[1] - q[1])^2

import math
def dist(p,q):
    return math.sqrt( (p[0] - q[0])**2 + (p[1] - q[1])**2 )

p = [0,0]
q = [3,3]
    
print dist([0,0], [3,3])


## vector as a difference of 2 points
##math v = p-q
v[0] = p[0] - q[0]
v[1] = p[1] - q[1]

## move point using a vector
# #math: p = q + v
p[0] = q[0] + v[0]
p[1] = q[1] + v[1]

## update for motion
## math: pt at pos p w / velocity v
## p = p + a*v
p[0] = p[0] + a * v[0]
p[1] = p[1] + a * v[1]

## collision of wall vs ball w/ center p and raduis r
## left wall
p[0] <= 0

## right wall
p[0] >= (width-1)-r

## collision of wall vs. pt p
## left wall
p[0] <= 0

## right wall
p[0] >= width - 1

## update velocity vector v
## left wall : compute reflected velocity vector
v[0] = -v[0]
v[1] = v[1]