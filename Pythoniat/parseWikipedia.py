import wikipedia
#wikipedia.set_lang("ar")
#wikipedia.set_lang("fr")
wiki = wikipedia.summary("facebook" , sentences=1)
print(wiki)

# wiki = wikipedia.search("keyword" )
