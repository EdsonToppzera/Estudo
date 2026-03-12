file = input("file name: ").lower().strip(" ")
file2 = file.split(".")

if file2[-1] == "gif":
    print("image/gif")

elif file2[-1] == "jpg":
    print("image/jpeg")

elif file2[-1] == "jpeg":
    print("image/jpeg")

elif file2[-1] == "png":
    print("image/png")

elif file2[-1] == "pdf":
    print("application/pdf")

elif file2[-1] == "txt":
    print("text/plain")

elif file2[-1] == "zip":
    print("application/zip")

else:
    print("application/octet-stream")
