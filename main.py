import time

def test():

    prompt = "The Solar System consists of the Sun Moon and Planets. "

    print("Hello!!!!! Welcome to the speed typing Test.!!!!!!!!!!!!!!!!!")

    print("You have to type the following sentence as fast as you can-------------->")

    print(prompt)

    input("Press Enter to Start !!!!!!!!!!")

    startingtime = time.time()

    usersinput = input()

    endtime = time.time()

    elapsedtime = endtime - startingtime

    wordsstyped = len(usersinput.split())

    speed = wordsstyped / elapsedtime

    accuracy = c_accuracy(usersinput, prompt)

    print("Results:")

    print("Time elapsed-------------------> {:.2f} seconds".format(elapsedtime))

    print("Words typed--------------------> {}".format(wordsstyped))

    print("Speed--------------------------> {:.2f} words per second".format(speed))

    print("Accuracy-----------------------> {:.2f}%".format(accuracy * 100))

def c_accuracy(usersinput, prompt):

    promptwords = prompt.split()

    userswords = usersinput.split()

    correctwords = 0

    for promptword, userword in zip(promptwords, userswords):

        if promptword == userword:

            correctwords += 1

    accuracy = correctwords / len(promptwords)

    return accuracy

test()
