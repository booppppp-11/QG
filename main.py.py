from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

class QuestionGameApp(App):
    def build(self):
        self.title = 'Question Game'
        self.score = 0
        self.current_question = 0
        self.playing = False
        self.difficulty_selected = False

        self.main_layout = BoxLayout(orientation='vertical')

        self.difficulty_label = Label(text='Select a difficulty level:')
        self.main_layout.add_widget(self.difficulty_label)

        self.easy_button = Button(text='Easy', on_press=self.start_game)
        self.hard_button = Button(text='Hard', on_press=self.start_hard_game)
        self.extreme_button = Button(text='Extreme', on_press=self.start_extreme_game)

        self.main_layout.add_widget(self.easy_button)
        self.main_layout.add_widget(self.hard_button)
        self.main_layout.add_widget(self.extreme_button)

        return self.main_layout

    def start_game(self, instance):
        self.reset_game()
        self.difficulty_selected = True
        self.playing = True
        self.question_set = random.sample(easy_questions, k=8)
        self.main_layout.clear_widgets()
        self.display_next_question()

    def start_hard_game(self, instance):
        if self.score >= 5:
            self.reset_game()
            self.playing = True
            self.question_set = random.sample(hard_questions, k=8)
            self.main_layout.clear_widgets()
            self.display_next_question()

    def start_extreme_game(self, instance):
        if self.score >= 5:
            self.reset_game()
            self.playing = True
            self.question_set = random.sample(extreme_questions, k=8)
            self.main_layout.clear_widgets()
            self.display_next_question()

    def display_next_question(self):
        if self.playing and self.current_question < len(self.question_set):
            question, answer = self.question_set[self.current_question]
            self.current_question += 1

            self.question_label = Label(text=question)
            self.user_answer_input = TextInput(hint_text='Your Answer')
            self.submit_button = Button(text='Submit', on_press=self.check_answer)

            self.main_layout.add_widget(self.question_label)
            self.main_layout.add_widget(self.user_answer_input)
            self.main_layout.add_widget(self.submit_button)
        elif self.playing:
            self.display_score()
            self.playing = False
            self.difficulty_selected = False

            if self.score >= 5:
                self.main_layout.add_widget(Button(text='Play Hard', on_press=self.start_hard_game))
                self.main_layout.add_widget(Button(text='Play Extreme', on_press=self.start_extreme_game))
            else:
                self.main_layout.add_widget(Button(text='Play Again', on_press=self.start_game))

    def check_answer(self, instance):
        user_answer = self.user_answer_input.text.lower().strip()
        correct_answer = self.question_set[self.current_question - 1][1].lower().strip()

        if user_answer == correct_answer:
            self.score += 1

        self.main_layout.clear_widgets()
        self.display_next_question()

    def display_score(self):
        self.score_label = Label(text=f'Your score is: {self.score}')
        self.main_layout.add_widget(self.score_label)

    def reset_game(self):
        self.current_question = 0
        self.score = 0
        self.playing = False
        self.difficulty_selected = False

easy_questions = [
    ("What is the capital of France?", "Paris"),
    ("Which planet is closest to the Sun?", "Mercury"),
    ("What is the largest mammal on Earth?", "Blue Whale"),
    ("How many continents are there on Earth?", "Seven"),
    ("What is the chemical symbol for oxygen?", "O"),
    ("Who wrote the novel 'To Kill a Mockingbird'?", "Harper Lee"),
    ("What gas do plants absorb from the atmosphere?", "Carbon Dioxide"),
    ("What is the currency of Japan?", "Yen"),
]

hard_questions = [
    ("What is the capital of Australia?", "Canberra"),
    ("Which gas is responsible for the color of Earth's sky?", "Nitrogen"),
    ("What is the smallest prime number?", "Two"),
    ("Which planet is known as the 'Red Planet'?", "Mars"),
    ("What is the chemical symbol for the element silver?", "Ag"),
    ("Who wrote the play 'Hamlet'?", "William Shakespeare"),
    ("What is the process by which plants make their own food?", "Photosynthesis"),
    ("What is the currency of Brazil?", "Real"),
]

extreme_questions = [
    ("What is the capital of Mongolia?", "Ulaanbaatar"),
    ("Which gas is known as 'laughing gas'?", "Nitrous Oxide"),
    ("What is the largest prime number less than 100?", "97"),
    ("Which planet has the highest surface temperature?", "Venus"),
    ("What is the chemical symbol for the element uranium?", "U"),
    ("Who wrote the novel 1984?", "George Orwell"),
]
if __name__ == '__main__':
    QuestionGameApp().run()