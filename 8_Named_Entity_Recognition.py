""" #spacy
import spacy

# Load pre-trained spaCy NER model
nlp = spacy.load("en_core_web_sm")  # For better performance, consider a fine-tuned model

# Combine all text into a single string
full_text = ' '.join(cleaned_text)

# Perform NER
doc = nlp(full_text)

entities = [(ent.text, ent.label_) for ent in doc.ents] """

from transformers import LayoutLMForTokenClassification, LayoutLMTokenizer
import torch

# Load pre-trained LayoutLM model and tokenizer
tokenizer = LayoutLMTokenizer.from_pretrained("microsoft/layoutlm-base-uncased")
model = LayoutLMForTokenClassification.from_pretrained("your-fine-tuned-model")

# Prepare input (requires bounding box information)
# This is more involved and requires structured input; refer to LayoutLM documentation
# Prepare inputs with bounding boxes
encoded_inputs = tokenizer(texts, boxes=bounding_boxes, return_tensors="pt", padding="max_length", truncation=True)

# Example placeholder
inputs = tokenizer(full_text, return_tensors="pt")
outputs = model(**inputs)
predictions = torch.argmax(outputs.logits, dim=2)

# Map predictions to labels (e.g., B-FIRST, I-FIRST, B-LAST, I-LAST)
# Extract first, middle, last names based on labels