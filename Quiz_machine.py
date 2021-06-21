


class Word():
    def __init__(self, new_word, example1, example2, x):
        self.new_word = new_word
        self.example1 = example1
        self.example2 = example2
        self.x = x
    def show_question(self):
        print("\"{0}\"의 뜻은?".format(self.new_word))
        print("1. {0}".format(self.example1))
        print("2. {0}".format(self.example2))

    def check_answer(self, user_input):
        if user_input == self.x:
            print("정답입니다")
        else:
            print("틀렸습니다.")

word = Word("얼죽아", "얼어 죽어도 아메리카노", "얼굴만은 죽어도 아기피부", 1)
word.show_question()
word.check_answer(int(input("=> ")))