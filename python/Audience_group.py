audience_group = 'kid', 'teen', 'adult'

audience = input("plese enter are you kid or teen or adult")

if audience in audience_group:
    if audience == "kid":
        print("it is free to go to cinema")
    elif audience == "teen":
        print("discounted price!")
    else: # audience == "adult":
        print("normal price")
else:
    print("No such audience, stay at your home!")