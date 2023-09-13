import laspy
import sys
import os
import subprocess

file_path = sys.argv[1]
file_name = os.path.basename(sys.argv[1]).split('.')

if file_name[-1] == 'laz':
    file = laspy.read(file_path)
    file = laspy.convert(file)
    output_file_name = './tmp/{a}.las'.format(a=file_name[0])
    file.write(output_file_name)
if file_name[-1] == 'las':
	output_file_name = file_path

sys.stdout.write(output_file_name)