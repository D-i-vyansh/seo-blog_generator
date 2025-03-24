import ollama  # Importing Ollama for AI-powered content optimization

def optimize_for_seo(content):
    """
    Enhances the blog content for SEO by adding relevant keywords, headings, 
    meta title, meta description, and structuring it for better search visibility.

    Args:
        content (str): The original blog content.

    Returns:
        str: SEO-optimized blog content.
    """

    # Define the AI prompt to optimize the blog for SEO
    prompt = f"""
    Improve the SEO of this HR blog:

    {content}

    Modify the blog to:
    - Include relevant keywords naturally within the content.
    - Use SEO-friendly headings and structure.
    - Replace the main title with a **meta title** and add a **meta description**.
    - Integrate 1-2 relevant quotes to enhance credibility.
    - Prioritize **helpful, valuable, and engaging content**.
    - Implement the **E-E-A-T Principle** (Experience, Expertise, Authoritativeness, Trustworthiness).
    - Ensure smooth readability without mentioning terms like "SEO optimized" or "AI-generated."
    
    Format:
    - Use bold formatting for important terms.
    - Maintain a clean and structured heading hierarchy.
    """

    # Generate optimized content using Mistral
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    
    return response["message"]["content"]


def optimize(blog_content):
    """
    Optimizes the given blog content for SEO.

    Args:
        blog_content (str): The original blog content.

    Returns:
        str: The SEO-optimized version of the blog.
    """

    print("SEO Optimization in progress...")
    return optimize_for_seo(blog_content)
