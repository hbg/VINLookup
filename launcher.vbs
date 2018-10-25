Set cmd = CreateObject("WScript.shell")

cmd.run"cmd"
WScript.sleep 200
cmd.Sendkeys"cd  C:\Users\legos\AppData\Local\Programs\Python\Python36{Enter}"
WScript.sleep 200
cmd.Sendkeys"python C:\Users\legos\OneDrive\Desktop\VINLookup\src\{Enter}"
WScript.sleep 500
