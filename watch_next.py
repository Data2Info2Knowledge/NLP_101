import spacy
nlp = spacy.load('en_core_web_md')

# Function to return recommended based on most similar description
def recommend(desc, cleanup=False):
    nlp_desc = nlp(desc)
    # calculate description similarity for each movie in list
    for movie in movies:
        this_desc = movie[1]
        doc = nlp(this_desc)
        if cleanup:
            clean_list =[token.orth_ for token in doc 
                         if not (token.is_punct | token.is_space)]
            doc = nlp(" ".join(clean_list))
        similarity = doc.similarity(nlp_desc)
        movie.append(similarity)    
    movies.sort(key=lambda x:x[2], reverse=True) # sort by decreasing similarity
    return movies[0][0] # title of top movie in list

movies = []
cleanup = False
try:
    with open('movies.txt', 'r', encoding='utf-8-sig') as f:
        for line in f.readlines():
            details = line.strip("\n").split(" :")
            movies.append(details) # details[0] is title, details[1] is summary
except:
    print("Error reading input file.")

desc = "Will he save their world or destroy it? When the Hulk becomes too \
    dangerous for the Earth, the Illuminati trick Hulk into a shuttle and \
    launch him into space to a planet where the Hulk can live in peace. \
    Unfortunately, Hulk lands on the planet Sakaar where he is sold into \
    slavery and trained as a gladiator."

rm_stop = input("Eliminate 'stop words' and punctuation from film summaries (Y/N)?").upper()
if rm_stop == "Y": cleanup = True
    
print(f"We recommend you watch {recommend(desc, cleanup)} next.")
tell_more = input("Would you like an idea of\
 how we came up with this recommendation (Y/N)?").upper()
if tell_more == "Y":
    print("Title \t Similarity \t Summary")
    for movie in movies:
        print(f"{movie[0]} \t {movie[2]: .3f} \t {movie[1][:80]}...")