#!/usr/bin/env python

output_file = open("preseed.seed", 'w')
with open("preseed-template.seed", 'r') as source_file:
	for line in source_file:
		if line[0] != "#" and line != "\n":
			output_file.write(line)
output_file.close()

