#firebase documentation: https://pypi.org/project/firebase/
#
# Military Phonetic Alphabet
# A : Allpha
# B : Bravo
# C : Charlie
# D : Delta
# E : Echo
# F : Fox
# G : Gorge
# H : Hypo
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

from os import system, name
import time
import speech_recognition as sr
from firebase import firebase

from colorama import init
from colorama import Fore, Back, Style
init()

from mobility import get_possible_loc
from mobility import check_pone_mobility_3
from mobility import check_pone_kill_and_mobile

valid_count = 0
fail_count = 0


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
clear()


# Initializing speech recognition engine
print("Listing avilable mikes........")
r = sr.Recognizer()
m = sr.Microphone()
for index,name in enumerate(sr.Microphone.list_microphone_names()):
	print("Microhone with name\"{1}\" found index = {0}".format(index,name))

print("Adjusting to the background noise........")
print(Fore.YELLOW+"Cpt. Price >> Count from 1-10 !!")
time.sleep(1)
print(Fore.YELLOW+"Cpt. Price >> Start Now")
print(Style.RESET_ALL)
time.sleep(3)

with m as source: r.adjust_for_ambient_noise(source)
print("Setting minimum energy threshold to {}".format(r.energy_threshold))

#initilizing firebase
print("Initializing Data base........")
firebase = firebase.FirebaseApplication('https://chess-pieces-d8869-default-rtdb.firebaseio.com/', None)

def sideSelection(text):
	textsplited = split(text)[0]
	if ((textsplited == "W") or (textsplited == 'w')):
		return 'white' 
	elif ((textsplited == "B") or (textsplited == 'b')):
		return 'black'
	else:
		return ' '

white_string = 'WR1:A1,WN1:B1,WB1:C1,WQ :D1,WK :E1,WB2:F1,WN2:G1,WR2:H1,WP1:A2,WP2:B2,WP3:C2,WP4:D2,WP5:E2,WP6:F2,WP7:G2,WP8:H2'
black_string = 'BR1:A8,BN1:B8,BB1:C8,BQ :D8,BK :E8,BB2:F8,BN2:G8,BR2:H8,BP1:A7,BP2:B7,BP3:C7,BP4:D7,BP5:E7,BP6:F7,BP7:G7,BP8:H7'

white_string_list = white_string.split(",")
black_string_list = black_string.split(",")

columns = ['A','B','C','D','E','F','G','H']

dead_white = []
dead_black = []

def initilizing():

	clear()

	global sessionID 
	global side
	sessionID = 1234
	side = ' '

	print(Fore.GREEN+"*************************************************************")
	print("*                                                           *")
	print("*                                                           *")
	print("*                "+Fore.YELLOW+"Play Chess with Your Voice"+Fore.GREEN+"                 *")
	print("*                     Game Room:"+str(sessionID)+"                        *")
	print("*                          V 1.0                            *")
	print("*                                                           *")
	print("*                                                           *")
	print("*************************************************************")
	print(Style.RESET_ALL)
	
	print("Cpt. Price >> Select the side: [White/Black] : ")

	time.sleep(1)

	while((side != 'white') and (side != 'black')):
		side = sideSelection(listining())

	setboard(sessionID,side)

	print(Fore.GREEN+"*************************************************************")
	print("*                                                           *")
	print("*                 The War is about to Begin !!              *")
	print("*                You are the warrior in "+Fore.YELLOW+side+Fore.GREEN+"               *")
	print("*                                                           *")
	print("*************************************************************")
	print("\n")
	print(Fore.RED+ "Cpt. Price >> Leave your Radio Message in following format")
	print("\n")
	print("Game Controls")
	print("Queen  Alpha 1   > to move queen to  A1")
	print("King   Bravo 2   > to move king to   B2")
	print("Knight Cheeta 3 > to move knight to C1")
	print("Bishop Delta 4   > to move bishop to D1")
	print("Ruk    Echo 5    > to move ruk to    E5")
	print("Pone   Fox 6     > to move pone to   F6")
	print("Queen  Gorge 7   > to move queen to  G7")
	print("King   Hypo 1    > to move king to   H8")

	time.sleep(3)
	print("\n")
	
	# for i in range(9,0,-1):
	# 	print("Game begins in: ", i, end = "\r")
	# 	time.sleep(1)

	print(Style.RESET_ALL)

	if side=='white':
		print("First Move is Yours")

	else:
		print("Wait for the White move")

	firebase.put('/'+str(sessionID)+'/','Current','white')

def setboard(ID,side):
	global white_string,black_string
	print(Fore.BLUE+"Army is onboarding ...............")
	try:
		firebase.put('/'+str(ID)+'/white','0',white_string)
		firebase.put('/'+str(ID)+'/black','0',black_string)
	except ConnectionError(e):
		print(Fore.RED+"Intenet is not connected. Please connect to the intenet")

	print(Style.RESET_ALL)
	time.sleep(1)

def listining():
	print("Listening.. ")
	with m as source: audio = r.listen(source,phrase_time_limit= 6)
	print("understanding...")

	try: 
		value = r.recognize_google(audio)
		valueString = ""

		if str is bytes:
			valueString = value.encode("utf-8")
			print(valueString)

		else:
			valueString = value
			print(value)
		return valueString

	except sr.UnknownValueError:
		print("Missed")
		return "Nope"

	except sr.RequestError as e:
		print("Could not make the request service; {0}".format(e))
		return "Nope"

def listining_at_hold():
	#print("Listening.. ")
	with m as source: audio = r.listen(source,phrase_time_limit= 6)
	#print("understanding...")

	try: 
		value = r.recognize_google(audio)
		valueString = ""

		if str is bytes:
			valueString = value.encode("utf-8")
			print(valueString)

		else:
			valueString = value
			print(value)
		return valueString

	except sr.UnknownValueError:
		#print("Missed")
		return "Nope"

	except sr.RequestError as e:
		#print("Could not make the request service; {0}".format(e))
		return "Nope"

def valid_command_ckeck_v1(command):
	global fail_count

	words = []
	words = command.split(" ")
	if len(words) >= 4:
		return True
	else: 
		print("repeat!!")
		fail_count += 1
		return False

def valid_command_ckeck_v2(command):
	global fail_count

	words = []
	words = command.split(" ")
	if len(words) >= 3:
		return True
	else: 
		print("repeat!!")
		fail_count += 1
		return False

def get_number(word):
	if((word == '1') or (word == 'One') or (word == 'one')):
		return 1
	elif ((word == '2') or (word == 'Two') or (word == 'two') or (split(word)[0] == 't') or (split(word)[0] == 'T')):
		return 2
	elif ((word == '3') or (word == 'Three') or (word == 'tree') or (word == 'free') or (word == 'three')):
		return 3
	elif ((word == '4') or (word == 'Four') or (word == 'four') or (word == 'Ho')):
		return 4
	elif ((word == '5') or (word == 'Five') or (word == 'five')):
		return 5
	elif ((word == '6') or (word == 'Six') or (word == 'six')):
		return 6
	elif ((word == '7') or (word == 'Seven') or (word == 'seven')):
		return 7
	elif ((word == '8') or (word == 'Eight') or (word == 'eight')):
		return 8
	else:
		return 0

def get_number_one_or_two(word):
	if((word == '1') or (word == 'One') or (word == 'one')):
		return 1
	elif ((word == '2') or (word == 'Two') or (word == 'two') or (split(word)[0] == 't') or (split(word)[0] == 'T')):
		return 2
	else:
		return 0

def command_comprehend_v1(command):
	global valid_count
	global fail_count


	words = []
	words = command.split(" ")
	print(words)
	source = " "
	destination = " " 
	source_int = 0
	destination_int = 0

	if ((split(words[0])[0]) == "A" or (split(words[0])[0]) == "a"):
		source = "A"
	elif ((split(words[0])[0]) == "B" or (split(words[0])[0]) == "b"):
		source = "B"
	elif ((split(words[0])[0]) == "C" or (split(words[0])[0]) == "c"):
		source = "C"
	elif ((split(words[0])[0]) == "D" or (split(words[0])[0]) == "d"):
		source = "D"
	elif ((split(words[0])[0]) == "E" or (split(words[0])[0]) == "e"):
		source = "E"
	elif ((split(words[0])[0]) == "F" or (split(words[0])[0]) == "f"):
		source = "F"
	elif ((split(words[0])[0]) == "G" or (split(words[0])[0]) == "g"):
		source = "G"
	 


	if ((split(words[2])[0]) == "A" or (split(words[2])[0]) == "a"):
		destination = "A"
	elif ((split(words[2])[0]) == "B" or (split(words[2])[0]) == "b"):
		destination = "B"
	elif ((split(words[2])[0]) == "C" or (split(words[2])[0]) == "c"):
		destination  = "C"
	elif ((split(words[2])[0]) == "D" or (split(words[2])[0]) == "d"):
		destination  = "D"
	elif ((split(words[2])[0]) == "E" or (split(words[2])[0]) == "e"):
		destination  = "E"
	elif ((split(words[2])[0]) == "F" or (split(words[2])[0]) == "f"):
		destination  = "F"
	elif ((split(words[2])[0]) == "G" or (split(words[2])[0]) == "g"):
		destination    = "G"

	try:
		source_int = get_number(words[1])
	except ValueError:
		source_int = 0

	try:
		destination_int = get_number(words[3])
	except ValueError:
		destination_int = 0


	if ((source != " ") and (destination != " ") and ((source_int <= 8) and (source_int > 0)) and ((destination_int <= 8) and (destination_int > 0))):
		print(Back.GREEN + "Cpt. Price >> Valid Command:",source,source_int,destination,destination_int)
		valid_count += 1
		return [source,source_int,destination,destination_int]
	else:
		print("Cpt. Price >> Repeat the Command!!")
		fail_count += 1
	
def command_comprehend_v2(command):
	global valid_count
	global fail_count

	words = []
	words = command.split(" ")
	#print(words)


	source = " "
	number = "Nope"
	intnumber = 0
	destination = " "
	destination_int = 0

	if (((split(words[0])[0]) == 'K') or ((split(words[0])[0]) == 'k') or ((split(words[0])[0]) == 'King')):
		source = "K "
		#print("King")
	elif (((split(words[0])[0]) == 'Q') or ((split(words[0])[0]) == 'q') or ((split(words[0])[0]) == 'Qeen')):
		source = "Q "
	elif (((split(words[0])[0]) == 'B') or ((split(words[0])[0]) == 'b') or ((split(words[0])[0]) == 'Bishop')):
		print(Fore.YELLOW+"Which Bishop? one or two?")
		while(intnumber == 0):
			intnumber = get_number_one_or_two(listining())

		source = 'B'+ str(intnumber)
		print("Understood, Bishop"+str(intnumber)+" ie. "+source)
		print(Style.RESET_ALL)

	elif (((split(words[0])[0]) == 'N') or ((split(words[0])[0]) == 'n') or ((split(words[0])[0]) == 'night')):
		print(Fore.YELLOW+"Which Knight? one or two?")
		while(intnumber == 0):
			intnumber = get_number_one_or_two(listining())

		source = 'N'+ str(intnumber)
		print("Understood, Knight"+str(intnumber)+" ie. "+source)
		print(Style.RESET_ALL)

	elif (((split(words[0])[0]) == 'R') or ((split(words[0])[0]) == 'r') or ((split(words[0])[0]) == 'Ruk')):
		print(Fore.YELLOW+"Which Ruk? one or two?")
		while(intnumber == 0):
			intnumber = get_number_one_or_two(listining())

		source = 'R'+ str(intnumber)
		print("Understood, Ruk"+str(intnumber)+" ie. "+source)
		print(Style.RESET_ALL)

	elif (((split(words[0])[0]) == 'P') or ((split(words[0])[0]) == 'p') or ((split(words[0])[0]) == 'pone')):
		print(Fore.YELLOW+"Which Pone? one, two, three, four, five, six, seven, eight?")
		while(intnumber == 0):
			intnumber = get_number(listining())

		source = 'P'+ str(intnumber)
		print("Understood, Pone"+str(intnumber)+" ie. "+source)
		print(Style.RESET_ALL)

	if ((split(words[1])[0]) == "A" or (split(words[1])[0]) == "a"):
		destination = "A"
		#print("A")
	elif ((split(words[1])[0]) == "B" or (split(words[1])[0]) == "b"):
		destination= "B"
	elif ((split(words[1])[0]) == "C" or (split(words[1])[0]) == "c"):
		destination= "C"
	elif ((split(words[1])[0]) == "D" or (split(words[1])[0]) == "d"):
		destination= "D"
	elif ((split(words[1])[0]) == "E" or (split(words[1])[0]) == "e"):
		destination= "E"
	elif ((split(words[1])[0]) == "F" or (split(words[1])[0]) == "f"):
		destination= "F"
	elif ((split(words[1])[0]) == "G" or (split(words[1])[0]) == "g"):
		destination= "G"
	elif ((split(words[1])[0]) == "H" or (split(words[1])[0]) == "h"):
		destination= "H"

	try:
		destination_int = get_number(words[2])
		#print(destination_int)
	except ValueError:
		destination_int = 0



	if ((source != " ") and (destination != " ")):
		print(Fore.GREEN + "Valid Command: "+Style.RESET_ALL,source,destination,destination_int)
		valid_count += 1
		return [source,destination,destination_int]
	else:
		print(Fore.RED+ "Try Again")
		print(Style.RESET_ALL)
		fail_count += 1

def concatanate(list):
	string=''
	for item in range(0,len(list)-1):
		string = string+list[item] +","

	string = string + list[len(list)-1] # adding last component without priting addition comma at the end

	return string

def update(new,pos,side):

	global white_string_list, black_string_list, sessionID 
	#String list legend
	# 0: RUK1       8:P1 
	# 1: KNIGHT1    9:P2 
	# 2: BISHOP1    10:P3
	# 3: Queen      11:P4
	# 4: King       12:P5
	# 5: BISHOP2    13:P6
	# 6: KNIGHT2    14:P7
	# 7: RUK2       15:P8
	if side == 'W':
		white_string_list[pos] = new
		#print(concatanate(white_string_list))
		firebase.put('/'+str(sessionID)+'/'+'white','0',concatanate(white_string_list))


	elif side == 'B':
		black_string_list[pos] = new
		#print(concatanate(black_string_list))
		firebase.put('/'+str(sessionID)+'/'+'black','0',concatanate(black_string_list))

def move(command,side):
	#String list legend
	# 0: RUK1       8:P1 
	# 1: KNIGHT1    9:P2 
	# 2: BISHOP1    10:P3
	# 3: Queen      11:P4
	# 4: King       12:P5
	# 5: BISHOP2    13:P6
	# 6: KNIGHT2    14:P7
	# 7: RUK2       15:P8 

	if side == 'white':
		side = "W"
	elif side == 'black':
		side = "B"

	if command[0] == "R1":
		new_pos = side+'R1'+':'+command[1]+str(command[2])
		update(new_pos,0,side)
	elif command[0] == "N1":
		new_pos = side+'N1'+':'+command[1]+str(command[2])
		update(new_pos,1,side)
	elif command[0] == "B1":
		new_pos = side+'B1'+':'+command[1]+str(command[2])
		update(new_pos,2,side)
	elif command[0] == "Q ":
		new_pos = side+'Q '+':'+command[1]+str(command[2])
		update(new_pos,3,side)
	elif command[0] == "K ":
		new_pos = side+'K '+':'+command[1]+str(command[2])
		update(new_pos,4,side)
	elif command[0] == "B2":
		new_pos = side+'B2'+':'+command[1]+str(command[2])
		update(new_pos,5,side)
	elif command[0] == "N2":
		new_pos = side+'N2'+':'+command[1]+str(command[2])
		update(new_pos,6,side)
	elif command[0] == "R2":
		new_pos = side+'R2'+':'+command[1]+str(command[2])
		update(new_pos,7,side)
	elif command[0] == "P1":
		new_pos = side+'P1'+':'+command[1]+str(command[2])
		update(new_pos,8,side)
	elif command[0] == "P2":
		new_pos = side+'P2'+':'+command[1]+str(command[2])
		update(new_pos,9,side)
	elif command[0] == "P3":
		new_pos = side+'P3'+':'+command[1]+str(command[2])
		update(new_pos,10,side)
	elif command[0] == "P4":
		new_pos = side+'P4'+':'+command[1]+str(command[2])
		update(new_pos,11,side)
	elif command[0] == "P5":
		new_pos = side+'P5'+':'+command[1]+str(command[2])
		update(new_pos,12,side)
	elif command[0] == "P6":
		new_pos = side+'P6'+':'+command[1]+str(command[2])
		update(new_pos,13,side)
	elif command[0] == "P7":
		new_pos = side+'P7'+':'+command[1]+str(command[2])
		update(new_pos,14,side)
	elif command[0] == "P8":
		new_pos = side+'P8'+':'+command[1]+str(command[2])
		update(new_pos,15,side)

def delete(item,loc_set):
	print(loc_set)
	temp_p = item.split(":")[0]
	for i,ite in enumerate(loc_set):
		if ite.split(":")[0] == temp_p:
			pos = i
			print("Pos: ",pos)
			side = split(temp_p)[0]

	update(temp_p+":. ",pos,side)

def split(word):
    return [char for char in word]

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_loc_firebase(gameno,side):
	global chess_prices,black_loc,white_loc

	# black_loc = [] # Order : P1,P2,P3,P4,P5,P6,P7,P8,B1,B2,N1,N2,R1,R2,K,Q
	# white_loc = [] # Order : P1,P2,P3,P4,P5,P6,P7,P8,B1,B2,N1,N2,R1,R2,K,Q

	print(Fore.BLUE+"Getting "+side+" Army Location",end= ". . .")
	if (side == 'white'):
		try:
			loc=firebase.get('/'+str(gameno)+'/'+side+'/', '0').split(",")
		except ConnectionError(e):
			print(Fore.RED+"Intenet is not connected. Please connect to the intenet")

	elif(side == 'black'):
		try:
			loc=firebase.get('/'+str(gameno)+'/'+side+'/', '0').split(",")
		except ConnectionError(e):
			print(Fore.RED+"Intenet is not connected. Please connect to the intenet")

	print(Style.RESET_ALL)
	return loc

def board(white,black):
	print(" ")
	print("__________________________________________")
	print(" ")
	for row in range(8,0,-1):
		q = [" . "," . "," . "," . "," . "," . "," . "," . "]
		for count,column in enumerate(columns):
			for item in white:
				cell = column + str(row)
				if item.split(":")[1] == cell:
					q[count] = item.split(":")[0]
				#elif item.split(":")[1] == ". ":
				#	q[count] = " . "


			for item in black:
				cell = column + str(row)
				if item.split(":")[1] == cell:
					q[count] = item.split(":")[0]
				#elif item.split(":")[1] == ". ":
				#	q[count] = " . "

		print(Fore.YELLOW +str(row),end=' ')
		print(Style.RESET_ALL,end=' ')
		print("%s  %s  %s  %s  %s  %s  %s  %s  "%(q[0],q[1],q[2],q[3],q[4],q[5],q[6],q[7]))

	print(Fore.YELLOW +"    %s    %s    %s    %s    %s    %s    %s    %s  "%("A","B","C","D","E","F","G","H"))
	print(Style.RESET_ALL)
	print("__________________________________________")
	print(" ")

def mobility_check(commd_received,player_side,white,black):
	try:
		given_command = commd_received[1]+ str(commd_received[2])
	except:
		return False
	if player_side == 'white':
		royal_member = "W" + commd_received[0]
		print("Cpt. Price >> Mobility check for white move.. ", end = " ")
		if given_command in get_possible_loc(royal_member,white,black):
			print("Pass")
			return True
		else:
			print("Fail")
			return False
	elif player_side == 'black':
		royal_member = "B" + commd_received[0]
		print("Cpt. Price >> Mobility check for black move..", end = " ")
		if given_command in get_possible_loc(royal_member,white,black):
			print("Pass")
			return True
		else:
			print("Fail")
			return False

def occupancy_check(commd_received,player_side,white,black):
	#EX: Command Received = [P1 A 6]
	given_command = commd_received[1]+ str(commd_received[2])
	player = commd_received[0]
	temp_a = []
	temp_b = []
	pones_w = ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8']
	pones_b = ['BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8']

	global dead_black,dead_white



	if player_side == 'white':
		print("Cpt. Price >> Occupancy check for white move.. ", end = " ")
		
		for item in white:
			temp_a.append(item.split(":")[1])

		#Check for white peice
		if given_command in temp_a:
			print("There is a white peice")
			print("Fail")
			return False
		else:
			#Check for black peic3 # Removing the king from dying
			for item in black:
				if item.split(":")[0] in pones_b:
					check_no = check_pone_mobility_3(commd_received,'W',item.split(":")[1],white,black)
					#print("Check No:",check_no)
					if check_no == 1:
						print("Fail")
						return False
					elif check_no == 2:
						dead_black.append(item.split(":")[0])
						delete(item,black)
						print("Pass")
						return True

				if item.split(":")[0] != 'BK ':
					#print(item,given_command)
					if (item.split(":")[1] == given_command): 
						#print(item.split(":")[0] + " Dead, He was a nice worrier") # Dead
						dead_black.append(item.split(":")[0])
						delete(item,black)
						print("Pass")
						return True
			print("Pass")
			return True
		
	elif player_side == 'black':
		print("Cpt. Price >> Occupancy check for black move.. ", end = " ")
		
		for item in black:
			temp_b.append(item.split(":")[1])

		#Check for black peice
		if given_command in temp_b:
			print("Cpt. Price >> There is a black peice, Speak a command again")
			print("Fail")
			return False
		else:
			#Check for white peice# Removing the king from dying
			for item in white:
				if item.split(":")[0] in pones_w:
					check_no = check_pone_mobility_3(commd_received,'B',item.split(":")[1],white,black)
					#print("Check No:",check_no)
					if check_no == 1:
						print("Fail")
						return False
					elif check_no == 2:
						dead_white.append(item.split(":")[0])
						delete(item,black)
						print("Pass")
						return True

				if item.split(":")[0] != 'WK ':
					if item.split(":")[1] == given_command: 
						#print(item.split(":")[0] + " Dead, He was a nice worrier") # Dead
						dead_white.append(item.split(":")[0])
						delete(item,white)
						print("Pass")
						return True
			print("Pass")
			return True
	else:
		print("Error in occupancy")
		


initilizing()

white_loc = get_loc_firebase(sessionID,'white')
black_loc =get_loc_firebase(sessionID,'black')
board(white_loc,black_loc)

hold = False


while True:
	try: 
		command = []

		side = firebase.get('/'+str(sessionID)+'/', 'Current')

		if side == 'white':
			print(Fore.CYAN+"Cpt. Price >> Playing Side : White")
		elif side == 'black':
			print(Fore.MAGENTA+"Cpt. Price >> Playing Side : Black")
		
		print(Style.RESET_ALL)

		command_string = listining()

		if (command_string == 'Stop') or (command_string == 'stop'):
			print(Fore.YELLOW+"Game Pause!, Yeh better think before move .."+Style.RESET_ALL)
			hold = True
		elif (command_string == 'Start') or (command_string == 'start'):
			hold = False

		while(hold):
			command_string = listining_at_hold()
			if (command_string == 'Start') or (command_string == 'start'):
				hold = False



		try:
		
			if(valid_command_ckeck_v2(command_string)):

				command= command_comprehend_v2(command_string)

				if mobility_check(command,side,white_loc,black_loc):
					if occupancy_check(command,side,white_loc,black_loc):
						print(Fore.GREEN+"Cpt. Price >> GO Go GO")
						print(Style.RESET_ALL)
						move(command,side)
						if side == 'white':
							firebase.put('/'+str(sessionID)+'/','Current','black')
						else:
							firebase.put('/'+str(sessionID)+'/','Current','white')
					else :
						print(Fore.RED+"Cpt. Price >> Cant Move"+Style.RESET_ALL)
						
				else:
					print(Fore.RED+"Cpt. Price >> Cant Mobile"+Style.RESET_ALL)
				
		except:
			pass

			#print("command:",command)
			#move(command,side)

			
		white_loc = get_loc_firebase(sessionID,'white')
		black_loc =get_loc_firebase(sessionID,'black')
		#print(white_loc)
		#print(black_loc)

		board(white_loc,black_loc)
		print(Fore.YELLOW+'Dead List')
		print(Fore.MAGENTA+"White :",dead_black)
		print(Fore.CYAN + "Black :",dead_white)
		print(Style.RESET_ALL)
		#except:
		#	pass



		time.sleep(3)
	
	except KeyboardInterrupt:
		break
	#print("Command Pronounsation Success Rate: ", str(valid_count*100/(valid_count+fail_count)))

# command_string = "alpha 1 beta 6"

# if(valid_command_ckeck(command_string)):
# 	command= command_comprehend(command_string)






#data2 = firebase.get('/iot_control/', '')
#print(data2["front_gate"])


# firebase = firebase.FirebaseApplication('Database URL', None)
# firebase.put('/python-example-f6d0b/Students/-LjLUhaWGuxNd5gOEmse','Name','Bob')
# print('Record Updated')
