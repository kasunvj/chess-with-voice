import math
import numpy as np

columns = ['A','B','C','D','E','F','G','H']

def split(word):
    return [char for char in word]

def get_loc(member,white_locations,black_locations):
	temp_a = []
	temp_b = []
	side = split(member)[0]
	if side == "W":
		for item in white_locations:
			temp_a.append(item.split(":")[0])
			temp_b.append(item.split(":")[1])
		return temp_b[temp_a.index(member)]

	elif side == "B":
		for item in black_locations:
			temp_a.append(item.split(":")[0])
			temp_b.append(item.split(":")[1])
		return temp_b[temp_a.index(member)]

def encode_coordinate(loc_cartis):
	#7       B            8         B
	#6                    7
	#5                    6
	#4               >>   5
	#3                    4
	#2                    3
	#1       W            2         W
	#0 1 2 3 4 5 6 7 8    A B C D E F G H
	temp_d = ['A','B','C','D','E','F','G','H']
	first = temp_d[loc_cartis[0]]
	second = loc_cartis[1] + 1
	return first + str(second)

def decode_coordinate(loc_chess):
	#7       B            8        B
	#6                    7
	#5                    6
	#4               <<   5
	#3                    4
	#2                    3
	#1       W            2        W
	#0 1 2 3 4 5 6 7      A B C D E F G H

	temp_c = ['A','B','C','D','E','F','G','H'] 
	x = temp_c.index(split(loc_chess)[0])
	y = int(split(loc_chess)[1])-1
	return [x,y]

def bishop(current_cor):
	a,b = current_cor[0],current_cor[1]
	x_list = [0,1,2,3,4,5,6,7]
	y_list = [0,1,2,3,4,5,6,7]
	cor_pairs = []
	encoded_cor_pairs = []
	
	for x in x_list:
		y = x - a + b  # y= x translate to (a,b)  y = (x-a) + b
		if y in y_list:
			cor_pairs.append([x,y])

		y =-x + a + b # y= -x translate to (a,b)  y = -(x-a) + b
		if y in y_list:
			cor_pairs.append([x,y])
	
	#print(cor_pairs)

	for pair in cor_pairs:
		encoded_cor_pairs.append(encode_coordinate(pair))

	return encoded_cor_pairs


def ruk(current_cor):
	a,b = current_cor[0],current_cor[1] # x value is a, y value is b
	x_list = [0,1,2,3,4,5,6,7]
	y_list = [0,1,2,3,4,5,6,7]
	cor_pairs = []
	encoded_cor_pairs = []
	
	for x in x_list:
		y = b  # y= 0 translate to (a,b)
		if y in y_list:
			cor_pairs.append([x,y])
	for y in y_list:
		x = a# x = 0 translate to (a,b) 
		if y in y_list:
			cor_pairs.append([x,y])
	
	#print(cor_pairs)

	for pair in cor_pairs:
		encoded_cor_pairs.append(encode_coordinate(pair))

	return encoded_cor_pairs

def queen(current_cor):
	a,b = current_cor[0],current_cor[1]
	x_list = [0,1,2,3,4,5,6,7]
	y_list = [0,1,2,3,4,5,6,7]
	cor_pairs = []
	encoded_cor_pairs = []

	#Capabilities of Bishop
	for x in x_list:
		y = x - a + b  # y= x translate to (a,b)  y = (x-a) + b
		if y in y_list:
			cor_pairs.append([x,y])

		y =-x + a + b # y= -x translate to (a,b)  y = -(x-a) + b
		if y in y_list:
			cor_pairs.append([x,y])

	#Capabilities of Ruk
	for x in x_list:
		y = b  # y= 0 translate to (a,b)
		if y in y_list:
			cor_pairs.append([x,y])
	for y in y_list:
		x = a# x = 0 translate to (a,b) 
		if y in y_list:
			cor_pairs.append([x,y])

	#print(cor_pairs)

	for pair in cor_pairs:
		encoded_cor_pairs.append(encode_coordinate(pair))

	return encoded_cor_pairs

def knight(current_cor):
	a,b = current_cor[0],current_cor[1]
	x_list = [0,1,2,3,4,5,6,7]
	y_list = [0,1,2,3,4,5,6,7]
	cor_pairs = []
	encoded_cor_pairs = []
	
	for x in x_list:
		y = 2*(x - a) + b  # y= 2x translate to (a,b)   y = 2(x-a) + b
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 2.24): # square root of 5 is 2.24 
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])

		y = -2*(x - a) + b  # y= -2x translate to (a,b) y = -2(x-a) + b
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 2.24):# square root of 5 is 2.24 
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])


		y =0.5*(x - a) + b # y= 0.5x translate to (a,b) y = 0.5(x-a) + b
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 2.24):# square root of 5 is 2.24 
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])

		y =-0.5*(x - a) + b # y= -0.5x translate to (a,b) y =-0.5(x-a) + b
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 2.24):# square root of 5 is 2.24 
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])

	#print(cor_pairs)

	for pair in cor_pairs:
		encoded_cor_pairs.append(encode_coordinate(pair))

	return encoded_cor_pairs

def king(current_cor):
	a,b = current_cor[0],current_cor[1]
	x_list = [0,1,2,3,4,5,6,7]
	y_list = [0,1,2,3,4,5,6,7]
	cor_pairs = []
	encoded_cor_pairs = []

	#Capabilities of Bishop but limited on moving distance
	for x in x_list:
		y = x - a + b  # y= x translate to (a,b)  y = (x-a) + b
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 1.41):# square root of 2 is 1.41
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])

		y =-x + a + b # y= -x translate to (a,b)  y = -(x-a) + b
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 1.41):# square root of 2 is 1.41
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])

	#Capabilities of Ruk but limited on moving distance
	for x in x_list:
		y = b  # y= 0 translate to (a,b)
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 1):# distance is 1 in X direction
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])
	for y in y_list:
		x = a# x = 0 translate to (a,b) 
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 1):# distance is 1 in X direction
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])

	#print(cor_pairs)

	for pair in cor_pairs:
		encoded_cor_pairs.append(encode_coordinate(pair))

	return encoded_cor_pairs


def pone(current_cor,member):
	colour = split(member)[0]
	a,b = current_cor[0],current_cor[1]
	x_list = [1,2,3,4,5,6,7]
	y_list = [1,2,3,4,5,6,7]
	cor_pairs = []
	encoded_cor_pairs = []


	for y in y_list:
		if (colour == "W"):
			if(y > b):
				x = a# x = 0 translate to (a,b) 
				d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
				if ((d == 1) or (d == 2)):# distance is 1 or 2 in X direction
					if y in y_list:
						y = int(y)
						cor_pairs.append([x,y])

		elif (colour == "B"):
			if(y < b):
				x = a# x = 0 translate to (a,b) 
				d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
				if ((d == 1) or (d == 2)):# distance is 1 or 2 in X direction
					if y in y_list:
						y = int(y)
						cor_pairs.append([x,y])

	for y in y_list:
		if (colour == "W"):
			if (y > b):
				for x in x_list:
					y = x - a + b  # y= x translate to (a,b)  y = (x-a) + b
					if (y > b):
						d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
						if (d == 1.41):# square root of 2 is 1.41
							y = int(y)
							cor_pairs.append([x,y])

				for x in x_list:
					y = -x + a + b  # y= x translate to (a,b)  y = (x-a) + b
					d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
					if (y > b):
						if (d == 1.41):# square root of 2 is 1.41
							y = int(y)
							cor_pairs.append([x,y])


	for y in y_list:
		if (colour == "B"):
			if (y < b):
				for x in x_list:
					y = x - a + b  # y= x translate to (a,b)  y = (x-a) + b
					d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
					if (y < b):
						if (d == 1.41):# square root of 2 is 1.41
							y = int(y)
							if [x,y] not in cor_pairs:
								cor_pairs.append([x,y])

				for x in x_list:
					y = -x + a + b  # y= x translate to (a,b)  y = (x-a) + b
					d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
					if (y < b):
						if (d == 1.41):# square root of 2 is 1.41
							y = int(y)
							if [x,y] not in cor_pairs:
								cor_pairs.append([x,y])
	
	#print(cor_pairs)

	for pair in cor_pairs:
		encoded_cor_pairs.append(encode_coordinate(pair))

	return encoded_cor_pairs

def get_possible_loc(member,w,b):
	poss_loc = []

	if split(member)[1] == "K":
		current_cor = decode_coordinate(get_loc(member,w,b))
		poss_loc = king(current_cor)

	elif split(member)[1] == "Q":
		current_cor = decode_coordinate(get_loc(member,w,b))
		poss_loc = queen(current_cor)

	elif split(member)[1] == "B":
		current_cor = decode_coordinate(get_loc(member,w,b))
		poss_loc = bishop(current_cor)

	elif split(member)[1] == "N":
		current_cor = decode_coordinate(get_loc(member,w,b))
		poss_loc = knight(current_cor)

	elif split(member)[1] == "R":
		current_cor = decode_coordinate(get_loc(member,w,b))
		poss_loc = ruk(current_cor)

	elif split(member)[1] == "P":
		current_cor = decode_coordinate(get_loc(member,w,b))
		poss_loc = pone(current_cor,member)


	return poss_loc

	
def check_pone_mobility_3(com,checker_side,bloker_loc,w,b):
	phone_locs = pone(decode_coordinate(get_loc(checker_side+com[0],w,b)),checker_side+com[0])

	if len(phone_locs) == 3:
		hold_loc = [phone_locs[0],phone_locs[1]]
		kill_loc = phone_locs[2]
	elif len(phone_locs) == 4:
		hold_loc = [phone_locs[0],phone_locs[1]]
		kill_loc = phone_locs[2],phone_locs[3]
	else:
		hold_loc = [phone_locs[0],phone_locs[1]]
		kill_loc = phone_locs[2],phone_locs[3]

	command = str(com[1])+str(com[2])
	result = 0

	if bloker_loc in hold_loc:
		if command in hold_loc:
			result = 1 #Hold
			print("Cant move, a Peice is there, Speak a command again")

	elif bloker_loc in kill_loc:
		if command in kill_loc:
			result = 2 #Hold
			print("Can move, killed by pone, Say Sorry!!")
	else:
		#print("")
		result = 0

	return result


			





def check_pone_mobility(com,checker_side,bloker_loc,w,b):

	#print("Debug 1:check mobility",com,checker_side,bloker_loc,w,b)
	
	cor_player = decode_coordinate(get_loc(checker_side+com[0],w,b))
	a,b = cor_player[0],cor_player[1]
	#print(a,b)

	#print("Debug 2:",encode_coordinate([a,b+1]))
	if checker_side == 'W' :
		if bloker_loc == encode_coordinate([a,b+1]):
			print("Cant move there is a black peice infront, Speak a command again")
			if bloker_loc == encode_coordinate([a+1,b+1]):
				print("Black peice is there but still can move")
				return False
			return True
		
		else:
			return False

	elif checker_side == 'B' :
		if bloker_loc == encode_coordinate([a,b-1]):
			print("Cant move there is a white peice infront")
			if bloker_loc == encode_coordinate([a-1,b-1]):
				print("white peice is there but still can move")
				return False
			return True
		
		else:
			return False

		

def check_pone_kill_and_mobile(com,checker_side,bloker_loc,w,b):

	#print("Debug:kill mobility",com,checker_side,bloker_loc,w,b)

	cor_player = decode_coordinate(get_loc(checker_side+com[0],w,b))
	a,b = cor_player[0],cor_player[1]

	x_list = [0,1,2,3,4,5,6,7]
	y_list = [0,1,2,3,4,5,6,7]
	cor_pairs = []
	encoded_cor_pairs = []

	for x in x_list:
		y = x -a + b 
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 1.41):# square root of 2 is 1.41
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])
	for x in x_list:
		y = -x +a + b 
		d = round(math.sqrt((x-a)**2 + (y-b)**2),2)
		if (d == 1.41):# square root of 2 is 1.41
			if y in y_list:
				y = int(y)
				cor_pairs.append([x,y])

	#print(cor_pairs)

	for pair in cor_pairs:
		encoded_cor_pairs.append(encode_coordinate(pair))

	if bloker_loc in encoded_cor_pairs :
		print('Pone killed, He was a nice soldier')
		return True
	else:
		return False
