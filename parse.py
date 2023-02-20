import os
import sys


def run():
    # SECTION 1 CWD

    Path = os.getcwd()

    CurrentWorkingDirectory = os.getcwd()

    os.chdir('code')


    NewWorkingDirectory = os.getcwd()



    #print(NewWorkingDirectory)
    sys.path.append(Path + '/code')
    import main

    game = main.Game()

    game.run()


