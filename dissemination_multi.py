import math

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--youtube", type=str, action='append', nargs=3)
parser.add_argument("-i", "--instagram", type=str, action='append', nargs=3)
parser.add_argument("-n", "--newsletter", type=str, action='append', nargs=3)
parser.add_argument("-l", "--live", type=str, action='append', nargs=3)
parser.add_argument("-o", "--csv", type=int)

args = parser.parse_args()

print('')
print('')

today_day = []
today_mo = []
repeat = []

today_day.append(int(args.youtube[0][0]))
today_mo.append(int(args.youtube[0][1]))
repeat.append(int(args.youtube[0][2]))

today_day.append(int(args.instagram[0][0]))
today_mo.append(int(args.instagram[0][1]))
repeat.append(int(args.instagram[0][2]))

today_day.append(int(args.newsletter[0][0]))
today_mo.append(int(args.newsletter[0][1]))
repeat.append(int(args.newsletter[0][2]))

today_day.append(int(args.live[0][0]))
today_mo.append(int(args.live[0][1]))
repeat.append(int(args.live[0][2]))


#print(today_day)
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

#print(today_day)

pairs_list_clean = []

for sm_index in range(4):
	if sm_index == 0:
		sm = 'YT'
	elif sm_index == 1:
		sm = 'IG'
	elif sm_index == 2:
		sm = 'N'
	elif sm_index == 3:
		sm = 'L'
	else:
		sm = ' '

	day = int(today_day[sm_index])
	mo = int(today_mo[sm_index])
	repeat_num = int(repeat[sm_index])


	while mo < 13:
		if (repeat_num > day) and ((day + repeat_num) > months_len[mo]):
        		next_ocasion_day = day + repeat_num - months_len[mo+1]
        		next_ocasion_mo = mo + 1
			
			pair_clean = [next_ocasion_day, next_ocasion_mo]

			pair = [next_ocasion_day, next_ocasion_mo, sm]
		else:
        		if (day+ repeat_num) <= months_len[mo]:
                		next_ocasion_day = day + repeat_num
                		next_ocasion_mo = mo
				pair_clean = [next_ocasion_day, next_ocasion_mo]
				pair = [next_ocasion_day, next_ocasion_mo, sm]
        		else:
                		next_ocasion_day = day + repeat_num - months_len[mo]
                		next_ocasion_mo = mo + 1
				pair_clean = [next_ocasion_day, next_ocasion_mo]
				pair = [next_ocasion_day, next_ocasion_mo, sm]

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

	print('')
	print('')

	flag_mo = 0
	flag_week = 0
	flag_day = 0

	for p in pairs_list:
		
		if m+1 == p[1]:
			flag_mo = 1



#	print('tm'+str(today_mo))
#	print('tw'+str(total_week))
#	print('td'+str(total_day))

        i=0

	flag_week = 1



        for j in range(7):
                s=''
                for n in range(7):
			flag_day = 0
			sm = ''
			key = str(((j-1)*7)+n-plus_per_mo[m+1]+1)
			if [(((j-1)*7)+n-plus_per_mo[m+1]+1),m+1,'YT'] in pairs_list:
				flag_day = 1
				sm = 'YT.'
			if [(((j-1)*7)+n-plus_per_mo[m+1]+1),m+1,'L'] in pairs_list:
				flag_day = 1
				sm = sm+'L.'
			if [(((j-1)*7)+n-plus_per_mo[m+1]+1),m+1,'N'] in pairs_list:
                                flag_day = 1
				sm = sm+'N.'
			if [(((j-1)*7)+n-plus_per_mo[m+1]+1),m+1,'IG'] in pairs_list:
                                flag_day = 1
				sm = sm+'IG'
	
			if flag_mo == 1 and flag_day == 1 and flag_week == 1:

				if csv_option == 1:
					s=s+'('+str(sm)+')\t'
				else:
					s=s+str(sm)+'*\t'
			else:
				if (((j-1)*7)+n-plus_per_mo[m+1]+1) < 1 or (((j-1)*7)+n-plus_per_mo[m+1]+1) > months_len[m+1]:
					if csv_option == 1:
						s=s+str('--     ')+'\t'
					else:
						s=s+str('--    ')+'\t'
				else:
					if csv_option == 1:
						s=s+str(((j-1)*7)+n-plus_per_mo[m+1]+1)+'     '+'\t'
					else:
						s=s+str(i+n+1)+' '+str(((j-1)*7)+n-plus_per_mo[m+1]+1)+str('     ')+'\t'
			#s=s+'--\t'
			#else:	
			#	s=s+str(i+n+1)+'\t'
                print(s)

#	print('flag mo '+str(flag_mo))

        print('')
