# Pathfinding
with decomposition of the map into squares

Goal: finding short, not nessesary shortest, ways in a map of squares. Lot's of them, fast.

Problem: precompiling all ways would be fastest, but the running time increases with n^4 for a nxn map

Insigt: an empty square would be trivial to navigate (just go in the direction of the goal), but is the worst case if all ways are 
        precompiled in a naive way

Idea: Decompose the map into squares. Approximate the part of a short-way inside a square with its side length. Find a good orrder of ways simmilar to A*. Easyly navigate inside a Square. 
