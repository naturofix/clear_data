import os
import sys
import subprocess

path = sys.argv[1]
file_list = os.listdir(path)

line_list = []
for file_name in file_list:
	path_name = '%s/%s' %(path,file_name)
	if os.path.isdir(path_name):
		cmd = 'du -sh %s' %(path_name)
		print cmd
        	proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
        	(start_size, err) = proc.communicate()
        	print start_size
		#line = '%s : %s' %(path_name,start_size)
		#print(line)
		#os.system(cmd)
		line_list.append(start_size)

file_name = '/blackburn3/scripts/clear_data/space.txt'
write_file = open(file_name,'w')
write_file.writelines(line_list)
write_file.close()



