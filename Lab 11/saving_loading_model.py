import pickle

# assume you already trained a model
# model = your trained ML model

# Save the model
with open('model_pickle.pkl', 'wb') as file:
    pickle.dump(model, file)


# Load the saved model
with open('model_pickle.pkl', 'rb') as file:
    model = pickle.load(file)