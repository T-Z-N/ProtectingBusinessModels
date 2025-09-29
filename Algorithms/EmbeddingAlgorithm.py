import csv
import re
import numpy as np
import torch
import time
from google import genai

api_key = ""  # Insrt your Gemini API key here
client = genai.Client(api_key=api_key)

file_path = r"Assertion/Mechanism.md"

claims = []
claim_ids = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        match = re.match(r'^(\d+)\.\s*(.*?)$', line)

        if match:
            claim_id = int(match.group(1))
            claim_text = match.group(2)
            claim_text = claim_text.strip('"')
            claims.append(claim_text)
            claim_ids.append(claim_id)

print(f"Loaded {len(claims)} claims from file")

def get_embeddings(texts, batch_size=5):
    all_embeddings = []
    
    print(f"Generating embeddings in batches of {batch_size}...")
    
    # Process in batches
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        batch_end = min(i + batch_size, len(texts))
        print(f"Processing batch {i+1}-{batch_end} of {len(texts)}")
        
        result = client.models.embed_content(
            model="text-embedding-004", 
            contents=batch
        )
        
        for embedding in result.embeddings:
            embedding_values = embedding.values
            all_embeddings.append(embedding_values)
        
        time.sleep(1)
    
    return np.array(all_embeddings, dtype=np.float32)

claim_embeddings = get_embeddings(claims)
print("Embeddings generated successfully")

print("Calculating similarity scores between all pairs...")
similarity_matrix = torch.matmul(
    torch.tensor(claim_embeddings, dtype=torch.float32), 
    torch.tensor(claim_embeddings, dtype=torch.float32).transpose(0, 1)
)

output_file = 'similarity_scores.csv'
threshold = 0.50  

with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['source_id', 'target_id', 'source_claim', 'target_claim', 'weight', 'is_Condensed'])

    similar_pairs = 0
    for i in range(len(claims)):
        for j in range(i + 1, len(claims)):
            similarity_score = similarity_matrix[i][j].item()
            if similarity_score >= threshold:
                writer.writerow([
                    claim_ids[i],
                    claim_ids[j],
                    claims[i],
                    claims[j],
                    f"{similarity_score:.6f}",
                    "False"
                ])
                similar_pairs += 1

print(f"Analysis complete. Found {similar_pairs} similar claim pairs (similarity >= {threshold})")
print(f"Results saved to {output_file}")