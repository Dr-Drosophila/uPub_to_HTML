"""
fucntions that work on uPub data, but do not look at the data itself
"""

def get_paths_of_files( path ):
	"""
	- gets the paths of 5 files:
		- uPub document
		- supplement document
		- GFF/GTF
		- FASTA/FNA
		- PEP/FAA
	- returns dictionary

	- INPUT: 	path to publishable model
	- OUTPUT:	dictionary of absolute paths to 5 files
	"""
	import os
	from pprint import pprint as pprint
	file_list = getListOfFiles( path )
	file_dict = {}

	for file_path in file_list:
		file_name = file_path.split("/")[-1].upper()
		if "~" in file_name:
			continue
		else:
			if "GFF" in file_name:
				file_dict["gff"] = file_path
				continue
			elif "FASTA" in file_name or "FNA" in file_name:
				file_dict["fna"] = file_path
				continue
			elif "PEP" in file_name or "FAA" in file_name:
				file_dict["faa"] = file_path
				continue
			elif "DOCX" in file_name:
				if "UPUB" in file_name:
					file_dict["uPub_path"] = file_path
					continue
				if "SUPP" in file_name:
					file_dict["supp_path"] = file_path
					continue

	return( file_dict )

def getListOfFiles( dirName ):
	import os
	# create a list of file and sub directories
	# names in the given directory
	# from: https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/

	listOfFile = os.listdir(dirName)
	allFiles = list()
	# Iterate over all the entries
	for entry in listOfFile:
		# Create full path
		fullPath = os.path.join(dirName, entry)
		# If entry is a directory then get the list of files in this directory
		if os.path.isdir(fullPath):
			allFiles = allFiles + getListOfFiles(fullPath)
		else:
			allFiles.append(fullPath)

	return( allFiles )

def purge( dir_path ):
	"""
	- purges a particulat directory of all files and subdirectories.
	- to be used for testing purposes and cleaning the in_progress folder only
	"""
	import shutil	# to remove directory completely
	import os		# to make a new directory
	import time		# to sleep between deleting a directory and making another.
	try:
		shutil.rmtree( dir_path )
		time.sleep( 1 )
		print( "Purged:\t{0}".format( dir_path ) )
	except:
		pass
	os.mkdir( dir_path )
	print( "Created new directory:\t{0}".format( dir_path ) )
