def insta_check():
    import requests
    username = input("enter: ")
    r = requests.get("https://instagram.com/" + username)
    print(r.status_code)
    print("\n")
#insta_check()