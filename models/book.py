class Book:
    def __init__(self, title, author, genre, description, id):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.checked_out = False
        self.id = id

