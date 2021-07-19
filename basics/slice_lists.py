invites = ['richie', 'kathryn', 'tony', 'lewis', 'disco', 'jenny']

print(invites[1:3])

print(invites[:4])

print(invites[2:])

print(invites[-3:])

print("Here's my top 3 peeps:")
for peeps in invites[:3]:
    print(peeps.title())
