import os
import torch
from fastai.learner import load_learner

class ModelInference:
    def __init__(self, model_filename):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(base_dir, model_filename)
        self.model = load_learner(model_path)

    # def predict(self, input_data):
    #     # Preprocess your input_data if necessary
    #     # ...
        
    #     # Make a prediction
    #     prediction = self.model.predict(input_data)
        
    #     # Postprocess your prediction if necessary
    #     # ...
        
    #     return prediction
    
    def predict(self, input_data):
    # Preprocess your input_data if necessary
    # ...

    # Make a prediction
        pred, pred_idx, probs = self.model.predict(input_data)

        # Postprocess your prediction if necessary
        # ...

        # Sort the probabilities in descending order
        sorted_probs = sorted(zip(self.model.dls.vocab, probs.tolist()), key=lambda x: x[1], reverse=True)

        return sorted_probs


model = ModelInference('model.pkl')
