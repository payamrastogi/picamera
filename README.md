#### settings.yaml
```
client_config_backend: 'settings'
client_config:
  client_id: <client_id>
  client_secret: <client_secret>
save_credentials: True
save_credentials_backend: 'file'
save_credentials_file: 'creds.json'
oauth_scope:
- "https://www.googleapis.com/auth/drive"

```

#### client_secrets.json
```
{"installed":{"client_id":"<client_id>","project_id":"picamera-295003","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"<client_secret>","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}

```

## References:
- https://www.raspberrypi.org/documentation/remote-access/ssh/scp.md
- https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
- https://pythonhosted.org/PyDrive/filemanagement.html#upload-a-new-file
- https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button/all#:~:text=We%20can%20reboot%20the%20Pi,reboot%20(%20%2Dr%20)%20command.
- https://docs.python.org/2/library/multiprocessing.html#exchanging-objects-between-processes
- https://www.dummies.com/programming/python/how-to-delete-a-file-in-python/
- https://stackoverflow.com/questions/20690951/check-if-time-is-between-tonight-and-tomorrow-morning
- https://www.tutorialspoint.com/python/python_functions.htm
- https://developers.google.com/drive/api/v3/search-files
- https://pymotw.com/2/Queue/
- https://stackoverflow.com/questions/42401108/when-is-queue-join-necessary
- https://medium.com/analytics-vidhya/pydrive-to-download-from-google-drive-to-a-remote-machine-14c2d086e84e
- https://medium.com/@annissouames99/how-to-upload-files-automatically-to-drive-with-python-ee19bb13dda
- https://linuxize.com/post/how-to-run-linux-commands-in-background/
- https://stackoverflow.com/questions/20154490/how-to-log-everything-into-a-file-using-rotatingfilehandler-by-using-logging-con
- https://unix.stackexchange.com/questions/506347/why-do-most-systemd-examples-contain-wantedby-multi-user-target
