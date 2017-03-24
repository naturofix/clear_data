# the purpose of this script is to check to file location and make sure files exist in both.
# if not file should be copied to to a temp folder in the second location



import os
import sys
import fnmatch
import time
import datetime
import filecmp

os.system('clear')
raw_input('\n\nprogram lists all files and *.raw in a path and writes them to a text file\n\npython list_all_files.py <path>\n\nenter to continue...\n\n')

path_1 = sys.argv[1]


os.system('mkdir file_list')

def new_dir(test_path):
	if not os.path.isdir(test_path):
		cmd = 'mkdir %s' %(test_path)
		print cmd
		os.system(cmd)

file_list = ['*']

file_extension_list = ['xlsx','txt', 'pptx', 'docx', 'db', 'cal', 'sld', 'pdf','meth']
print file_list

print('running search %s' %(path_1))

for file_name in file_list:
	print file_name
	raw_1 = []
	file_name_list_1 = []
	for root, dirnames, filenames in os.walk(path_1):
			for filename in fnmatch.filter(filenames, file_name):
				raw_1.append(os.path.join(root, filename))
				file_name_list_1.append(filename)
				#print filename
	print('search 1 done')

	print(len(raw_1))
	print(len(set(file_name_list_1)))


	output_file_name = 'file_list/%s_%s.txt' %(path_1.replace('/','_'),file_name.replace('*','all'))
	print output_file_name
	write_list = [x+'\n' for x in raw_1]
	write_file = open(output_file_name,'w')
	write_file.writelines(write_list)
	write_file.close()

#for x in file_name_list_1:
#	print x
	
extension_list = [e.split('.')[-1] for e in file_name_list_1]
print set(extension_list)
file_extension_list = ['xlsx','txt', 'pptx', 'docx', 'db', 'cal', 'sld', 'pdf','meth']
print file_extension_list

raw_input('edit if its not complete')


# for i in range(0,len(file_name_list)):
# 	file_name = file_name_list[i]
# 	file_path = refs[i]
# 	#print file_path
# 	#print file_name
# 	number = file_name_list.count(file_name)
# 	#li = file_name_list.index(file_name)
# 	#print li
# 	#print refs[li]
# 	#print number
# 	if number > 1: 
# 		print file_name
# 		print number
# 		indices = [i for i, x in enumerate(file_name_list) if x == file_name]
# 		dups = [refs[j] for j in indices]
# 		times = []

# 		for dup_file_path in dups:
# 			if os.path.exists(dup_file_path):
# 				times.append(os.path.getmtime(dup_file_path))
# 		#print dups
# 		#print times
# 		min_index = times.index(min(times))
# 		#print min_index
# 		#print times[min_index]
# 		first_file = dups[min_index]
# 		if  os.path.exists(first_file) and os.path.exists(file_path):
# 			if 'History' not in file_path:
# 				if file_path != first_file:
# 					print "\n"
# 					print first_file
# 					print file_path
# 					if filecmp.cmp(first_file,file_path):
# 						print 'same file'
# 						cmd = 'mv %s %s' %(file_path,rep_path)
# 						print cmd
# 						reps_count += 1
# 						if test == False:
# 							os.system(cmd)
# 							print 'moved'
# 							mv_file_list.append(file_path)
# 					else:
# 						print 'not the same'
# 						diffs += 1
# 				else:
# 					print 'first file'  
# 			else:
# 				print 'in history'
# 				hist += 1
# 		else:
# 			missing_file_list = []
# 			if not os.path.exists(file_path):
# 				missing_file_list.append(file_path)
# 			if not os.path.exists(first_file):
# 				missing_file_list.append(first_file)
# 			for missing_file in missing_file_list:
# 				print '\n\n\n##################### Error ###################\n\n\n'
# 				if file_path in mv_file_list:
# 					print 'file already moved, which is rather strange'
# 				else:
# 					print 'file not in moved list'
# 				print '%s no longer exists' %file_path
# 				print '\n\n\n##################### Error ###################\n\n\n'
# 				raw_input('enter to continue')

# 		print 'total : %s' %total
# 		print i
# 		print 'reps  : %s (%s%s)' %(reps_count,round(float(reps_count)/float(i),3)*100,'%')		
# 		print 'same name different file = %s' %(diffs)
# 		print 'in history : %s' %(hist)


# print 'total : %s' %total
# print 'reps  : %s (%s%s)' %(reps_count,round(float(reps_count)/float(i),3)*100,'%')
# print 'same name different file = %s' %(diffs)
# print 'in history : %s' %(hist)
	
# for file_path in refs
# 	if os.path.exists(file_path):
# 		cmd = 'mv %s %s' %(file_path.replace(' ','\ '),wash_month)
# 		print cmd
# 		if test == False:
# 			os.system(cmd)
# 			print 'executed'
# 			#raw_input()


	
