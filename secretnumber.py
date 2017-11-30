print 'hello'

secret = 37
guess = -5

n_guesses = 0

while guess != secret and n_guesses < 5:

    guess = raw_input('Enter you guess:')
    guess = int(guess)

    if guess == secret:
        print 'Your guess was correct!'
    elif guess < secret:
        print 'Your guess was too low'
        difference = secret - guess
        print 'you are off by', difference
    else:
        print 'Your guess was to high'
        difference = guess - secret
        print 'you are off by', difference

    n_guesses += 1

print 'End'