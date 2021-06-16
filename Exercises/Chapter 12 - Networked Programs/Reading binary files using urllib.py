import urllib.error
import urllib.request

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0

# To copy any file with any size, we retrieve the data in blocks (buffers)
while True:
    info = img.read(10000)
    if len(info) < 1:
        break
    size = size + len(info)
    fhand.write(info)
    print(size, end='\t')

print(f"\n\n{size} characters copied")
fhand.close()
