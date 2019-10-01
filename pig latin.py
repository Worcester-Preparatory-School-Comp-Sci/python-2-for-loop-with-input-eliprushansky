#ELI PRUSHANSKY 270919
def pigLatin():
    x = input("what word?")
    changedConsonant = x[1:]+x[0]+"ay"
    changedVowel = x[0:]+"way"
    vowels = ["a","e","i","o","u"]
    if x[0] in vowels[0:4]: #no need to select the index values ... just say in vowels:
        print(changedVowel)
    else:
        print(changedConsonant)

pigLatin()
    
    
    
