// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//PHASE 1: The Listener 
(MAIN_LOOP)
@KBD
D=M
@BLACK
D;JGT
@WHITE
D;JEQ

//PHASE 2: Color and Pointer Setup
(BLACK)
D=-1
@color
M=D
@SCREEN
D=A
@pointer
M=D
@DRAW_LOOP
0;JMP

(WHITE)
D=0
@color
M=D
@SCREEN
D=A
@pointer
M=D
@DRAW_LOOP
0;JMP

//PHASE 3: The Drawing loop
//1.Boundary Check
(DRAW_LOOP)
@KBD 
D=A
@pointer
D=D-M
@MAIN_LOOP
D;JEQ

//2.Derefercing and Paint
@color
D=M
@pointer
A=M
M=D

//3.Increment Pointer
@pointer
M=M+1

//4.Repeat
@DRAW_LOOP
0;JMP