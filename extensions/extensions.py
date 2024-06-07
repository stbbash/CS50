answer = input("File Name: ").lower().strip()

if answer.endswith(".gif"):
    print("image/gif")
elif answer.endswith(".jpeg") or answer.endswith(".jpg"):
    print("image/jpeg")
elif answer.endswith(".png"):
    print("image/png")
elif answer.endswith(".pdf"):
    print("application/pdf")
elif answer.endswith(".txt"):
    print("text/plain")
elif answer.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
