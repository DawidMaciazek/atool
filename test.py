#!/usr/bin/python
import atool

t=atool.ReadTraj("test.lammpstrj")

frame = t.readFrame()

print frame[0]['format']
print frame[3][20:30]
