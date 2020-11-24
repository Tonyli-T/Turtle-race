import turtle
import random
from playsound import playsound

# Code intended to record player's sound and apply into the game.
# Apparently, we failed to do that
# ---------------------------------------------------
# import sounddevice as sd
# from scipy.io.wavfile import write
#
# # Recording turtle sound
# fs = 44100
# seconds = 3
#
# my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
# sd.wait()
# write('output.wav', fs, my_recording)
#
# playsound('output.wav')
# ---------------------------------------------------


# A method that initializes two turtles
def init(p, color, x, y):
    p.shape("arrow")
    p.color(color)
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.circle(50)
    p.penup()
    p.goto(x - 50, y + 50)
    p.pendown()

    for index in range(15):
        p.bk(50)
        p.stamp()
    p.penup()


# Setting up the environment
s = turtle.Screen()
s.setup(width=1300, height=1000)
s.bgcolor("pink")
s.title("Welcome to the ultimate turtle tournament")

# Initial setup for player 1
p1 = turtle.Turtle()
init(p1, "blue", 300, 100)

# Initial setup for player 2
p2 = turtle.Turtle()
init(p2, "red", 300, -100)

p1.shape("turtle")
p2.shape("turtle")

# Making the dice
die = [1, 2, 3, 4]
die2 = [-6, 8, -4, 2]

i = 1
while i != 0:
    # Player 1's turn
    print("Hello, player1")
    o = input('Press x to roll the regular dice with special die, but be careful it might help you or destroy you ')

    if o == 'x':
        die_outcome_2 = random.choice(die2)

    die_outcome = random.choice(die)
    print("The result of your die roll is: ")

    if o == 'x':
        print(die_outcome + die_outcome_2)
        p1.fd((die_outcome + die_outcome_2) * 50)
        playsound('move.mp3')
    else:
        print(die_outcome)
        p1.fd(die_outcome * 50)
        playsound('move.mp3')

    if p1.pos() >= (300, 0):
        print("Player One Wins!")
        playsound("Sample1.mp3")
        break

    # Player 2's turn
    print("Hello, player2")
    o = input('Press x to roll the regular dice with special die, but be careful it might help you or destroy you ')

    if o == 'x':
        die_outcome_2 = random.choice(die2)

    die_outcome = random.choice(die)
    print("The result of your die roll is: ")

    if o == 'x':
        print(die_outcome + die_outcome_2)
        p2.fd((die_outcome + die_outcome_2) * 50)
        playsound('move.mp3')
    else:
        print(die_outcome)
        p2.fd(die_outcome * 50)
        playsound('move.mp3')

    if p2.pos() >= (300, 0):
        print("Player Two Wins!")
        playsound("Sample1.mp3")
        break
