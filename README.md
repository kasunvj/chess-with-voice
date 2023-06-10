# chess-with-voice

Google Drive link for vertual env <br> 
https://drive.google.com/file/d/1nyZ2gkFwxF_QXZmSNChuiD9GQvisNd6Q/view?usp=sharing
<br>

How to play <br> 
1.Direct CMD prompt where the 'venv_chessplay' folder is located <br> 
2.Activate Vertual env: <br> 
	$venv_chessplay\Scripts\activate.bat<br> 
3.Go in to 'game_files'<br> 
	$cd game_files<br> 
4.Run the script: <br> 
	$python 17072021.py<br> 
<br>


![ezgif com-crop](https://github.com/kasunvj/chess-with-voice/assets/20115338/b4493da0-9ad8-4525-9b6a-b548a7096cf8)

Developer Note
JMKV Jayalath

-------------------------------------------------------
Features Implemented and Tested
1.	Voice Recognition –using google speech recognition
2.	Firebase RT Database implementation 
3.	Two players can play simultaneously from different location in separate consoles.
4.	Two players can play simultaneously from same location using same console
5.	Identify user commands 
6.	Selection of sides using voice 
7.	In game pause during the game
8.	Visual location of the chess pieces on console
9.	Colorful console interface 
10.	Rule check engine for each chess piece – for mobility to identified commands
11.	Rule check engine for each chess piece – for occupancy to identified commands
12.	Rule check engine for each chess piece – for killing opponent
13.	Algorithm development for each single piece for moving along the board.   

Features Not Implemented
1.	No voice separation of two players – will not identify player by voice
2.	Not locking the piece by moving during Check scenario. 
3.	Not fully bug tested for all the possible scenarios during the game
