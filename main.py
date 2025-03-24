from research_agent import research
from content_planner import plan
from content_generator import generator
from review import review
from seo_optimization import optimize
from sentiment_analyser import analyze_audience_sentiment

def save_blog(content):
    """Saves the blog content in multiple formats."""
    
    formats = {
        "txt": "generated_blog.txt",
        "md": "generated_blog.md",
        "html": "generated_blog.html"
    }
    
    for ext, filename in formats.items():
        with open(filename, "w", encoding="utf-8") as file:
            if ext == "html":
                file.write(f"<html><body><h1>Generated Blog</h1><p>{content.replace('\n', '<br>')}</p></body></html>")
            else:
                file.write(content)
        
        print(f"Blog saved successfully as {filename}")

def main():
    print("\nStarting the blog generation pipeline...\n")
    
    # Step 1: Research trending topics
    research_content = research()
    
    # Step 2: Generate a structured outline
    outline = plan(research_content)
    
    # Step 3: Generate and refine blog content
    blog_content = generator(outline)
    
    # Step 4: Optimize for SEO
    seo_content = optimize(blog_content)
    
    # Step 5: Review the blog for grammar and quality
    reviewed_blog = review(seo_content)
    
    # Step 6: Analyze audience sentiment
    sentiment = analyze_audience_sentiment(reviewed_blog)
    
    # Step 7: Save the blog in multiple formats
    save_blog(reviewed_blog)
    
    print(f"\nThe sentiment of the blog is: {sentiment}")

if __name__ == "__main__":
    main()
