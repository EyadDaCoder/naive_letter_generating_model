# This file handles launching the model, providing info and providing a config menu.
import dataset
import weights
import model

cmd_list = ['start', 'config', 'info']

config = {
    'iterations': 100000,
    'freeze_training': False,
    'reset_weights': True,
    'feed_forward_weights': False
}

def main():
    global cmd_list, config

    print("Naive Letter Generating Model 1.0.0")
    print("This file isn't fully implemented so its just gonna start lol")
    i = 0
    while i != config['iterations']:
        model.ai.run()
        model.ai.feedback()
        i += 1