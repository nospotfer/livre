import sys, string, os, datetime, time, glob, subprocess, re, fnmatch
#Uploads previously generated XML files in a folder to Solr
#UNIX version (slashes = / )
currFolder = os.path.dirname(os.path.realpath(__file__));

# Write a list of all XML files on the rootFolder to a file. Recursive.
rootFolder = "%s\\videos\\" % currFolder; #XML root Folder. Change this path if necessary. Attention windows/unix slash direction
outputXMLList = "XMLFiles.txt" 
type = "*.xml"
XMLFiles = []
for root, dirs, files in os.walk(rootFolder):
	for filename in fnmatch.filter(files, type):
		XMLFiles.append(os.path.join(root, filename))

#Write XML list to txt file
fid = open(outputXMLList, 'w');
for XMLFile in XMLFiles:
	fid.write(XMLFile + "\n");
fid.close();

#uploads XML to Solr
print('XML Files list populated successfully. \n Now Uploading to Solr ... \n');
for XMLFile in XMLFiles:
	cmd = "curl http://localhost:8983/solr/LIvRE/update  -H \"Content-Type: text/xml\" --data-binary @" + XMLFile;
	print(cmd);
	os.system(cmd);

cmd = "curl http://localhost:8983/solr/LIvRE/update  -H \"Content-Type: text/xml\" --data-binary \"<commit/>\"";
#print(cmd);
os.system(cmd);
