import sys

def load(file):
    """
        Opens our file of words
    """
    try:
        with open(file) as f:
            dictionary = f.read().strip().split('\n')
            dictionary = [x.lower() for x in dictionary]
        return dictionary
    except IOError as e:
        print(f"{e}\n Error opening {e}. Stopping...", file=sys.stderr)
        sys.exit(1)