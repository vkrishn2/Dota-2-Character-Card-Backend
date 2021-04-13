import subprocess
import sys

if len(sys.argv) == 2:
    value = sys.argv[1]
else:
    value = ""
print("Starting fetch of data on Dota 2...\n")
subprocess.call("python dota2_download_info.py "+value)
print("Finished. Now uploading to MongoDB...\n")
subprocess.call("python dota2_upload_to_mongodb.py")
print("Finished.")
