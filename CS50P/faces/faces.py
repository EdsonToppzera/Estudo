#converts emoticons to emotes
def convert(to):
    to = to.replace(":)", "🙂")
    to = to.replace(":(", "🙁")
    print(to)

def main():
    faces = input()
    convert(faces)

main()
