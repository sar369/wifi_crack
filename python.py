import subprocess
command = "ifconfig down ; iwconfig wlan0 mode monitor ; ifconfig wlan0 up ; iwconfig"
result = subprocess.run(["bash test.sh"] capture_output=True, text=True)

if result.returncode == 0:
	print("Output:")
	print(result.stdout)
else:
	print("Error")
