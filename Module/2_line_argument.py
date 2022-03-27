import sys
from urllib.request import urlopen


def fetch_words():
    story = urlopen("http://sixty-nort.com/c/t.txt")
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_words(story_words):
    for word in story_words:
        print(word)


def main():
    words = fetch_words()
    print(words)


if __name__ == "__main__":
    main(sys.argv[1])
