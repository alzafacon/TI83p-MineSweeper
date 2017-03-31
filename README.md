# TI83p-MineSweeper
Clone of windows Mine Sweeper. Efficient auto-clear functionality inspired by Chris Hamilton. His project is also included in this repo.

My first attempt, in BreadthFirstSearch folder, is around 8 times slower than Hamilton's.

All credit for the auto-reveal goes to Chris Hamilton (chrisrham@hotmail.com this email does not work). In fact I copy-pasted his code into [my solution](/Main) and then made modifications to work with my [SWEEP](/Main/SWEEP.txt) (that slowed it down).

## Other Clones
Several TI graphing calculator mine sweepers can be found [here](http://www.ticalc.org/pub/83/basic/games/puzzle/minesweeper/).
If you would like to download Chris Hamilton's version, it is named [msweep.zip](http://www.ticalc.org/pub/83/basic/games/puzzle/minesweeper/msweep.zip). I have also included the program files in this repo.

## Goal: Structured Programming
My principal goal in this project is to write a structured version (no Goto statements) of Hamilton's program that will make understanding the code much easier. As described in Issue#1, I know it is possible but this has proven more challenging than I expected ~~(I have not succeeded in writing the structured version thus far)~~(A working version of Hamilton's structured program is [here](/Testing/Hamilton_Testing)). The best I was able to do in terms of elucidating the operation of Hamilton's auto-reveal is a Finite State Machine (FSM) to describe the principles that the program uses (but not directly the program itself).

### Breadth-First Search v. ZMSO
I wrote a breadth-first search algorithm to perform auto-reveal. unfortunately this was very slow since each visited cell had to make on average 8 checks for its neighbors. Hamilton on the other hand only makes approximately at worst 2\*((board width)/4)+2 on each _row_ being processed for auto-reveal. (That figure was kinda pulled out of a hat). Basically... +2 because at the beginning of each row 2 checks (i.e. above and below) are made to determine if the row above or below need to be queued for later processing. As a row is being processed if a non-zero tile is encountered then a single check (the wort-case formula I give does not account for this check) is made to determine if there is still a bordering zero above or below, row processing is continued if yes other wise we are done. If there is a zero _above or below_ we continue processing this same row, if a zero tile is encountered again on the row then we have to make the 2 more checks (i.e. above and below). The alternating from non-zero to zero is only possible at most (board width)/4 times because said alternation can only happen when there are **3 consecutive non-zero tiles** (_3 is the minumum number of consecutive non-zero tiles_) followed by a zero (3 non-zero + 1 zero = 4 tiles) hence divison by 4. The zero tile requieres 2 checks to be performed hence the multiplication by 2. 

For any given tile no more than 2 checks are ever made, and almost all of the time 0 checks are made. This explains why Hamilton's auto-reveal is _so_ much faster than breadth-first search.

### Row-Oriented Auto-Reveal (ROAR)
Ultimately I hope to make a version of ZMSO that is structured and works with my clone of MineSweeper and I will name it ROAR! The main features that distinguish my clone from Hamilton are:
1. Auto-Detection of game completion (this slows down HAMAUTO slightly)
2. Flexible board size (but can be crashed easily)
3. The cursor wraps!
4. More intuitive buttons (Flag with ^ and reveal with 'Enter')

Hamilton's version definitely has great features:
1. Cool Animations
2. High scores
3. Directions
4. Superfast Auto-Reveal
5. Best Times (This can be done much better for TI-84 with Timer)

### Development Enviorment
I am using TokenIDE for editing the programs. I don't know where I got it, but it should be easy to Google. I recommend saving two versions of your programs. One in .txt and the other should be .8xp which you should let TokenIDE compile for you. Never open an .8xp in TokenIDE! Although it works, you will lose all comments and formatting that you have saved in your .txt file. (Compiled versions of the source were deliberatly not ingnored in case you have no way of compiling.)

I find it useful to have an emulator to test the programs. I use WabbitEmu (should also be easy to Google). You will need to get a hold of a ROM. To my understanding this is basically a copy of the operating system for the calculator. This must be extracted from a physical calulator. It is **illegal** to distibute ROMs. Alternataively, you could just use TI-Connect and test the programs on a physical calulator.

In summary, to get programming you will need:
1. TokenIDE
2. Calculator (preferably TI-83+)
  -An emulator (for example WabbitEmu) and a ROM (for TI-83+ of course)
  -or a physical calculator

### So what is actually working?
Use SWEEP.8XP (in the Main folder) and HAMAUTO.8XP (in the HamiltonAlg++ folder) for a working version. The folder 'Hamilton' contains the files from Hamilton's original project.
