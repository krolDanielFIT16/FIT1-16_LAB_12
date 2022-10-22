def without_proto(urls):
    return ["//".join((x.split("//"))[1:]) for x in urls]

links = [
    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "https://geeksforgeeks.org",
    "http://github.com",
    "http://www.mail.google.com"
]

lst = without_proto(links)
print(lst)
print(type(lst))
