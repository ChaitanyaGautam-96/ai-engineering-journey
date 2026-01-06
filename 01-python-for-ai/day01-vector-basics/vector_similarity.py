import numpy as np

def cosine_similarity(vec_a, vec_b):
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot_product / (norm_a * norm_b)

# Examples

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])

similarity = cosine_similarity(vec1, vec2)
print(f"Cosine Similarity: {similarity}")