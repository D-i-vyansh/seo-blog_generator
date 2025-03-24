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

    Add:
    - Keywords 
    - SEO-Friendly Headings and keywords
    - replace the main title with meta title and add meta description just as description
    - may use1 or 2 related quote in the blog
    - prioritizes helpful and valuable content
    - implement the E-E-A-T Principle: Experience, Expertise, Authoritativeness, Trustworthiness while modifying
    - dont mention things like seo optimized or ai generated just make a complete blog and nothing else
    
    in the blog itself and dont write the word title or quote just bold them or make heading difference"""
    

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
