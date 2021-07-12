sports = ["swimming", "climbing", "running", "cycling"]

print(sports)

print(sports[3])

print(sports[2])

message = f"I love to compete in sports, my favourite is {sports[1].title()}"

print(message)

sports.append("wrestling")

sports.append("basketball")

sports.append("skateboarding")

print(sports)

sports.insert(1, "sky diving")

print(sports)

print(sports.index("climbing"))

popped_sports = sports.pop()

print(sports)

print(popped_sports)

print(sorted(sports, reverse=True))

print(len(sports))