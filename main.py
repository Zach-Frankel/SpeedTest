import speedtest
import datetime

choice = int(input("1 = Test for internet speed\n2 = Input speed manually\n\nChoice: "))
if choice == 1:
    s = speedtest.Speedtest()
    print("Testing internet speed:")
    speed = s.download()
    print(f"{int(speed / 1048576)} Mbps")
elif choice == 2:
    speed = float(input("Input your speed in Mbps: "))
    speed = speed * 1048576

fileSize = float(input("How big is the file? !! MUST BE IN GB\n\n"))
fileSizeBytes = fileSize * 1073741824

time = fileSizeBytes / (speed / 8)
formattedTime = str(datetime.timedelta(seconds=time))
formattedTime = str(formattedTime).split(".")[0]
print(f"It will take {formattedTime} to download {fileSize}GB.")