extract = """We have developed speed, but we have shut ourselves in. Machinery that gives abundance has left us in want. Our knowledge has made us cynical. Our cleverness, hard and unkind. We think too much and feel too little. More than machinery we need humanity. More than cleverness we need kindness and gentleness."""

lines = 0
words = 0

for line in extract:
	if line==".":
		lines=lines+1
	if line==" ":
		words=words+1
characters=len(extract)
print ("number of lines", lines)
print ("number of words", words)