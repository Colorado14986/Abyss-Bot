import requests
import giphypop

g = giphypop.Giphy()

f = g.translate(phrase='cat')#, limit=1)
print(f.media_url)