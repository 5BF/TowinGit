;ControlFocus('title','text',controlID)Edit1=Edit instance 1
ControlFocus("��","","Edit1")

;Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)

;Set the file name text on the Edit filed
ControlSetText("��","","Edit1","C:\Users\Administrator\PycharmProjects\untitled2\Towin\test1.jpg")

;Click on the Open button
ControlClick("��","","Button1")
