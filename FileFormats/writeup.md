## Program 1 Writeup 
#### File Conversion
This particular set of data is a simple table with fixed rows and columns.  This means that every object in the json file will have identical keys.  So we really only need to read the field names once, rather than looking for them over and over as we would have to if we were converting from yaml or xml.  So the sql or csv files look like the best options.  The csv file does not contain the field names, but reading the csv file is easier because we do not have to ignore instructions as we would with the sql file.  So converting the csv file looks like the easiest, most efficient option, assuming we already know the field names.

I used Python to write the script.  Here's how it works:  
1. Read a line  
2. Remove quotes and whitespace  
3. Split the line by commas  
4. Write each field name to the json file, followed by the element of the array that matches it, referred to by index.  These are the key-value pairs, with each line being a json object.  
5. Repeat this for the entire file.  
This is simple enough that a number of languages would probably work pretty well.  Python may have good libraries for this sort of thing, but that is irrelevant since we are not using them for this assignment.  So the language chosen did not affect the file type chosen for conversion.
The json file produced by this program is 814MB, a little bigger than the yaml file.  This makes sense since the json file is sort of like the yaml file plus brackets, braces, commas, and quotation marks, minus only the dashes. 

Important note: the files in this repository are much smaller portions of the original files, since GitHub rejects any pushes that contain files larger than 100 MB (see https://help.github.com/articles/working-with-large-files/).

Here are all the files with original and compressed sizes:
#### File Compression
| type | size  | zip  | ratio | gzip | ratio |
|------|-------|------|-------|------|-------|
| csv  | 484MB | 51MB |  90%  | 59MB |  88%  |
| sql  | 467MB | 52MB |  89%  | 60MB |  87%  |
| xml  | 2.3GB | 82MB |  96%  | 75MB |  97%  |
| yml  | 771MB | 52MB |  93%  | 61MB |  92%  |
| json | 814MB | 54MB |  93%  | 63MB |  92%  |
XML has the highest compression ratio.  This is probably because it has by far the most repeated strings (e.g. <column name= ... </column>), which can be reduced to a reference to the previous identical string.
