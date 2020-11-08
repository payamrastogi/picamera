from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os

def getDriveInstance():
    gauth = GoogleAuth()
    gauth.CommandLineAuth()
    drive = GoogleDrive(gauth)
    return drive

def listFiles(drive):
    fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in fileList:
        print('title: %s, id: %s' % (file1['title'], file1['id']))

def upload(drive):
    os.chdir("/home/pi/upload")
    for file in glob.glob("*.jpg"):
        print (file)
        with open(file, "r") as f:
            fn = os.path.basename(f.name)
            file_drive = drive.CreateFile({ 'title': fn })
            file_drive.SetContentFile(fn)
            file_drive.Upload()
            print ("The file: " + fn + " has been uploaded ")
            os.remove(fn)
    print ("All files have been uploaded")



if __name__ == '__main__':
    drive = getDriveInstance()
    listFiles(drive)
    upload(drive)
