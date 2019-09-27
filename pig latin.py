def pigLatin():
    x = input("what word?")
    changedConsonant = x[1:]+x[0]+"ay"
    changedVowel = x[0:]+"way"
    vowels = ["a","e","i","o","u"]
    if x[0] in vowels[0:4]:
        print(changedVowel)
    else:
        print(changedConsonant)

pigLatin()
    
    
    
