# the purpose of this script is to check to file location and make sure files exist in both.
# if not file should be copied to to a temp folder in the second location



import os
import sys
import fnmatch
import time
import datetime
import filecmp

path_1 = sys.argv[1]
path_2 = sys.argv[2]
path_3 = '/mnt/BLACKBURNLAB/'

raw = True
other = True


def new_dir(test_path):
	if not os.path.isdir(test_path):
		cmd = 'mkdir %s' %(test_path)
		print cmd
		os.system(cmd)

# test = False
# try :
# 	test = sys.argv[3]
# except:

# 	print('python check_4_duplicates.py <path_1> <path_2> test   : test will prevent deleting files')
# 	raw_input('enter to run script, all raw file not duplicated on both paths, will be copied to path_2')
# 	test = False
if raw == True:

	raw_input('\n\nenter to run script, all raw file not duplicated on both paths, will be copied to %s/missing_files \n\n' %(path_2))

	missing_file_list = []

	cmd = 'mkdir missing_files'
	os.system(cmd)
	write_file = open('missing_files/%s_duplications.txt' %(path_1.replace('/','_')),'a')


	file_list = ['*.raw']
	print file_list
	raw_1 = []
	file_name_list_1 = []
	print('running search %s' %(path_1))
	for file_name in file_list:
		print file_name
		for root, dirnames, filenames in os.walk(path_1):
				for filename in fnmatch.filter(filenames, file_name):
					raw_1.append(os.path.join(root, filename))
					file_name_list_1.append(filename)
					#print filename
	print('search 1 done')

	print(len(raw_1))
	print(len(set(file_name_list_1)))

	write_file.write('%s : %s\n\n' %(path_1,len(raw_1)))

	raw_2 = []
	file_name_list_2 = []
	print('running search %s' %path_3)
	for file_name in file_list:
		print file_name
		for root, dirnames, filenames in os.walk(path_3):
				for filename in fnmatch.filter(filenames, file_name):
					raw_2.append(os.path.join(root, filename))
					file_name_list_2.append(filename)
					#print filename
	print('search 2 done')

	print(len(raw_2))
	print(len(set(file_name_list_2)))




	for entry in list(set(file_name_list_1)):
		print '\n\n'
		print entry
		#index_1 = file_name_list_1.index(entry)
		index_1 = [i for i, x in enumerate(file_name_list_1) if x == entry]
		print index_1
		#index_2 = file_name_list_2.index(entry)
		index_2 = [i for i, x in enumerate(file_name_list_2) if x == entry]
		print index_2
		for i in index_1:
			file_1 =  raw_1[i]
			hit = 0
			dup_list = []
			print file_1
			for j in index_2:
				file_2 =  raw_2[j]
				print file_2
				print filecmp.cmp(file_1,file_2)
				if filecmp.cmp(file_1,file_2) == True:
					hit += 1
					dup_list.append(file_2)
			if hit == 0:
				missing_file_list.append(file_1+'\n')
				new_path = '%s/missing_files/' %(path_2)
				new_dir(new_path)


				file_list = file_1.split('/')
				#print file_list
				path_list = file_list[4:len(file_list)-1]
				for path_entry in path_list:
					new_path = '%s/%s' %(new_path,path_entry)
					new_dir(new_path)
				output_path = new_path
				cmd = 'cp %s %s/%s' %(file_1,output_path,entry)
				print cmd
				os.system(cmd)
			if hit > 1:
				write_file.write('\n%s : %s copies in %s\n' %(file_1,hit,path_2))
				for dup in dup_list:
					write_file.write('\t\t%s\n' %(dup))
				write_file.flush()
				#raw_input()
	write_file.close()

	print missing_file_list


	write_file = open('missing_files/%s_missing.txt' %(path_1.replace('/','_')),'a')
	write_file.writelines(missing_file_list)
	write_file.close()

if other == True:
	print '\n\nsearching for QE configuration files\n\n'

	file_extension_list = ['xlsx', 'pptx', 'docx', 'db', 'sld', 'pdf','meth','csv',]
	file_list_ext = []
	for file_name in file_extension_list:
		print file_name
		for root, dirnames, filenames in os.walk(path_1):
				for filename in fnmatch.filter(filenames, '*.%s' %file_name):
					file_list_ext.append(os.path.join(root, filename))
					#print filename
	for file_path in file_list_ext:
		#missing_file_list.append(file_1+'\n')
		#print 'missing file %s' %file_1
		new_path = '%s/QE_files/' %(path_2)
		new_dir(new_path)


		file_list = file_path.split('/')
		path_list = file_list[4:len(file_list)-1]
		for path_entry in path_list:
			new_path = '%s/%s' %(new_path,path_entry)
			new_dir(new_path)
		output_path = new_path
		cmd = 'cp %s %s/%s' %(file_path,output_path,file_list[-1])
		print cmd
		os.system(cmd)
	











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


	
