class Character:
    def __init__(
        self,
        title: str,
        name: str,
        power_score: int,
        biography: str
    ):
        self.title = title
        self.name = name
        self.power_score = power_score
        self.biography = biography

    @property
    def full_name(self) -> str:
        return f'{self.title} {self.name}'

    @property
    def data(self) -> str:
        return (
            f'{self.title} {self.name} | Power score - {self.power_score} -\n'
            f'{self.biography}'
        )


def ascii_artx():
    # Y(Height) of ascii-art
    z = 12
    for x in range(z):

        hyphens = "_" * (z-x)
        print(hyphens + "::" * x + hyphens)

def ascii_art():
    # Y(Height) of ascii-art
    z = 12
    for x in range(z):

        hyphens = "~~" * (z-x)
        print("" * x + " " * x + hyphens)


def input_yesno(prompt: str) -> bool:
    full_prompt = f'{prompt} ([Yes]/No): '
    while True:
        answer = input(full_prompt).strip()
        if answer == '':
            return True

        answer = answer[0].lower()
        if answer == 'y':
            return True
        if answer == 'n':
            return False
        print('ERROR')


def main():
    ascii_artx()
    ascii_art()
    if not input_yesno('Are you ready to play'):
        return

    is_hero = input_yesno('Do you want to be a Hero')
    print('\nYou have selected', end=' ')
    if is_hero:
        print('to be a hero')
        character = Character('Barbarian', 'Cider', 4854, 'Not much is known about this character')
    else:
        print('not to be a hero')
        character = Character('Lord', 'Cido', 7910, 'Not much is known about this character')

    print("\nYour character's profile:")
    print(character.data)


if __name__ == '__main__':
    main()







# class Character:
#     def __init__(
#         self,
#         title: str,
#         name: str,
#         power_score: int,
#         biography: str
#     ):
#         self.title = title
#         self.name = name
#         self.power_score = power_score
#         self.biography = biography

#     @property
#     def full_name(self) -> str:
#         return f'{self.title} {self.name}'

#     @property
#     def data(self) -> str:
#         return (
#             f'{self.title} {self.name} | Power score - {self.power_score} -\n'
#             f'{self.biography}'
#         )


# def ascii_art():
#     # Y(Height) of ascii-art
#     z = 12
#     for x in range(z):
#         hyphens = "-" * (z-x)
#         print(hyphens + "*" * x + " " * x + hyphens)


# def input_yesno(prompt: str) -> bool:
#     full_prompt = f'{prompt} ([Yes]/No): '
#     while True:
#         answer = input(full_prompt).strip()
#         if answer == '':
#             return True

#         answer = answer[0].lower()
#         if answer == 'y':
#             return True
#         if answer == 'n':
#             return False
#         print('ERROR')


# def main():
#     ascii_art()
#     if not input_yesno('Are you ready to play'):
#         return

#     is_hero = input_yesno('Do you want to be a Hero')
#     print('\nYou have selected', end=' ')
#     if is_hero:
#         print('to be a hero')
#         character = Character('Barbarian', 'Cider', 4854, 'Not much is known about this character')
#     else:
#         print('not to be a hero')
#         character = Character('Lord', 'Cido', 7910, 'Not much is known about this character')

#     print("\nYour character's profile:")
#     print(character.data)


# if __name__ == '__main__':
#     main()



# class characters:

#     def __init__(self, title, character_name, power_score, biography):
#         self.title = title
#         self.character_name = character_name
#         self.power_score = '| ' + 'Power score - ' + power_score + ' -\n'
#         self.biography = biography

#     def title_name(self):
#         print('{} {}'.format(self.title,self.character_name))

#     def characters_data(self):
#         print('{} {} {} {}'.format(self.title, self.character_name, self.power_score, self.biography))

#     def characters_vm(self):
#         print('{} {}\n {}'.format(self.title, self.character_name, self.biography))


# B_Cider = characters('Barbarian', 'Cider', '4854', 'Not much is known about this character')
# L_Cido = characters('Lord', 'Cido', '7910', 'Not much is known about this character' )
# N_Grandmaster = characters('New', 'Grandmaster', '999999999999999', 'The more i know about the past the futher I can see in future' )
# T_Universe = characters('The', 'Universe', '999999999999999', 'Space and time and their contents, including planets, stars, galaxies, and all other forms of matter and energy.')

# # Y(Height) of ascii-art
# z = 12
# print("\n-Aventure Game-\n")
# for x in range(z):
#     print("-" * (z-x) + "*" * x + " " * x + "-" * (z-x))
# # ...............

# answer = input('Are you ready to play? (Yes/No or Enter) : ').lower().strip()
# first_selection = "Do you want to be a Hero? (Yes/No or Enter) : "
# not_Ahero = "\nYou have selected not to be a hero\n____\nYour characters profile:"
# Ahero = "\nYou have selected to be a hero\n____\nYour characters profile:"
# error = 'ERROR'
# yesAnswers = {'yes', 'y', 'sure!', 'yea', 'yeah', 'ye', 'si', ''}
# noAnswers = {'no', 'n', 'nope', 'nah', 'not'}
# Answers_Attack = {'attack', 'att', 'a', 'ack', 'atck', 'atk', 'tt', 'k'}
# Answers_Talk = {'talk', 't', 'a', 'tak', 'speak', 'hello', 'hi', 'hey'}
# Answers_Who = {'who', 'are', 'who are you', 'what', 'do I know you?', 'who are you?', '?', 'hey'}
# Answers_Space = {'space', 'universe', 'life', 'galaxy', 'what is it?', 'where?', 'why', 'new'}

# if answer in yesAnswers:
#     answer = input(first_selection).lower().strip()
#     if answer in yesAnswers:
#         print(Ahero)
#         print('____'.format(characters.characters_data(B_Cider)))
#         answer = input('\nYou have encountered a Friendly enemy\n (Attack/Talk) :').lower().strip()
#         if answer in Answers_Attack:
#             print('-999999999 damage')
#             print('Game Over')
#         elif answer in Answers_Talk:
#             print('Greetings,')
#             print('So about what would you like talk?'.format(characters.title_name(B_Cider)))
#             answer = input('\n____\n:').lower().strip()
#         if answer in Answers_Who:
#             print("I'm just a traveler".format(characters.characters_data(N_Grandmaster)))
#         elif answer in Answers_Space:
#             print(''.format(characters.characters_vm(T_Universe)))
#     if answer in noAnswers:
#         print(not_Ahero)
#         print('____'.format(characters.characters_data(L_Cido)))
#         answer = input('\nYou have encountered a Friend\n (Attack/Talk):' ).lower().strip()
#         if answer in Answers_Attack:
#             print('-7910 damage')
#             print("Game Over")
#         elif answer in Answers_Talk:
#             print("How's it going?")
#             print(''.format(characters.title_name(B_Cider)))
#             answer = input('\n:').lower().strip()
#         if answer in Answers_Space:
#             print(''.format(characters.characters_vm(T_Universe)))
# else:
#     print(error)
