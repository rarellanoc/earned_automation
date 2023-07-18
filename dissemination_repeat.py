import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--day", type=int)
parser.add_argument("-m", "--month", type=int)
parser.add_argument("-r", "--repeat", type=int)
parser.add_argument("-c", "--csv", type=int)



args = parser.parse_args()
today_day = args.day
today_mo = args.month
repeat = args.repeat
csv_option = args.csv



months_len = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8: 31, 9:30, 10:31, 11:30, 12:31, 13:31}


#for j in range(5):
#	i=0
#	print(str(i+1)+'\t'+str(i+2)+'\t'+str(i+3)+'\t'+str(i+4)+'\t'+str(i+5)+'\t'+str(i+6)+'\t'+str(i+7))


#year_started_on_day_of_the_week = input('day year started, example: mon is 1 : ')

year_started_on_day_of_the_week = 7
 
#today_day = input('today day : ')
#repeat = input('repeat each _ days: ')

pairs_list = []



#repeat ocasions list


day = today_day
mo = today_mo

while mo < 13:

	if (repeat > day) and ((day + repeat) > months_len[mo]):
        	next_ocasion_day = day + repeat - months_len[mo+1]
        	next_ocasion_mo = mo + 1
		pair = [next_ocasion_day, next_ocasion_mo]
	else:
        	if (day+ repeat) <= months_len[mo]:
                	next_ocasion_day = day + repeat
                	next_ocasion_mo = mo
			pair = [next_ocasion_day, next_ocasion_mo]
        	else:
                	next_ocasion_day = day + repeat - months_len[mo]
                	next_ocasion_mo = mo + 1
			pair = [next_ocasion_day, next_ocasion_mo]


	pairs_list.append(pair)
	day = next_ocasion_day
	mo = next_ocasion_mo
	

#print(pairs_list)


#print('')

plus_per_mo_2023_test = {1:6, 2:2, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
plus_per_mo = {}

initial_plus = year_started_on_day_of_the_week - 1

plus_per_mo[1] = initial_plus
for m in range(11):
        #print(m)
        initial_plus_working = plus_per_mo[m+1]

        cant_slots_until_31 = initial_plus_working + months_len[m+1]

        #38
        cant_slots_until_1_next = cant_slots_until_31 + 1

        next_number = cant_slots_until_1_next - (7*5) -1

        if (next_number < 0):
                next_number = next_number + 7
        #print(next_number)

        plus_per_mo[m+2] = next_number

#print('pre: '+str(plus_per_mo_2023_test))
#print('post '+str(plus_per_mo))


#version 1 

for m in range(12):

        print('month : '+str(m+1))

	flag_mo = 0
	flag_week = 0
	flag_day = 0

	for p in pairs_list:
		
		if m+1 == p[1]:
			flag_mo = 1


	total_day = plus_per_mo[m+1] + today_day
	total_week = math.ceil(total_day / 7) +1

#	print('tm'+str(today_mo))
#	print('tw'+str(total_week))
#	print('td'+str(total_day))


        i=0
        for j in range(7):
                s=''

		if total_week == j+1 or j:
			flag_week = 1
		else:
			flag_week = 0

                for n in range(7):


			key = str(((j-1)*7)+n-plus_per_mo[m+1]+1)
				
			if [(((j-1)*7)+n-plus_per_mo[m+1]+1),m+1] in pairs_list:
				flag_day = 1
			else:
				flag_day = 0

			if flag_mo == 1 and flag_week == 1 and flag_day == 1:
				
				if csv_option == 1:
					s=s+'('+str(key)+')\t'
				else:
					s=s+str(key)+'** \t'
			else:
				if (((j-1)*7)+n-plus_per_mo[m+1]+1) < 1 or (((j-1)*7)+n-plus_per_mo[m+1]+1) > months_len[m+1]:
					if csv_option == 1:
						s=s+str('--')+'\t'
					else:
						s=s+str('--')+'\t'
				else:
					if csv_option == 1:
						s=s+str(((j-1)*7)+n-plus_per_mo[m+1]+1)+'\t'
					else:
						s=s+str(i+n+1)+' '+str(((j-1)*7)+n-plus_per_mo[m+1]+1)+'\t'
			#s=s+'--\t'
			#else:	
			#	s=s+str(i+n+1)+'\t'
                print(s)

#		print('flag week '+str(flag_week))
#	print('flag mo '+str(flag_mo))

        print('')

