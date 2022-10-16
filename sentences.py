import random
def welcome():
    stop_signal = False
    who_from_where(names, places)
    action(adverbs, verbs, nouns)
    detail(details)
    print("Welcome to the Random Sentence Generator")
    print('This will be your first sentence.')
    print(*sentences)
    continue_or_not = input('If you wish to continue type: NEW\n otherwise to stop the program type: STOP').lower()
    if continue_or_not == 'stop':
        stop_signal = True
    while True:
        print(*sentences)
        continue_or_not = input('If you wish to continue type: NEW\n otherwise to stop the program type: STOP').lower()
        if continue_or_not == 'stop':
            stop_signal = True
            break
    if continue_or_not:
        print('Thank you for using my little program.')
        print('Made by Borislav')
def who_from_where(name, place):
    random_name = random.choice(name)
    random_place = random.choice(place)
    sentence = f'{random_name} from {random_place}'
    sentences.append(sentence)
    return sentences

def action(adverb, verb, noun):
    random_adverb = random.choice(adverb)
    random_verb = random.choice(verb)
    random_noun = random.choice(noun)
    sentece = f'{random_adverb} {random_verb} {random_noun}'
    sentences.append(sentece)
    return sentences

def detail(detail):
    random_detail = random.choice(detail)
    sentences.append(random_detail)
    return sentences


sentences = []
names = ['Haralampi', 'Ivan', 'Gosho', 'Pesho']
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

welcome()
