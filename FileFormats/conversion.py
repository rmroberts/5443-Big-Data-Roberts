fin = open('/var/www/html/BigData/FileFormats/xaa.csv')
jsonoutput = open('GpsFilePoints.json', 'w');

jsonoutput.write('[\n')

#reads and writes the first line, without a comma
line = fin.readline()
line = line.strip()
line = line.translate(None, '"')
line = line.split(',')	
#`UserID`, `FileID`, `PointID`, `Lat`, `Lon`, `Ele`, `Time`, `Course`, `Hdop`, `Sat`, `Filtered`
jsonoutput.write('{\n"UserID": '+line[0]+',\n"FileID": '+line[1]+',\n"PointID": '+line[2]+',\n"Lat": '+line[3]+',\n"Lon": '+line[4]+',\n"Ele": '+line[5]+',\n"Time": '+line[6]+\
	',\n"Course": '+line[7]+',\n"Hdop": '+line[8]+',\n"Sat": '+line[9]+',\n"Filtered": '+line[10]+'\n}\n')
	
for line in fin:
	line = line.strip()
	line = line.translate(None, '"')
	line = line.split(',')
	if len(line) >= 10:
		jsonoutput.write(',\n')
		jsonoutput.write('{\n"UserID": '+line[0]+',\n"FileID": '+line[1]+',\n"PointID": '+line[2]+',\n"Lat": '+line[3]+',\n"Lon": '+line[4]+',\n"Ele": '+line[5]+',\n"Time": '+line[6]+\
			',\n"Course": '+line[7]+',\n"Hdop": '+line[8]+',\n"Sat": '+line[9]+',\n"Filtered": '+line[10]+'\n}\n')

jsonoutput.write(']')

fin.close()
jsonoutput.close()