import  re
import linkGrabber

links = linkGrabber.Links("http://www.brotherprog.cf")
gb = links.find(limit=5 , duplicates=False , pretty=True)
print(gb)

