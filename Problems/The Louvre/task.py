class Painting:

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year


tit = input()
art = input()
yr = input()

new_paint = Painting(tit, art, yr)

print('"{0}" by {1} ({2}) hangs in the Louvre.'
      .format(new_paint.title, new_paint.artist, new_paint.year))
