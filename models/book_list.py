from models.book import *

book1 = Book("The Adventures of Huckleberry Finn", "Mark Twain", "American Fiction", "Revered by all of the town's children and dreaded by all of its mothers, Huckleberry Finn is indisputably the most appealing child-hero in American literature. Unlike the tall-tale, idyllic world of Tom Sawyer, The Adventures of Huckleberry Finn is firmly grounded in early reality. From the abusive drunkard who serves as Huckleberry's father, to Huck's first tentative grappling with issues of personal liberty and the unknown, Huckleberry Finn endeavors to delve quite a bit deeper into the complexities — both joyful and tragic of life.", 1)
book2 = Book("In Search of Lost Time", "Marcel Proust", "Philosphical Fiction", "Swann's Way, the first part of A la recherche de temps perdu, Marcel Proust's seven-part cycle, was published in 1913. In it, Proust introduces the themes that run through the entire work. The narrator recalls his childhood, aided by the famous madeleine; and describes M. Swann's passion for Odette. The work is incomparable. Edmund Wilson said '[Proust] has supplied for the first time in literature an equivalent in the full scale for the new theory of modern physics.'", 2)
book3 = Book("The Republic", "Plato", "Philosphy", "The Republic is a Socratic dialogue by Plato, written c. 380 B.C.E.. It is one of the most influential works of philosophy and political theory, and Plato's best known work. In Plato's fictional dialogues the characters of Socrates as well as various Athenians and foreigners discuss the meaning of justice and examine whether the just man is happier than the unjust man by imagining a society ruled by philosopher-kings and the guardians. The dialogue also discusses the role of the philosopher, Plato's Theory of Forms, the place of poetry, and the immortality of the soul.", 3)
book4 = Book("Oedipus the King", "Sophocles", "Greek Tragedy", "Oedipus the King is an Athenian tragedy by Sophocles that was first performed c. 429 BC. It was the second of Sophocles's three Theban plays to be produced, but it comes first in the internal chronology, followed by Oedipus at Colonus and then Antigone. Over the centuries, it has come to be regarded by many as the Greek tragedy par excellence.", 4)

books = [book1, book2, book3, book4]

def add_new_book(book):
    books.append(book)


def check_out_book(self, book_id):
    if self.id == book_id:
        self.checked_out = True