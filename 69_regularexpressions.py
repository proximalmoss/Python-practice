#no need to use regular expression for basic matching you can use in or for lopp
import re
pattern=r"[A-Z]+yclone"
text='''
In meteorology, a Cyclone (/ˈsaɪ.kloʊn/) is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Cyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones and subtropical cyclones also lie within the synoptic scale.[5] Mesocyclones, tornadoes, and dust devils lie within the smaller mesoscale.[6]
'''
#now we want to find if was is there in the text
match=re.search(pattern,text)
print(match)
#re.search stops after the first match
#now i want all occurances so
matches=re.finditer(pattern,text)
for match in matches:
    print(match)
    print(match.span()) #to get index of where it appears
    #now to get the word
    print(text[match.span()[0]:match.span()[1]])