import os
import sys
import fnmatch
import time
import datetime
import filecmp


def new_dir(test_path):
	if not os.path.isdir(test_path):
		cmd = 'mkdir %s' %(test_path)
		print cmd
		os.system(cmd)


		
core_path = "/mnt/BLACKBURNLAB/temp_files"
base_path = sys.argv[1]

rep_path = '%s/ref_rep/' %(core_path)
new_dir(rep_path)

test = False
try :
	test = sys.argv[2]
except:
	print base_path
	print('python remove_replicate_files.py <path> test   : test will prevent deleting files')
	raw_input('enter to run script and delete all replicate raw files')
	test = False


file_list = ['*.raw']
print file_list
refs = []
file_name_list = []
print('running search')
for file_name in file_list:
	print file_name
	for root, dirnames, filenames in os.walk(base_path):
			for filename in fnmatch.filter(filenames, file_name):
				refs.append(os.path.join(root, filename))
				file_name_list.append(filename)
				#print filename
print('search done')

total =  len(refs)
print total
reps_count = 0
diffs = 0
hist = 0
mv_file_list = []
for i in range(0,len(file_name_list)):
	file_name = file_name_list[i]
	file_path = refs[i]
	#print file_path
	#print file_name
	number = file_name_list.count(file_name)
	#li = file_name_list.index(file_name)
	#print li
	#print refs[li]
	#print number
	if number > 1: 
		print file_name
		print number
		indices = [i for i, x in enumerate(file_name_list) if x == file_name]
		dups = [refs[j] for j in indices]
		times = []

		for dup_file_path in dups:
			if os.path.exists(dup_file_path):
				times.append(os.path.getmtime(dup_file_path))
		#print dups
		#print times
		min_index = times.index(min(times))
		#print min_index
		#print times[min_index]
		first_file = dups[min_index]
		if  os.path.exists(first_file) and os.path.exists(file_path):
			if 'History' not in file_path:
				if file_path != first_file:
					print "\n"
					print first_file
					print file_path
					if filecmp.cmp(first_file,file_path):
						print 'same file'
						cmd = 'mv %s %s' %(file_path,rep_path)
						print cmd
						reps_count += 1
						if test == False:
							os.system(cmd)
							print 'moved'
							mv_file_list.append(file_path)
					else:
						print 'not the same'
						diffs += 1
				else:
					print 'first file'  
			else:
				print 'in history'
				hist += 1
		else:
			missing_file_list = []
			if not os.path.exists(file_path):
				missing_file_list.append(file_path)
			if not os.path.exists(first_file):
				missing_file_list.append(first_file)
			for missing_file in missing_file_list:
				print '\n\n\n##################### Error ###################\n\n\n'
				if file_path in mv_file_list:
					print 'file already moved, which is rather strange'
				else:
					print 'file not in moved list'
				print '%s no longer exists' %file_path
				print '\n\n\n##################### Error ###################\n\n\n'
				raw_input('enter to continue')

		print 'total : %s' %total
		print i
		print 'reps  : %s (%s%s)' %(reps_count,round(float(reps_count)/float(i),3)*100,'%')		
		print 'same name different file = %s' %(diffs)
		print 'in history : %s' %(hist)


print 'total : %s' %total
print 'reps  : %s (%s%s)' %(reps_count,round(float(reps_count)/float(i),3)*100,'%')
print 'same name different file = %s' %(diffs)
print 'in history : %s' %(hist)
	
# for file_path in refs
# 	if os.path.exists(file_path):
# 		cmd = 'mv %s %s' %(file_path.replace(' ','\ '),wash_month)
# 		print cmd
# 		if test == False:
# 			os.system(cmd)
# 			print 'executed'
# 			#raw_input()


	
