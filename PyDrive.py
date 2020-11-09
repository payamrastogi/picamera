from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import glob, os
import logging
import logging.config

class PyDrive:
    def __init__(self):
        gauth = GoogleAuth()
        gauth.CommandLineAuth()
        self.drive = GoogleDrive(gauth)
        logging.config.fileConfig('pyDriveLog.conf',disable_existing_loggers=0)
        self.logger = logging.getLogger('pydrivelogger')

    def listFiles(self):
        fileList = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
        for file1 in fileList:
            print('title: %s, id: %s' % (file1['title'], file1['id']))

    def upload(self, fileName):
        with open(fileName, "r") as f:
            fn = os.path.basename(f.name)
            file_drive = self.drive.CreateFile({ 'title': fn })
            file_drive.SetContentFile(fileName)
            file_drive.Upload()
            self.logger.info("Uploaded: "+fn)
            os.remove(fileName)

    def getFiles(self, folder_id):
        query = "\'"+folder_id + "' in parents and trashed=false"
        fileList = self.drive.ListFile({'q': query}).GetList()
        return fileList

    def getId(self, folderName, parentFolder):
        fileList = self.getFiles(parentFolder)
        for file1 in fileList:
            if file1['title'] == folderName:
                return file1['id']
        return None

    def createFolder(self, folderName, parentFolder):
        folder = self.drive.CreateFile({'title': folderName, 'mimeType': 'application/vnd.google-apps.folder', 'parents':["'"+parentFolder+"'"]})
        folder.Upload()
        return folder['id']

    def createFolderIfNotExists(self, folderName, parentFolder):
        folder_id = self.getId(folderName, parentFolder)
        if folder_id is None:
            folder_id = self.createFolder(folderName, parentFolder)
        return folder_id

#pyDrive = PyDrive()
#pyDrive.upload('/home/pi/upload/picam-2020-11-09 00:44:35.731405.jpg')
