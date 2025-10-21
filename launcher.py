# This file handles launching the model, providing info and providing a config menu.
import dataset
import weights
import model

cmd_list = ['start', 'config', 'info']

config = {
    'iterations': 1,
    'freeze_training': False,
    'reset_weights': True,
    'feed_forward_weights': False,
    'version': '1.0.0'
}
print(model.__file__)
print("Naive Letter Generating Model 1.0.0")
print("This file isn't fully implemented so its just gonna start lol")
ai = model.naive_word_generating_model()
i = 0
while i != config['iterations']:
    ai.feedback(ai.generate())
    i += 1
