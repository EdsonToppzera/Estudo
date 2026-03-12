import re
import sys


def main():
    print(parse(input("HTML: ")))

#<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0"...
#<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

def parse(s):
    if matches := re.search(r'^.+src="https?://(?:www\.)?youtube.com/embed/([a-z0-9]+)".+$', s, re.IGNORECASE):
        return(f"https://youtu.be/{matches.group(1)}")
    else:
        return(None)

if __name__ == "__main__":
    main()
