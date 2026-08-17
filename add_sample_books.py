from app import app, db, Book

sample_books = [
    # Classics (10 books)
    Book(
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        genre="Classic",
        description="A story of wealth, love, and the American Dream in the Jazz Age.",
        year_published=1925,
        isbn="978-0-7432-7356-5"
    ),
    Book(
        title="To Kill a Mockingbird",
        author="Harper Lee",
        genre="Classic",
        description="A young girl's view of racial injustice in the Deep South.",
        year_published=1960,
        isbn="978-0-06-112008-4"
    ),
    Book(
        title="1984",
        author="George Orwell",
        genre="Sci-Fi",
        description="A dystopian vision of a totalitarian future where Big Brother watches all.",
        year_published=1949,
        isbn="978-0-452-28423-4"
    ),
    Book(
        title="Pride and Prejudice",
        author="Jane Austen",
        genre="Romance",
        description="A classic tale of love, class, and social standing in Regency England.",
        year_published=1813,
        isbn="978-0-14-143951-8"
    ),
    Book(
        title="The Hobbit",
        author="J.R.R. Tolkien",
        genre="Fantasy",
        description="A hobbit's unexpected journey to reclaim a lost kingdom from a dragon.",
        year_published=1937,
        isbn="978-0-395-07122-2"
    ),
    Book(
        title="Moby-Dick",
        author="Herman Melville",
        genre="Classic",
        description="The obsessive quest of Captain Ahab to hunt the white whale.",
        year_published=1851,
        isbn="978-0-14-243724-7"
    ),
    Book(
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        genre="Classic",
        description="A teenage boy's journey through New York City and his struggles with identity.",
        year_published=1951,
        isbn="978-0-316-76948-0"
    ),
    Book(
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        genre="Fantasy",
        description="The epic quest to destroy the One Ring and defeat the dark lord Sauron.",
        year_published=1954,
        isbn="978-0-618-64015-7"
    ),
    Book(
        title="Animal Farm",
        author="George Orwell",
        genre="Classic",
        description="A satirical tale of farm animals who rebel against their human farmer.",
        year_published=1945,
        isbn="978-0-452-28424-1"
    ),
    Book(
        title="Jane Eyre",
        author="Charlotte Brontë",
        genre="Romance",
        description="A young governess falls in love with her brooding employer.",
        year_published=1847,
        isbn="978-0-14-243720-9"
    ),
    
    # Sci-Fi (12 books)
    Book(
        title="Dune",
        author="Frank Herbert",
        genre="Sci-Fi",
        description="A desert planet becomes the center of an interstellar empire's power struggle.",
        year_published=1965,
        isbn="978-0-441-17271-9"
    ),
    Book(
        title="Foundation",
        author="Isaac Asimov",
        genre="Sci-Fi",
        description="A mathematician predicts the fall of the Galactic Empire and plans to save humanity.",
        year_published=1951,
        isbn="978-0-553-29335-7"
    ),
    Book(
        title="Neuromancer",
        author="William Gibson",
        genre="Sci-Fi",
        description="A washed-up hacker is hired for one last job in cyberspace.",
        year_published=1984,
        isbn="978-0-441-56959-5"
    ),
    Book(
        title="Snow Crash",
        author="Neal Stephenson",
        genre="Sci-Fi",
        description="A hacker and a skateboard courier battle a dangerous new drug in the metaverse.",
        year_published=1992,
        isbn="978-0-553-38095-8"
    ),
    Book(
        title="The Left Hand of Darkness",
        author="Ursula K. Le Guin",
        genre="Sci-Fi",
        description="A human envoy navigates a planet where inhabitants have no fixed gender.",
        year_published=1969,
        isbn="978-0-441-47812-5"
    ),
    Book(
        title="Ender's Game",
        author="Orson Scott Card",
        genre="Sci-Fi",
        description="A young prodigy is trained to lead Earth's fleet against an alien threat.",
        year_published=1985,
        isbn="978-0-8125-5070-2"
    ),
    Book(
        title="The Hitchhiker's Guide to the Galaxy",
        author="Douglas Adams",
        genre="Sci-Fi",
        description="An ordinary Earthman is swept into an intergalactic adventure with his alien friend.",
        year_published=1979,
        isbn="978-0-345-39180-3"
    ),
    Book(
        title="Brave New World",
        author="Aldous Huxley",
        genre="Sci-Fi",
        description="A dystopian vision of a genetically engineered, pleasure-driven society.",
        year_published=1932,
        isbn="978-0-06-085052-4"
    ),
    Book(
        title="Fahrenheit 451",
        author="Ray Bradbury",
        genre="Sci-Fi",
        description="A fireman in a future society where books are banned and burned.",
        year_published=1953,
        isbn="978-1-4516-7331-9"
    ),
    Book(
        title="The Martian",
        author="Andy Weir",
        genre="Sci-Fi",
        description="An astronaut is stranded on Mars and must survive using his wits.",
        year_published=2011,
        isbn="978-0-553-41802-6"
    ),
    Book(
        title="Ready Player One",
        author="Ernest Cline",
        genre="Sci-Fi",
        description="A teenager hunts for an Easter egg in a virtual reality world.",
        year_published=2011,
        isbn="978-0-307-88744-3"
    ),
    Book(
        title="The Time Machine",
        author="H.G. Wells",
        genre="Sci-Fi",
        description="An inventor travels to the distant future and encounters two strange races.",
        year_published=1895,
        isbn="978-0-14-143997-6"
    ),
    
    # Fantasy (10 books)
    Book(
        title="Harry Potter and the Philosopher's Stone",
        author="J.K. Rowling",
        genre="Fantasy",
        description="A young boy discovers he's a wizard and begins his magical education.",
        year_published=1997,
        isbn="978-0-439-70818-8"
    ),
    Book(
        title="The Name of the Wind",
        author="Patrick Rothfuss",
        genre="Fantasy",
        description="A legendary hero tells his life story to a chronicler.",
        year_published=2007,
        isbn="978-0-7564-0474-1"
    ),
    Book(
        title="The Way of Kings",
        author="Brandon Sanderson",
        genre="Fantasy",
        description="In a world of storms and magic, warriors fight for survival.",
        year_published=2010,
        isbn="978-0-7653-2635-5"
    ),
    Book(
        title="A Game of Thrones",
        author="George R.R. Martin",
        genre="Fantasy",
        description="Noble families fight for control of the Iron Throne.",
        year_published=1996,
        isbn="978-0-553-57340-4"
    ),
    Book(
        title="The Lion, the Witch and the Wardrobe",
        author="C.S. Lewis",
        genre="Fantasy",
        description="Children discover a magical world through a wardrobe.",
        year_published=1950,
        isbn="978-0-06-447104-6"
    ),
    Book(
        title="The Final Empire",
        author="Brandon Sanderson",
        genre="Fantasy",
        description="A rebellion against an immortal emperor who rules with an iron fist.",
        year_published=2006,
        isbn="978-0-7653-4562-2"
    ),
    Book(
        title="The Subtle Knife",
        author="Philip Pullman",
        genre="Fantasy",
        description="A boy and a girl journey through parallel worlds to save the universe.",
        year_published=1997,
        isbn="978-0-679-87925-1"
    ),
    Book(
        title="The Eye of the World",
        author="Robert Jordan",
        genre="Fantasy",
        description="A young man discovers he's the Dragon Reborn, destined to save the world.",
        year_published=1990,
        isbn="978-0-8125-1181-9"
    ),
    Book(
        title="Good Omens",
        author="Neil Gaiman and Terry Pratchett",
        genre="Fantasy",
        description="An angel and a demon team up to prevent the apocalypse.",
        year_published=1990,
        isbn="978-0-06-085397-6"
    ),
    Book(
        title="The Ocean at the End of the Lane",
        author="Neil Gaiman",
        genre="Fantasy",
        description="A man returns to his childhood home and remembers magical events.",
        year_published=2013,
        isbn="978-0-06-225565-5"
    ),
    
    # Mystery/Thriller (8 books)
    Book(
        title="Murder on the Orient Express",
        author="Agatha Christie",
        genre="Mystery",
        description="A detective investigates a murder on a luxury train.",
        year_published=1934,
        isbn="978-0-06-269366-2"
    ),
    Book(
        title="The Girl with the Dragon Tattoo",
        author="Stieg Larsson",
        genre="Mystery",
        description="A journalist and a hacker investigate a wealthy family's dark secrets.",
        year_published=2005,
        isbn="978-0-307-47347-9"
    ),
    Book(
        title="The Da Vinci Code",
        author="Dan Brown",
        genre="Mystery",
        description="A symbologist uncovers a religious conspiracy in Paris.",
        year_published=2003,
        isbn="978-0-385-50420-1"
    ),
    Book(
        title="And Then There Were None",
        author="Agatha Christie",
        genre="Mystery",
        description="Ten strangers are invited to an island and one by one, they die.",
        year_published=1939,
        isbn="978-0-06-207348-8"
    ),
    Book(
        title="The Silent Patient",
        author="Alex Michaelides",
        genre="Mystery",
        description="A therapist tries to uncover why a famous painter killed her husband.",
        year_published=2019,
        isbn="978-1-250-30169-7"
    ),
    Book(
        title="Where the Crawdads Sing",
        author="Delia Owens",
        genre="Mystery",
        description="A young woman raised in the marsh becomes a murder suspect.",
        year_published=2018,
        isbn="978-0-7352-1909-0"
    ),
    Book(
        title="The Woman in the Window",
        author="A.J. Finn",
        genre="Mystery",
        description="A woman with agoraphobia witnesses a crime from her window.",
        year_published=2018,
        isbn="978-0-06-267841-6"
    ),
    Book(
        title="The Hound of the Baskervilles",
        author="Arthur Conan Doyle",
        genre="Mystery",
        description="Sherlock Holmes investigates a mysterious death on the moors.",
        year_published=1902,
        isbn="978-0-14-313745-3"
    ),
    
    # Romance (8 books)
    Book(
        title="Outlander",
        author="Diana Gabaldon",
        genre="Romance",
        description="A World War II nurse is transported to 18th-century Scotland.",
        year_published=1991,
        isbn="978-0-440-21256-0"
    ),
    Book(
        title="The Notebook",
        author="Nicholas Sparks",
        genre="Romance",
        description="A young man and woman fall in love during the 1940s.",
        year_published=1996,
        isbn="978-0-446-71143-8"
    ),
    Book(
        title="Me Before You",
        author="Jojo Moyes",
        genre="Romance",
        description="A young woman becomes caregiver to a paralyzed man and changes his life.",
        year_published=2012,
        isbn="978-0-14-312454-0"
    ),
    Book(
        title="The Fault in Our Stars",
        author="John Green",
        genre="Romance",
        description="Two teenagers with cancer fall in love and face mortality together.",
        year_published=2012,
        isbn="978-0-525-47881-2"
    ),
    Book(
        title="Twilight",
        author="Stephenie Meyer",
        genre="Romance",
        description="A teenage girl falls in love with a vampire and enters a dangerous world.",
        year_published=2005,
        isbn="978-0-316-16017-3"
    ),
    Book(
        title="Gone with the Wind",
        author="Margaret Mitchell",
        genre="Romance",
        description="A Southern belle fights to survive during the American Civil War.",
        year_published=1936,
        isbn="978-0-684-82420-6"
    ),
    Book(
        title="The Love Hypothesis",
        author="Ali Hazelwood",
        genre="Romance",
        description="A PhD student fakes a relationship with a professor to prove a point.",
        year_published=2021,
        isbn="978-0-593-41293-2"
    ),
    Book(
        title="Normal People",
        author="Sally Rooney",
        genre="Romance",
        description="Two young people from different backgrounds navigate love and life.",
        year_published=2018,
        isbn="978-1-9848-2218-5"
    ),
    
    # Horror (6 books)
    Book(
        title="The Shining",
        author="Stephen King",
        genre="Horror",
        description="A family's winter stay at an isolated hotel turns terrifying.",
        year_published=1977,
        isbn="978-0-385-12167-5"
    ),
    Book(
        title="Dracula",
        author="Bram Stoker",
        genre="Horror",
        description="The legendary vampire Count Dracula's terrifying journey to England.",
        year_published=1897,
        isbn="978-0-14-143984-6"
    ),
    Book(
        title="Frankenstein",
        author="Mary Shelley",
        genre="Horror",
        description="A scientist creates a creature that becomes a monster.",
        year_published=1818,
        isbn="978-0-14-313451-3"
    ),
    Book(
        title="The Haunting of Hill House",
        author="Shirley Jackson",
        genre="Horror",
        description="A group of investigators explores a haunted mansion.",
        year_published=1959,
        isbn="978-0-14-312235-9"
    ),
    Book(
        title="It",
        author="Stephen King",
        genre="Horror",
        description="A group of friends confronts a shape-shifting creature in their hometown.",
        year_published=1986,
        isbn="978-0-451-21155-6"
    ),
    Book(
        title="The Exorcist",
        author="William Peter Blatty",
        genre="Horror",
        description="A young girl is possessed by a demon and priests try to save her.",
        year_published=1971,
        isbn="978-0-06-265337-6"
    ),
    
    # Non-Fiction (6 books)
    Book(
        title="Sapiens",
        author="Yuval Noah Harari",
        genre="Non-Fiction",
        description="A brief history of humankind from the Stone Age to the present.",
        year_published=2011,
        isbn="978-0-06-231609-7"
    ),
    Book(
        title="The Diary of a Young Girl",
        author="Anne Frank",
        genre="Non-Fiction",
        description="The diary of a Jewish girl hiding from the Nazis during World War II.",
        year_published=1947,
        isbn="978-0-553-57712-9"
    ),
    Book(
        title="Becoming",
        author="Michelle Obama",
        genre="Non-Fiction",
        description="The memoir of the former First Lady of the United States.",
        year_published=2018,
        isbn="978-1-5247-6313-8"
    ),
    Book(
        title="The Art of War",
        author="Sun Tzu",
        genre="Non-Fiction",
        description="An ancient Chinese military treatise on strategy and tactics.",
        year_published=500,
        isbn="978-1-59030-225-9"
    ),
    Book(
        title="The Immortal Life of Henrietta Lacks",
        author="Rebecca Skloot",
        genre="Non-Fiction",
        description="The story of a woman whose cells became one of the most important medical discoveries.",
        year_published=2010,
        isbn="978-1-4000-5217-2"
    ),
    Book(
        title="The Power of Habit",
        author="Charles Duhigg",
        genre="Non-Fiction",
        description="Why we do what we do and how to change habits.",
        year_published=2012,
        isbn="978-0-8129-8160-5"
    )
]

with app.app_context():
    # Clear existing books
    db.session.query(Book).delete()
    db.session.commit()
    
    # Add new books
    for book in sample_books:
        db.session.add(book)
    db.session.commit()
    print(f"✅ {len(sample_books)} sample books added successfully!")