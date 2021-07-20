alien_0 = {'colour' : 'green', 'points' : 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}


print(alien_0['colour'])
print(alien_0['points'])

print(alien_0)

alien_0['x_pisition'] = 0
alien_0['y_position'] = 25

print(alien_0)

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

