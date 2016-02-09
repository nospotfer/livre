import sys, string, os, datetime, time, glob, subprocess, re, fnmatch
#WARNING! DELETES EVERYTHING ON THE SOLR SERVER. 
#USE WITH CARE!

def makeChoi(yeh, neh):
    accept = {}
    # for w in words:
    accept['yes'] = [ '', yeh, yeh.lower(), yeh.upper(), yeh.lower()[0], yeh.upper()[0] ]
    accept['no'] = [ neh, neh.lower(), neh.upper(), neh.lower()[0], neh.upper()[0] ]
    return accept

accepted = makeChoi('Yes', 'No')

def doYeh():
    print('Yeh! Let\'s do it.')
	cmd = "curl http://localhost:8983/solr/collection1/update -H \"Content-Type: text/xml\" --data-binary \"<delete><query>*:*</query></delete>\"";
	print(cmd);
	#os.system(delete);

	commit = "curl http://localhost:8983/solr/collection1/update -H \"Content-Type: text/xml\" --data-binary \"<commit/>\"";
	print(commit);
	#os.system(commit);
	
def doNeh():
    print('Neh! Let\'s not do it.')

choi = None
while not choi:
    choi = input( 'This will delete everything on Solr. Proceed?: Y/n? ' )
    if choi in accepted['yes']:
        choi = True
        doYeh()
    elif choi in accepted['no']:
        choi = True
        doNeh()
    else:
        print('Your choice was "{}". Please use an accepted input value ..'.format(choi))
        print( accepted )
        choi = None


