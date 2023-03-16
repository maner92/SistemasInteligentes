import numpy as np

class linealRegression():
    def _init_(self):
        self.thetas = np.asarray([])
        
    def target_function(self, x):
        return self.thetas[0]*x
    
    def fit(self, features, target, learning_rate=0.1, max_iter=100):
        n_features = 1
        n_examples = features.shape[0]
        self.thetas = np.random.rand(n_features)
        slipt_ponit = int(n_examples * 0.8)
        x_training = features[:slipt_ponit]      
        x_validate = features[:-slipt_ponit]
        target_training = target[:slipt_ponit]
        target_validate = target[:-slipt_ponit]
        
        print("El valor inicial de theta es: "+ str(self.thetas[0]))
        
        for i in range(max_iter):
            sum_ = 0
            for i,x in enumerate(x_training):
                sum_ = sum_ + (self.target_function(x) - target_training[i]**2)
            temp_0 = self.thetas[0] - (learning_rate * (1/n_examples)*(sum_))
            self.thetas[0] = temp_0
            print("El nuevo valor de theta es: "+ str(self.thetas[0]))
            
        y_predicted = []
        for x in x_validate:
            y_predicted.append(self.target_function(x))
            return (y_predicted, x_validate, target_validate)
            
        
    def mean_error(self):
        pass
    
    def predict(self, x):
        return self.thetas[0]*x
    
    