myPets = ['me', 'mu', 'ma']
print('who are you looking for?')
name = input()
if name not in myPets:
    print('sorry, I don\'t have a pet named ' + name)
else:
    print('yeah, I found ' + name + '. Here you go!')
