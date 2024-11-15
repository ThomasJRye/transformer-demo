# print_english_dataset.py
import torch
from Dataset.translation_dataset import EnglishToGermanDataset
  # Ensure this matches the filename of your dataset class definition

def main():
    # Initialize the dataset (set CUDA to False for simplicity)
    dataset = EnglishToGermanDataset(CUDA=False)
    
    # Set the mode to train (or test, depending on what you want to print)
    dataset.train()  # Use dataset.test() if you want to print the test data
    
    print("len(dataset):", len(dataset))
    # Print a portion of the English dataset
    print("Printing English sentences from the dataset:")
    for idx in range(min(3, len(dataset))):  # Adjust the range as needed
        data_item = dataset[idx]
        english_sentence = data_item['english']
        
        # Convert the tensor to a sentence using the reversed vocabulary
        sentence_text = " ".join([dataset.english_vocab_reversed[token.item()] for token in english_sentence])
        
        print(f"Sentence {idx + 1}: {sentence_text}")

if __name__ == "__main__":
    main()