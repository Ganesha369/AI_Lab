# Required: pip install tiktoken (for OpenAI style) or transformers (for Google/Meta style)
import tiktoken

def analyze_tokens(text: str, model_encoding: str = "cl100k_base"):
    """
    Demonstrates how a string is decomposed into token IDs and back.
    cl100k_base is the encoding used by GPT-4 and GPT-3.5.
    """
    encoding = tiktoken.get_encoding(model_encoding)
    
    # 1. Encoding: String -> List of Token IDs
    token_ids = encoding.encode(text)
    
    # 2. Decoding: Token ID -> String Piece
    token_pieces = [encoding.decode_single_token_bytes(tid).decode('utf-8', errors='replace') 
                    for tid in token_ids]

    print(f"Original Text: '{text}'")
    print(f"Token Count:   {len(token_ids)}")
    print(f"Token IDs:     {token_ids}")
    print(f"Token Pieces:  {token_pieces}")
    print("-" * 30)

# Case 1: Simple word
analyze_tokens("Artificial Intelligence")

# Case 2: Sub-word decomposition (Complex words)
analyze_tokens("Tokenization is foundational.")

# Case 3: Space efficiency (Notice how the space is often attached to the start of the word)
analyze_tokens("hello hello")

"""
STAFF ENGINEER TIP:
When building production RAG (Retrieval Augmented Generation) systems,
always calculate your token usage locally before hitting the API.
This prevents 'ContextWindowExceeded' errors and allows for better 
cost estimation.
"""