import os
import sys
import fnmatch
import time
import datetime

def new_dir(test_path):
	if not os.path.isdir(test_path):
		cmd = 'mkdir %s' %(test_path)
		print cmd
		os.system(cmd)

base_path = "/blackburn3/RAW_BACKUP"

wash_path = '%s/wash' %(base_path)
new_dir(wash_path)
test = False

try :
	test = sys.argv[1]
except:
	print base_path
	raw_input('python remove_wash_file.py    : without run it will only test the directories')
	test = False


folder_list = os.listdir(base_path)
#print(folder_list)
dir_list = []
for folder_name in folder_list:
	if os.path.isdir('%s/%s' %(base_path,folder_name)):
		dir_list.append(folder_name)
dir_list.sort()
#print dir_list
#raw_input()
for i in range(1,len(dir_list)+1):
	j= i-1
	print("%s : %s") %(i,dir_list[j])
print('This program removes all files with wash in the filename')
folder_number = int(raw_input('select folder folder by number : '))
selected_folder = (dir_list[folder_number-1])
#raw_input(selected_folder)
year_path = '%s/%s' %(base_path,selected_folder)
#print year_path
#raw_input(year_path)
wash_year = '%s/%s' %(wash_path,selected_folder)
new_dir(wash_year)
subfolder_list = os.listdir(year_path)
print subfolder_list

for subfolder in subfolder_list:
	month_path = "%s/%s" %(year_path,subfolder)
	if os.path.isdir(month_path):
		print month_path
		wash_month = '%s/%s' %(wash_year,subfolder)
		new_dir(wash_month)
		file_list = ['*wash*.raw','*Wash*.raw','*WASH*.raw','*blank*.raw','*Blank*.raw','*BLANK*.raw']
		refs = []
		for file_name in file_list:
			for root, dirnames, filenames in os.walk(month_path):
					for filename in fnmatch.filter(filenames, file_name):
						refs.append(os.path.join(root, filename))
		for file_path in refs:
			if os.path.exists(file_path):
				cmd = 'mv %s %s' %(file_path.replace(' ','\ '),wash_month)
				print cmd
				if test == False:
					os.system(cmd)
					print 'executed'
			#raw_input()


	