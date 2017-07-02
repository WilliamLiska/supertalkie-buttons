# supertalkie-buttons

Runs on the SuperTalkie at startup to listen to buttons for various purposes.  Note that Push To Talk functionality is still handled by TalkiePi.

## Run on boot

As root, copy supertalkie-buttons into place:

```
cp /home/mumble/supertalkie-buttons/supertalkie-buttons.service /etc/systemd/system/supertalkie-buttons.service
```

Enable the service to run on boot

```
systemctl enable supertalkie-buttons.service
```
