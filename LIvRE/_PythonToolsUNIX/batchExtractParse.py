import os, string, sys, glob, time, datetime
#1)Creates a list with all .avi .mpg .mp4 .webm .flv .3gp .f4v .mkv .rm .ogg (modify me if any other specific format is needed)
#2)Creates list with folder names
#3)Extracts keyframes of all movie files with ffmpeg into separate folders
#4)Write list of keyframes to file
#5)Creates .xml for each of these folders with request-handler

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print ("usage: python extract_keyframes.py video_file [output_folder_name] [rate] [filter_options]");
	else:
		videoFile = sys.argv[1];
		if len(sys.argv) >= 3:
			outputFolder = sys.argv[2];
			outputFolder = outputFolder.rstrip("/");
		else:
			root,name = os.path.splitext(videoFile);
			outputFolder = root + "_keyframes";
		if len(sys.argv) >= 4:
			rate = int(sys.argv[3]);
		else:
			rate = 1;
		if len(sys.argv) >= 5:
			filters = "-vf " + sys.argv[4];
		else:
			filters = "";

		# Make sure keyframes folder exists
		if not os.path.exists(outputFolder):
			os.makedirs(outputFolder);
		
		
		
		# Save keyframes as JPEG files
		cmd = "ffmpeg -i %s -y -an -qscale 0 -f image2 -r %d %s -loglevel quiet %s/%%06d.jpg" % (videoFile, rate, filters, outputFolder);
		print (cmd);
		os.system(cmd);	
		#TODO: Be sure that the keyframes are not already extracted
		
		# Write list of keyframes to file
		outputListFile = outputFolder + ".txt";
		keyframeFiles = glob.glob(outputFolder + "/*.jpg");
		keyframeFiles.sort();
		fid = open(outputListFile, 'w');
		for keyframeFile in keyframeFiles:
			fid.write(keyframeFile + "\n");
		fid.close();
		#TODO Be sure it overwrites previous .txt
		
		#Create XML
		cmd = "java -jar lire-request-handler.jar -i " + outputListFile + " -o " + outputFolder +".xml";
		print (cmd);
		os.system(cmd);
		
		
		#uploads XML to Solr
		#cmd = "curl http://localhost:8983/solr/collection1/update  -H \"Content-Type: text/xml\" --data-binary @" + outputFolder +".xml";
		#print(cmd);
		#os.system(cmd);
		#cmd = "curl http://localhost:8983/solr/collection1/update  -H \"Content-Type: text/xml\" --data-binary \"<commit/>\"";
		#print(cmd);
		#os.system(cmd);
		
