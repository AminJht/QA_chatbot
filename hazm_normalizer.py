from hazm import Normalizer

class NormalizerFarsi:
    def __init__(self):
        self.normalizer = Normalizer()

    def h_normalizer(self, prompt:str):
        if not prompt or not isinstance(prompt, str):
            return "it is null"
        normalized_text = self.normalizer.normalize(prompt)
        
        return normalized_text
    
