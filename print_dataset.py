import pickle

# Replace 'your_file.pkl' with the path to your .pkl file
with open('Dataset/English_sentences.pkl', 'rb') as file:
    data = pickle.load(file)

# Print or inspect the data
print(data)