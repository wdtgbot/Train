from os.path import abspath, dirname
if ":" in dirname(abspath(__file__)):
    print(True)
else:
    print(False)
    