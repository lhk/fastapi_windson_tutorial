useful commands

```
az webapp ssh --resource-group langwhisp --name languagewhispererv2

az webapp log tail --resource-group langwhisp --name languagewhispererv2
```

the webapp log tail command can wake up the webapp, the ssh command doesn't seem to be able to do that.
so if you want to ssh onto the app and it complains about not being active, try the log call first.