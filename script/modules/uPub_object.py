"""
- module that houses an object of type uPub

"""

class uPub_data(object):
	"""docstring for `uPub_data`."""

	def __init__(self, line):
		import hashlib
		"""assigns values to the object.
		INPUT:  MD file containing all data; path to image
		"""
		self.title = None					# title of the microPublication
		self.path_to_image = None
		self.gff = None
		self.fna = None
		self.faa = None
		self.uPub_path = None
		self.supp_path = None
		self.md_path = None
		self.publication_data = None		# data for publication (author list, figure title, etc...) as dictionary

	def show( self ):
		"""prints the object as a DICTIONARY
		"""
		from pprint import pprint as pprint
		pprint( self.__dict__ )

	def docx_to_md( uPub_doc ):
		"""
		- converts uPub doc from DOCX to MD
		- saves the image to disc and links to object
		- returns dictionary of paths to MD and PNG file
		"""
		import os			# to run pandoc from the command line
		from uPub_overworld_defs import getListOfFiles

		md_path = ".".join(uPub_doc.split(".")[:-1])+".md"
		image_folder = "/".join(uPub_doc.split("/")[:-1])+"_pub_image"
		os.system( "pandoc -s {0} --extract-media {2} --wrap=none --reference-links -t markdown -o {1}".format(
			uPub_doc,
			md_path,
			image_folder,
		) )

		image_file_name = getListOfFiles( image_folder )[0]

		output_dict = {
			"image_file_name"	:	image_file_name,
			"md_path"			:	md_path,
		}

		return( output_dict )

	def associate_all_data( uPub_data_object ):
		"""
		- takes in a uPub_data object and associates
		- calls in other methods to get each separate thing like title, figure text, etc...
		- returns a dictionary of the publication data:
		dict = {
			title				: 	...............		,
			author_list			:	[
				corresponding,
				other1,
				other2,
				...
			],
			figure_text			:	...............		,
			...
		}
		- uses other definitions to get invidual objects

		- INPUT:	uPub_data_object
		- OUTPUT:	dictionary that houses publication_data
		"""
		from pprint import pprint as pprint

		title = uPub_data.get_title( uPub_data_object.md_path )
		authors = uPub_data.get_authors( uPub_data_object.md_path )
		image_caption = uPub_data.get_image_caption( uPub_data_object.md_path )

		data = {
			"title"				:	title 				,
			"authors"			:	authors				,
			"image_caption"		:	image_caption		,
		}

		# print( "DATA", end="\t" )
		# pprint( data )
		return( data )
		# return( "Finished running uPub_data.associate_all_data( uPub_data_object )" )

	def get_title( md_path ):
		"""
		- reads in the md_path file and returns the name of the publication
		- INPUT: 	MD PATH (STR)
		- OUTPUT:	TITLE OF PUBLICATION (STR)
		"""
		title = ""
		with open( md_path, "r" ) as md_file:
			for line in md_file:
				if "title:" in line:
					title = line.strip()[8:-1]
					break

		return( title )

	def get_authors( md_path ):
		"""
		- gets the authors of the microPublication
		- return a list of objects of type author
		"""
		from author_object import author

		# filter out the section that houses author information.
		# Pass that list of lists to a function in the author class to return author data

		author_data_raw = author.grab_author_data( md_path )
		author_data_formatted = author.format_author_data( author_data_raw )

		return( author_data_formatted )

	def get_image_caption( md_path ):

		return( "test_image_caption" )
