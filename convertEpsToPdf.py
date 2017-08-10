import os
import sys
import getopt

short_opts = "i:"
long_opts = ["ifolder="]

argv = sys.argv[1:]
try:
	opts, args = getopt.getopt(argv,short_opts,long_opts)
except getopt.GetoptError:
	raise ValueError('ERROR: Not correct input to script')
for opt, arg in opts:
	if opt in ("-i", "--ifolder"):
		# postProcFolderName = arg
		folderAddress = arg

cwd = os.getcwd() #Get working directory

os.chdir(cwd + '/' + folderAddress)

for file in os.listdir(os.getcwd()):

    if file.endswith('.eps'):
    	print('-> Converting: '+file)

    	os.system('epstopdf '+file)

os.chdir(cwd)

print('----> Execution finished')