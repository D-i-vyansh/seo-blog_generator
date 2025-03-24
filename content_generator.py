import ollama  # Importing Ollama for AI-powered text generation

def generate_blog_draft(outline):
    """
    Generates a detailed blog draft using the Mistral model via Ollama.

    Args:
        outline (str): The structured outline for the blog.

    Returns:
        str: A well-structured blog draft.
    """
    
    # Define the AI prompt to create a detailed blog
    prompt = f"""
    Write a detailed and informative blog post of at least 3000 words based on the following structured outline:
    
    {outline}
    
    Ensure the content is engaging, well-structured, and follows this format:
    
    - H1: Main Title
        Introduction
      - H2: Section 1
      
        - H3: Subsection 1.1
        - H3: Subsection 1.2
        ...
        - Conclusion
    each heading must contain a proper content 
    """

    # Generate the blog draft using Mistral
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    
    return response["message"]["content"]


def refine_blog_with_gemma(blog_draft):
    """
    Enhances and optimizes the blog draft for clarity, readability, and conciseness using the Gemma model.

    Args:
        blog_draft (str): The initial blog draft.

    Returns:
        str: The refined and polished blog.
    """

    # Define the AI prompt to refine the blog content
    prompt = f"""
    Improve the following blog draft by making it more concise, clear, and engaging. 
    Ensure proper grammar, readability, and flow while preserving the original meaning.
    
    Blog Draft:
    {blog_draft}
    """

    # Refine the blog using Gemma
    response = ollama.chat(model="gemma:2b", messages=[{"role": "user", "content": prompt}])
    
    return response["message"]["content"]


def generator(outline):
    """
    Generates a blog by first creating a draft and then refining it for better readability and quality.

    Args:
        outline (str): The structured blog outline.

    Returns:
        str: The final, polished blog content.
    """

    print("Writing the initial blog draft...")
    blog_draft = generate_blog_draft(outline)
    
    print("Refining the blog for clarity and readability...")
    final_blog = refine_blog_with_gemma(blog_draft)
    
    return final_blog
