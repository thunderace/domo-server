#!/usr/bin/PYTHON
# -*- coding: utf-8 -*-

from ftplib import FTP
import os

host = '82.66.49.29'
#port = 8132
#usr = 'root'
port = 8136
usr = 'pi'
pwd = 'tetris'

localDir = '.'
#remoteDir = '/var/www/node-domo'
remoteDir = '/var/www/domo-server'

excludedDir = { ".git" , "node_modules", "python", "bdd" }

def copyDirToFtp(ftp, localDir, remoteDir, excludedDir):
    print("\ncopy files from "+localDir+" to "+remoteDir)
    if os.path.isdir(localDir):
      for f in os.listdir(localDir):
        print(f)
        filePath = os.path.join(localDir, f)
        if os.path.isdir(filePath):
          if not f in excludedDir:
            ftp.cwd(remoteDir)
            #ftp.mkd(f);
            copyDirToFtp(ftp, filePath, remoteDir+"/"+f, excludedDir)
        else:
          fh = open(filePath, 'rb')
          ftp.cwd(remoteDir)
          ftp.storbinary('STOR %s' % f, fh)
    else:
      print("Source dir does not exist")    
    print("copy ended\n")

def deleteAllFiles(ftp):
  for n in ftp.nlst():
    try:
      if n not in ('.','..'):
        print('Working on..'+n)
        try:
          ftp.delete(n)
          print('Deleted...'+n)
        except Exception:
          print(n+' Not deleted, we suspect its a directory, changing to '+n)
          ftp.cwd(n)
          deleteAllFiles(ftp)
          ftp.cwd('..')
          print('Trying to remove directory ..'+n)
          ftp.rmd(n)
          print('Directory, '+n+' Removed')
    except Exception:
      print('Trying to remove directory ..'+n)
      ftp.rmd(n)
      print('Directory, '+n+' Removed')
             
def connect_ftp(localDir, remoteDir, excludedDir, host, port, usr, pwd):
    ftp = FTP()
    print("connection to server")
    ftp.connect(host, port)
    ftp.login(usr, pwd)
    print("connection ok")
    
    os.chdir(localDir)
    localDir = os.getcwd()
    
    ftp.cwd(remoteDir)
    
    copyDirToFtp(ftp, localDir, remoteDir, excludedDir)
        
    ftp.quit()
    ftp.close()
    print("connection closed")
    
connect_ftp(localDir, remoteDir, excludedDir, host, port, usr, pwd)
