"""
- contains data for a single author
"""

class author( object ):
	"""docstring for `uPub_data`."""

	def __init__(self, line):
		import hashlib
		"""assigns values to the object.
		INPUT:  MD file containing all data; path to image
		"""
		self.fname = None
		self.lname = None
		self.contribution = None
		self.affiliation = None
		self.email = None
		self.ORCIDiD = None
		self.corresponding_author = False
		self.submitting_author = False
		self.equal_contribution = False

	def show( self ):
		"""prints the object as a DICTIONARY
		"""
		from pprint import pprint as pprint
		pprint( self.__dict__ )

	def grab_author_data( md_path ):
		"""
		- grabs all the author data from the md_path
		- returns a list of strings that contain all the data
		"""

		grab_line = False				# bool to check if you should grab that particular line
		author_data = []

		with open( md_path, "r" ) as md_file:
			for line in md_file:
				if ( "^1Ω^" in line.strip() and "^2^" in line.strip() ) or line.strip() == "**Author Contributions: **":
					grab_line = True
				elif line.strip() == "![][1]" or line.strip() == "Please select a tag below that best describes your submission":
					grab_line = False
				if grab_line and len( line.strip() ) != 0:
					author_data.append( line.strip() )
		return( author_data )

	def format_author_data( list_of_raw_author_data ):
		"""
		- gets the list of string of raw author data
		- returns dictionary of formatted author data
		"""
		from pprint import pprint as pprint

		# pprint( list_of_raw_author_data )

		list_names = list_of_raw_author_data[0].split(", ")
		affiliations = list_of_raw_author_data[ 1 : list_of_raw_author_data.index("> ^Ω^ To whom correspondence should be addressed") ]
		contributions = list_of_raw_author_data[ list_of_raw_author_data.index("**Author Contributions: **")+1 :]

		author_list = []

		for person in list_names:
			corresponding_author = False
			auth = author( person )

			if "Ω" in person:
				auth.corresponding_author = True
			if list_names.index( person ) == 0:
				auth.submitting_author = True

			temp = person.replace( "Ω", "" )

			num = int(temp[-2])
			full_name = temp[:-3]
			auth.fname = " ".join(full_name.split()[:-1])
			auth.lname = full_name.split()[-1]
			auth.affiliation = affiliations[num-1]
			auth.contribution = author.convert_contributions_to_dict(contributions)[full_name]

			author_list.append( auth )

		return( author_list )

	def convert_contributions_to_dict( contributions ):
		"""
		- converts the list of onctibutions to a dictionary of contributions for each author
		"""

		author_line = True
		contribution_line = False

		author_contribution = {}
		temp = "---||---".join( contributions )
		temp = temp.replace( "---||----   ", ";" )
		associated_contributions = temp.split("---||---")
		for item in associated_contributions:
			temp = item.split(";")
			contris = temp[1:]
			list_auths = temp[0].split(", ")
			for auth in list_auths:
				author_contribution[auth] = contris

		return( author_contribution )
