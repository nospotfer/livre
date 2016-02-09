import os, string, sys, glob, time, datetime
#1)Extracts mainframes with ffmpeg
#2)Creates .xml with request-handler
#IMPORTANT! ffmpeg and lire-request-handler.jar should be on the system path!
#UNIX version (slashes = / )

keyframeRate = 1;
keyframeHeight = 480;

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print ("usage: python extractFramesWIN.py video_file [output_folder_name] [rate] [filter_options]");
	else:
		videoFile = sys.argv[1];
		if len(sys.argv) >= 3:
			outputFolder = sys.argv[2];
			outputFolder = outputFolder.rstrip("\\");
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
		
		# # Write list of keyframes to file
		# outputListFile = outputFolder + ".txt";
		# keyframeFiles = glob.glob(outputFolder + "\\*.jpg");
		# keyframeFiles.sort();
		# fid = open(outputListFile, 'w');
		# for keyframeFile in keyframeFiles:
			# fid.write(keyframeFile + "\n");
		# fid.close();
				
		#Create XMLs
		#currFolder = os.path.dirname(os.path.realpath(__file__));
		#XMLFolder = "%s/VideoKeyframesXML/" % currFolder; #Extracted XML Folder. Change this path if necessary. 
		#base=os.path.basename(outputListFile);
		#name = XMLFolder + os.path.splitext(base)[0];

		# cmd = "java -jar lire-request-handler.jar -i " + outputListFile + " -o " + outputFolder +".xml"; # -y ph,cl,eh,jc,ce,ac"; #extracts all 6 features
		# print (cmd);
		# os.system(cmd);
		

		
