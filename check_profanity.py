__author__ = 'jannie'

import urllib

def read_text():
	quotes = open("movie_quotes.txt")
	contents = quotes.read()
	quotes.close()
	check_profanity(contents)


def check_profanity(text_to_check):
	conn = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = conn.read()
	conn.close()
	if "true" in output:
		print "Profanity Alert!"
	elif "false" in output:
		print "This document has no curse words!"
	else:
		print "Could not scan the document properly"

read_text()