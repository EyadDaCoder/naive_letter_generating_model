# The actual AI which does the thinking

import random
from dataset import dataset
import weights
import launcher

class naive_word_generating_model:
    def __init__(self):

        self.letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        self.i = 0
        self.accuracy = 0
        self.word_l1 = ['', '', '', '']
        self.word_l2 = ['', '', '', '']
        self.vacant_letter_positions = [0, 1, 2, 3]
        self.generated_word = ""
        self.generated_position = 0
        self.positional_weights_adjusted = []
        self.diff = []
        self.diff_count = 0
        self.gen_word_to_dataset_word_diff = []

    def generate(self):
        # Reset essential variables
        self.generated_word = ""
        self.vacant_letter_positions = [0, 1, 2, 3]
        self.word_l2 = ['', '', '', '']
        self.i = 0

        self.word_l1 = random.choices(self.letters, weights=weights.GLOBAL, k=4) # generate the random letters

        self.positional_weights_adjusted = weights.POSITIONAL
        while self.i != 4:
            self.generated_position = random.choices(self.vacant_letter_positions, weights=self.positional_weights_adjusted)
            self.word_l2[self.generated_position] = self.word_l1[self.i]
            self.vacant_letter_positions.remove(self.generated_position)
            self.positional_weights_adjusted[self.word_l1[self.i]].remove(self.generated_position)
            self.i += 1
        self.generated_word = ''.join(self.word_l2)
        return self.generated_word

    def feedback(self, generated_word):
        self.gen_word_to_dataset_word_diff = []
        for x in dataset:
            self.diff = list(zip(generated_word, x)) # create a side by side of the letters in every dataset word and the generated word.
            self.diff_count = 0
            for y in self.diff: # compare the side by side
                if y[0] == y[1]:
                    self.diff_count += 1
            self.gen_word_to_dataset_word_diff.append(self.diff_count)
        dataset_word = dataset[max(self.gen_word_to_dataset_word_diff)]
        self.diff = list(zip(generated_word, dataset_word)) # create a side by side of the letters in the dataset word and the generated word.
        self.i = 0
        y = 0 # this variable is how much the word got a letter in the correct position
        for x in self.diff: #
            if x[0] == x[1]:
                weights.POSITIONAL[x[0]][self.i] += 0.25
                weights.GLOBAL[self.letters.index(x[0])] += 0.25
                y += 1
            self.i += 1
        if y == 0: # the ai does not want this condition to be true, because that means the word was completely wrong, and every letter and its position will get penalized
            self.i = 0
            for z in generated_word:
                if weights.POSITIONAL[z][self.i] > 0.00 and weights.GLOBAL[self.letters.index(z)] > 0.00 :
                    weights.POSITIONAL[z][self.i] -= 0.25
                    weights.GLOBAL[self.letters.index(z)] -= 0.25
                else:
                    weights.POSITIONAL[z][self.i] += 0.05
                    weights.GLOBAL[self.letters.index(z)] += 0.05
                self.i += 1


ai = naive_word_generating_model()