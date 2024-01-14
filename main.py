userName = input("What is your name?: ")
holes = int(input("Would you like to play 3 or 6 holes?: "))
strokes = [0] * int(holes)
score = 0
par = 3 * holes

for s in strokes:
    strokes[strokes.index(s)] = int(input(f"How many putts for hole {strokes.index(s)+1}?: "))

score = sum(strokes)
if score < par:
    print(f"Great job, {userName}! Your total score was: -{par - score}.")
elif score > par:
    print(f"Nice try, {userName}... Your total score was: +{score - par}.")
else:
    print(f"Good game, {userName}. Your total score was: {par - score}.")

print(strokes)
#print(score)