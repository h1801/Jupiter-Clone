from flask import Flask, request, jsonify
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

app = Flask(__name__)

# Your clustering function
def clustering(candidate_labels, sequence_to_classify):
    data = classifier(sequence_to_classify, candidate_labels)
    # Get the index of the maximum score
    max_score_index = data['scores'].index(max(data['scores']))
    # Get the label with the maximum score
    max_score_label = data['labels'][max_score_index]
    return max_score_label

# Define the API endpoint
@app.route('/clustering', methods=['POST'])
def predict():
    # Get the data from the request
    data = request.get_json()
    candidate_labels = data['candidate_labels']
    sequence_to_classify = data['sequence_to_classify']
    
    # Call the clustering function
    result = clustering(candidate_labels, sequence_to_classify)
    
    # Return the result as a JSON response
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()