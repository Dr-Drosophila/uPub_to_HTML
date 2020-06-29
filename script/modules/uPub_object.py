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
		self.title = None
		self.path_to_image = None
		self.gff = None
		self.fna = None
		self.faa = None
		self.uPub_doc = None
		self.supp_doc = None

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

		md_path = ".".join(uPub_doc.split(".")[:-1])+".md"
		image_folder = "/".join(uPub_doc.split("/")[:-1])+"pub_image"
		print( "md_path:", md_path )
		os.system( "pandoc -s {0} --extract-media {2} --wrap=none --reference-links -t markdown -o {1}".format(
			uPub_doc,
			md_path,
			image_folder,
		) )

		return( uPub_doc )
