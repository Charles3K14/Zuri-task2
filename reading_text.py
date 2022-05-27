# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    file=open(filename)
    contents=file.read()
    return contents
    

def count_words():
    text = read_file_content("./story.txt")
    new_text=text.replace('.','').replace(',','').replace('?','')
    # [assignment] Add your code here
    my_dict={}
    for word in new_text.split():
        if word not in my_dict:
            my_dict[word]=1
        else:
            my_dict[word]+=1
    return my_dict

print(read_file_content("story.txt"))

print(count_words())
