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

def getFiles(drive, folder_id):
    query = "\'"+folder_id + "' in parents and trashed=false"
    fileList = drive.ListFile({'q': query}).GetList()
    return fileList

def getId(drive, folderName, parentFolder):
    fileList = getFiles(drive, parentFolder)
    for file1 in fileList:
        if file1['title'] == folderName:
            return file1['id']
    return None

def createFolder(drive, folderName, parentFolder):
    folder = drive.CreateFile({'title': folderName, 'mimeType': 'application/vnd.google-apps.folder', 'parents':["'"+parentFolder+"'"]})
    folder.Upload()
    return folder['id']

def createFolderIfNotExists(drive, folderName, parentFolder):
    folder_id = getId(drive, folderName, parentFolder)
    if folder_id is None:
        folder_id = createFolder(drive, folderName, parentFolder)
    return folder_id



if __name__ == '__main__':
    drive = getDriveInstance()
    #listFiles(drive)
    #upload(drive)
    picamId = getId(drive, 'picam', 'root')
    print(picamId)
    testId = getId(drive, 'test', picamId)
    print(testId)
    helloId = createFolder(drive, 'hello', picamId)
    print(helloId)
