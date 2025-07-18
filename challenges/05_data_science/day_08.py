import pandas as pd

data = [
    {
        "title": "The Silent Forest",
        "author": "Jane Hill",
        "genre": "Mystery",
        "description": "A detective uncovers secrets hidden deep in the woods while chasing a serial killer."
    },
    {
        "title": "Spacebound",
        "author": "Rico Vega",
        "genre": "Science Fiction",
        "description": "An astronaut embarks on a mission to Mars but discovers an ancient alien presence."
    },
    {
        "title": "Love in Paris",
        "author": "Emily Rose",
        "genre": "Romance",
        "description": "A love story between a local baker and a traveler unfolds in the heart of Paris."
    },
    {
        "title": "Quantum Heist",
        "author": "Leo Hunt",
        "genre": "Thriller",
        "description": "A group of hackers plans a digital heist targeting the world's most secure quantum server."
    },
    {
        "title": "Mystic Academy",
        "author": "Lara Moon",
        "genre": "Fantasy",
        "description": "A young girl discovers she has magical powers and is taken to an academy for gifted spellcasters."
    },
    {
        "title": "The Digital Mind",
        "author": "Alan Neural",
        "genre": "Science Fiction",
        "description": "An AI begins to question its creators and the meaning of consciousness."
    },
    {
        "title": "Fog Over London",
        "author": "Claire Black",
        "genre": "Mystery",
        "description": "Set in Victorian London, a private investigator unravels political conspiracies amid murders."
    },
    {
        "title": "Beneath the Waves",
        "author": "Diana Coast",
        "genre": "Adventure",
        "description": "An underwater archaeologist discovers an ancient city lost in the ocean."
    },
    {
        "title": "Heart Strings",
        "author": "Ella Harmony",
        "genre": "Romance",
        "description": "Two musicians from rival bands fall in love during a national tour."
    },
    {
        "title": "Dark Code",
        "author": "Nick Cipher",
        "genre": "Thriller",
        "description": "A cybersecurity expert is drawn into a global web of espionage and hidden messages."
    }
]

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("✅ Book dataset created")