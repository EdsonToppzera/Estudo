import random
import sys


def main():
    level = get_level()

    respostas_temp = []
    questao_temp = []
    score = []
    while True:
        if len(score) < 10:
            if len(questao_temp) == 0:
                x = (generate_integer(level))
                y = (generate_integer(level))

                resposta = input(f"{x} + {y} = ")
                respostas_temp.append(resposta)
                questao_temp.append(f"{x} + {y} = ")

            else:
                for i in respostas_temp[-1:]:
                    if len(respostas_temp) < 3:

                        if i.isnumeric() == True and int(i) == int(x+y):
                            score.append(1)
                            questao_temp.clear()
                            respostas_temp.clear()
                            break
                        else:
                            print("EEE")
                            q = input(*questao_temp[0:1])
                            respostas_temp.append(q)
                            continue
                    else:
                        print("EEE")
                        print(*questao_temp[0:1],int(x+y))
                        questao_temp.clear()
                        respostas_temp.clear()
                        score.append(0)
                        continue
        else:
            print("Score: "+str(sum(score)))
            sys.exit(0)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break

        except:
            pass
    return level

def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)

if __name__ == "__main__":
    main()
