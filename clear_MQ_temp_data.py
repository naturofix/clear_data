import os
import sys
import fnmatch
import subprocess
import datetime


print "python clear_MQ_temp_data.py path"


test = False
global test

def generate_command(command): # uses a numiric imput to deduce the command to run
	command_list = ['trash','recover','space']
	command_list_o = []
	if command == 1:
		command_list_o = command_list[0]
		print ("%s : %s") %(command,command_list_o)
	if command == 2:
		command_list_o = command_list[1]
		print ("%s : %s") %(command,command_list_o)
	if command == 3:
		command_list_o = command_list[0:2]
		print ("%s : %s") %(command,command_list_o)
	if command == 4:
		command_list_o = command_list[2]
		print ("%s : %s") %(command,command_list_o)
	if command == 7:
		command_list_o = command_list[0:3]
		print ("%s : %s") %(command,command_list_o)
	if command == 8:
		command_list_o = command_list[0]
		test = True
	return command_list_o


for i in range(1,8):
	generate_command(i)

path = sys.argv[1]
print path

base_path = "/mnt/BLACKBURNLAB/temp_files/"
os.system('mkdir %s' %(base_path))
trash_path = '%s/trash_temp' %(base_path)
os.system('mkdir %s' %(trash_path))
#trash_path = '/MS_Experiments/temp_trash'
#trash_path = '/MS_Experiments/trash_recover'
recover_path = '%s/trash_recover' %(base_path)
os.system('mkdir %s' %(recover_path))



try:
	command = int(sys.argv[2])
except:
	command = 7
command_list = generate_command(command)
raw_input(command_list)

extension_list = ['txt','raw','msf','mzxml','txt','csv','tab','pub','doc','docx','xls','xlsx','ppt','pptx','pps','pdf','r','R','accdb','py','fasta']
global error_list
error_list = []

def run_command(cmd):
	if test == False:
		
		proc = subprocess.Popen([cmd], stderr=subprocess.PIPE, shell=True)
		(sdoutput, err) = proc.communicate()
		
		#print(sdoutput)
		if sdoutput != None:
			print(sdoutput)
			print 'error'
			raw_input('enter ...')
	else:
		print 'just testing, no file are being moved'

def create_dir(base_path,path_list,created_path_list):
	dir_line = base_path
	for dir_entry in path_list:
		dir_line = '%s/%s' %(dir_line,dir_entry)
	if dir_line not in created_path_list:
		dir_line = base_path
		for dir_entry in path_list:
			#print dir_entry
			dir_line = '%s/%s' %(dir_line,dir_entry)
			#print dir_line
			try:
				os.stat(dir_line)
				hit = 0
			except:
				hit = 1
				os.mkdir(dir_line)
				#print '\n\nmkdir %s\n\n' %(dir_line)
				#raw_input('enter')
		if hit == 1:
			print 'mkdir %s' %(dir_line)
		created_path_list.append(dir_line)
	return created_path_list

def replace_characters(name):
	print name
	replace_list = ['+','(',')']
	for char in replace_list:
		name.replace(char,'_')
	
	print name
	return name
	

def extension_scan(incorrect_files,path,extension): #looks for specific file extensions within a path
	exclude_list = ['recal.txt']

	for root, dirnames, filenames in os.walk(path):
		for filename in fnmatch.filter(filenames, '*.%s' %(extension)):
			file_name = os.path.join(root, filename) # detected filename with extension
			if '/proc/' not in file_name: # ignores directory created by maxquant
				if '/p0/' not in file_name: # ignores directory created by maxquant
					split_list = file_name.split('/')
					if split_list[len(split_list)-1] not in exclude_list:	#compares to exclude list defines above
						print file_name
						incorrect_files.append(file_name) # addes to incorrect_files list
					else:
						print '\n\n\n file in exvlusion list\n'
						print file_name
						print split_list[len(split_list)-1]
						print '\nsearching ... please wait ...\n'
	return incorrect_files # incorrect files used to decided if the path should be moved or not

#os.system('clear')
print(path)
print datetime.datetime.now()
print command_list

#raw_input('enter to continue')
if 'space' in command_list:
	
	cmd = 'du -sh %s' %(path)
	print(cmd)
	
	proc = subprocess.Popen(["du -sh %s" %(path)], stdout=subprocess.PIPE, shell=True)
	(start_size, err) = proc.communicate()
	print start_size
	

trash_exclude_list = ['keep.txt']

if 'trash' in command_list:
	proc = subprocess.Popen(["du -sh %s" %(path)], stdout=subprocess.PIPE, shell=True)
	(start_size, err) = proc.communicate()
	print start_size
	
	#raw_input('trash')
	matches = []
	print 'searching please wait ....'

	### run through path looking for a folder called combined indicating a MaxQuant analysis
	for root, dirnames, filenames in os.walk(path):
		for filename in fnmatch.filter(dirnames, 'combined'):
			matches.append(os.path.join(root, filename))
	trash_path_list = []

	#matches is a list of "combined" file directories
	for match_entry in matches:
		error_hit = 0

		keep_hit = 0
		keep_list = []
		match_list = match_entry.split('/')
		match_line = '_'.join(match_list)

		base_dir = '/'.join(match_list[:len(match_list)-1])

		for keep_file in trash_exclude_list:
			for root, dirnames, filenames in os.walk(base_dir):
				for filename in fnmatch.filter(filenames, keep_file):
					keep_list.append(os.path.join(root, filename))
		print base_dir
		print match_entry

		raw_input(keep_list)
		if keep_list == []:



			dir_line = trash_path
			for dir_entry in match_list[2:]:
				dir_line = '%s/%s' %(dir_line,dir_entry)
			

			file_list = os.listdir(match_entry)
			#print file_list
			
			# runs through the files lists in "combined folder"


			for file_entry in file_list:
				incorrect_files = 'none' #if this is not defined properly, files will be moved
				# ignores the folder txt and folders called combined
				if "txt" not in file_entry:
					if 'combined' not in file_entry:
						print '\n\nsearching through extension list, please wait ...'
						incorrect_files = []
						file_path = '%s/%s' %(match_entry,file_entry)
						print(file_path)
						for extension in extension_list: # searches through an extension list
							if incorrect_files == []: # prevent unnecessory searching if extension is detected
								incorrect_files = extension_scan(incorrect_files,file_path,extension)
						
				if incorrect_files != [] and incorrect_files != 'none': # if incorrect files is not empty, the directory is not moved (raw input to see why)
					incorrect_hit = 1
					print '\n\nERROR : potentially important file extensions found in directory to be moved\n'

					
					print file_path
					print '\nwill not be moved\n\n'
					raw_input('\n\npress enter to continue\n\n')
				if incorrect_files == []: # is incorrect files is empty, files moved to trash path
					
					trash_path_list = create_dir(trash_path,match_list[2:],trash_path_list)
					cmd = "mv %s/%s %s" %(match_entry.replace(' ','\\ '),file_entry.replace(' ','\\ '),dir_line.replace(' ','\\ '))
					print(cmd+'\n')
					run_command(cmd)

			
			# removed .index files
			base_file_list = os.listdir(base_dir)
			for base_entry in base_file_list:
				if '.index' in base_entry:
					trash_path_list = create_dir(trash_path,match_list[2:],trash_path_list)
					cmd = 'mv %s/%s %s' %(base_dir.replace(' ','\\ '),base_entry.replace(' ','\\ '),dir_line.replace(' ','\\ '))
					print(cmd+'\n')
					run_command(cmd)
					#os.system(cmd)
					cmd = 'mv %s/%s %s' %(base_dir.replace(' ','\\ '),base_entry.replace('.index','').replace(' ','\\ '),dir_line.replace(' ','\\ '))
					print(cmd+'\n')
					run_command(cmd)

			if error_hit == 1:
				error_list.append('ERROR %s\n' %(match_entry))
				#raw_input('enter to continue')
				error_hit = 0
			#raw_input()
		else:
			print '\nDetected file indicating the data should not be touched'
			for keep_entry in keep_list:
				print keep_entry
			print "Data was not moved\n"
			raw_input()
	
	
	size_list = ['\n\n\n',str(datetime.datetime.now().time()),'\n\n']
	before_line =  'before : %s\n' %(start_size)
	print(before_line)
	size_list.append(before_line)
	
	proc = subprocess.Popen(["du -sh %s" %(path)], stdout=subprocess.PIPE, shell=True)
	(after_size, err) = proc.communicate()
	after_line =  'after : %s\n' %(after_size)
	print(after_line)
	size_list.append(after_line)
	
	size_file = open('data_usage.txt','a')
	size_file.writelines(size_list)
	size_file.close()
			




if 'recover' in command_list:
	
	os.system('clear')
	print 'Revovery of %s' %(trash_path)
	print extension_list
	print 'searching through extension list, please wait ...'
	
	for extension in extension_list:
		incorrect_files = []
		print extension
		incorrect_files = extension_scan(incorrect_files,trash_path,extension)
		print incorrect_files
		if incorrect_files == []:
			print 'no selected extensions found'
		else:

			print "\n\nERROR : This file might be usefull : ERROR\n\n"
			trash_folder_list = []
			for error_entry in incorrect_files:
				print '\n\n\n' + error_entry
				split_entry = error_entry.split('/')
				entry_dir_list = split_entry[3:len(split_entry)-1]
				#print(entry_dir_list)
				dir_line = recover_path
				for dir_entry in entry_dir_list:
					#print dir_entry
					dir_line = '%s/%s' %(dir_line,dir_entry)
					#print dir_line
					try:
						os.stat(dir_line)
					except:
						os.mkdir(dir_line) 
					#raw_input('mkdir')
				trash_folder = '/'.join(split_entry[:len(split_entry)-1])
				destination_path = '/'.join(split_entry[3:len(split_entry)-1])
				trash_folder = trash_folder.replace(' ','\\ ')
				destination_path = destination_path.replace(' ','\\ ')
				if trash_folder not in trash_folder_list:
					cmd = 'mv %s %s' %('/'+trash_folder,'%s/%s' %(recover_path,destination_path))
					print('\n'+cmd)
					if test == False:
						os.system(cmd)
						trash_folder_list.append(trash_folder)
					else:
						print 'just testing script'
				else:
					print 'folder already moved'
			print "\n\nERROR : moved the whole folder : ERROR\n\n"


if 'space' in command_list:

	print 'before : ', start_size
	
	cmd = 'du -sh %s' %(path)
	print(cmd)
	
	proc = subprocess.Popen(["du -sh %s" %(path)], stdout=subprocess.PIPE, shell=True)
	(after_size, err) = proc.communicate()
	print 'after : ',after_size
	
	#cmd = 'du -sh /MS_Experiments/temp_trash'
	#print(cmd)
	#os.system(cmd)
	
	#cmd = 'du -sh /MS_Experiments/trash_recover'
	#print(cmd)
	#os.system(cmd)
	
	folder_list = os.listdir('/MS_Experiments')
	size_list = ['\n\n\n',str(datetime.datetime.now().time()),'\n\n']
	for folder_name in folder_list:
		folder_path = '/MS_Experiments/%s' %(folder_name)
		print folder_path
		if os.path.isdir(folder_path):
			if folder_name[0].isdigit():
				proc = subprocess.Popen(["du -sh /MS_Experiments/%s" %(folder_name)], stdout=subprocess.PIPE, shell=True)
				(folder_size, err) = proc.communicate()
				print folder_size
				size_list.append(str(folder_size)+'\n')
			if folder_name == trash_path or folder_name == recover_path:
				proc = subprocess.Popen(["du -sh /MS_Experiments/%s" %(folder_name)], stdout=subprocess.PIPE, shell=True)
				(folder_size, err) = proc.communicate()
				print folder_size
				size_list.append(str(folder_size)+'\n')
		
	proc = subprocess.Popen(["df -h"], stdout=subprocess.PIPE, shell=True)
	(folder_size, err) = proc.communicate()
	print folder_size
	size_list.append(str(folder_size)+'\n')
		
	size_file = open('data_usage.txt','a')
	size_file.writelines(size_list)
	size_file.close()
	
	
error_file = open('error.txt','a')
error_file.writelines(error_list)
error_file.close()
