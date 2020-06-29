"""

- takes in a single/multiple directories containing:
	- datafiles/{*.gff, *.fasta, *.pep}

"""

### imports ==================================================================
import sys										# for creation/testing
sys.path.insert(0,"/Users/rele.c/Desktop/GEP/currently_working/uPub_to_HTML/script/modules")
from uPub_object import uPub_data					# import the object from the above directory
import uPub_overworld_defs						# for definitions that work on uPub data
from pprint import pprint as pprint				# for neat printing to console
import os										# to get list of files in directory
from distutils.dir_util import copy_tree		# to copy fill file_path


### variables/paths ==========================================================
testing_data = "/Users/rele.c/Desktop/GEP/currently_working/uPub_to_HTML/data/raw/testing"
working_data = "/Users/rele.c/Desktop/GEP/currently_working/uPub_to_HTML/data/in_progress"
formatted_data = "/Users/rele.c/Desktop/GEP/currently_working/uPub_to_HTML/data/generated"

# purge the working_data folder
uPub_overworld_defs.purge( working_data )
### code =====================================================================

publishable_models = [ os.path.join(testing_data, o) for o in os.listdir(testing_data) if os.path.isdir(os.path.join(testing_data,o)) ]

for model in publishable_models:
	working_destination = "{0}/{1}".format( working_data, model.split("/")[-1] )
	copy_tree( model, working_destination )
	file_paths = uPub_overworld_defs.get_paths_of_files( working_destination )
	temp = uPub_data( "temp" )
	temp.gff = file_paths["gff"]
	temp.faa = file_paths["faa"]
	temp.fna = file_paths["fna"]
	temp.uPub_doc = file_paths["uPub_doc"]
	temp.supp_doc = file_paths["supp_doc"]

	print( uPub_data.docx_to_md( temp.uPub_doc ) )

	temp.show()
