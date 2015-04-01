from getpass import getpass
from ftplib import FTP
import os

def publish():
  username = raw_input("Username: ")
  password = getpass()
  ftp = FTP('mpwoz.com')
  try: 
    status = ftp.login(username, password)
  except: 
    print "Invalid login, try again."
    return publish()
  sendFiles(ftp)
  ftp.quit()
  print "Done."

def sendFiles(ftp):
  for root, dirs, files in os.walk('www'):
    for fname in files:
      full_fname = os.path.join(root, fname)
      unprefixed_fname =  '/'.join(full_fname.split('/')[1:] ) # remove 'build' prefix
      #print os.path.split(full_fname)
      print(full_fname, unprefixed_fname)
      ftp.dir()
      ftp.mkd(root)
      ftp.storbinary("STOR {0}".format(unprefixed_fname), open(full_fname, 'rb'))

    


if __name__ == "__main__":
  publish()
  
