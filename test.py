import subprocess

results = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])

#print(results);
results = results.decode("ascii");
print(results);