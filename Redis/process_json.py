import string
import json
from fractions import Fraction

def is_json(myjson):
   try:
      json_object = json.loads(myjson)
   except ValueError, e:
      return False
   return True

fin = open('/var/www/html/BigData/Redis/nutrition.json', 'r')
fout = open('/var/www/html/BigData/Redis/nutrition_clean.json', 'w')
writeup = open('/var/www/html/BigData/Redis/writeup.md', 'w')
filtered_chars = []
chars = []
lines = 0
processed_lines = 0

for line in fin:
	#add 1 to total lines
	lines += 1
	if is_json(line):
		processed_lines += 1
		#removes non-ascii chars
		clean_line = filter(lambda x: x in string.printable, line)
		#if chars have been removed from the line, adds each removed char
		#and line number to list of filtered chars
		if line != clean_line:
			filtered = filter(lambda x: x not in string.printable, line)
			for ch in filtered:
				filtered_chars.append([ch,lines])
		clean_line = json.loads(clean_line)
		fout.write(json.dumps(clean_line,sort_keys=True))
bad_lines = lines - processed_lines
ratio = str(Fraction(bad_lines, processed_lines))
ratio = ratio.replace('/',':')
for i in filtered_chars:
	chars.append(i[0])
	
unique_chars = set(chars)
writeup.write('### Json File Processing\n')
writeup.write('### Written by Rebecca Roberts\n')
writeup.write('- Total lines: '+str(lines)+'  \n')
writeup.write('- Total lines processed: '+str(processed_lines)+'  \n')
writeup.write('- Total lines not processed: '+str(bad_lines)+'  \n')
writeup.write('- Ratio of bad to good lines: '+ratio+'  \n')
writeup.write('- Characters removed: '+str(len(filtered_chars))+'  \n')
writeup.write('- Unique characters: ')
for i in unique_chars:
	writeup.write(str(i)+' ')
writeup.write('  \n\nAll characters removed:  \n')
for ch in filtered_chars:
	writeup.write('- Illegal character '+str(ch[0])+' found on line '+str(ch[1])+'  \n')
	
fin.close()
fout.close()


