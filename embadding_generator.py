import requests

def generate_embedding(text, model_url="http://localhost:11434/api/embeddings"):
    """
    Generate embeddings for the given text using a local Ollama embedding model.

    Args:
        text (str): The input text to embed.
        model_url (str): The URL of the local Ollama embedding API.

    Returns:
        list: The embedding vector as a list of floats, or None if failed.
    """
    payload = {"model": "nomic-embed-text", "prompt": text}
    try:
        response = requests.post(model_url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data.get("embedding")
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None
