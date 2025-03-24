

# **SEO Blog Generator**  

## **Overview**  
This project automates the blog creation process using AI models and NLP tools. It researches trending topics, generates structured content, optimizes it for SEO, performs grammar and sentiment analysis, and delivers a well-written final blog.  

---

## **System Architecture**  

The system follows a modular approach with multiple agents handling specific tasks:  

1. **Research Agent**: Searches for trending HR topics and extracts relevant content.  
2. **Planning Agent**: Generates a structured outline for the blog.  
3. **Content Generation Agent**: Uses AI to draft and refine a full-length blog.  
4. **SEO Optimization Agent**: Enhances content with SEO best practices.  
5. **Review Agent**: Performs grammar and readability corrections.  
6. **Sentiment Analysis Agent**: Assesses the blog’s emotional tone.  

The pipeline ensures a **seamless workflow** where each agent refines the output before passing it to the next stage.  

---

## **Agent Workflow**  

1. **Research (`research_agent.py`)**  
   - Performs Google searches for trending HR topics.  
   - Extracts content from top-ranked articles using BeautifulSoup.  

2. **Planning (`content_planner.py`)**  
   - Uses AI (Gemma) to generate a structured outline for the blog.  

3. **Content Generation (`content_generator.py`)**  
   - Writes a detailed blog draft using AI (Mistral).  
   - Refines the draft for clarity and readability with AI (Gemma).  

4. **SEO Optimization (`seo_optimization.py`)**  
   - Adds SEO-friendly keywords, headings, and metadata.  
   - Ensures content follows E-E-A-T principles (Experience, Expertise, Authoritativeness, Trustworthiness).  

5. **Review (`review.py`)**  
   - Uses LanguageTool to correct grammar and improve readability.  

6. **Sentiment Analysis (`sentiment_analyser.py`)**  
   - Analyzes the blog’s tone (Positive, Negative, Neutral) using TextBlob.  

---

## **Tools and Frameworks Used**  

- **Python** – Core programming language.  
- **BeautifulSoup** – Web scraping to extract content from web pages.  
- **Requests** – Fetching content from URLs.  
- **GoogleSearch-Python** – Performing Google searches.  
- **Ollama** – AI model interaction (Gemma, Mistral).  
- **LanguageTool-Python** – Grammar and spell-checking.  
- **TextBlob** – Sentiment analysis.  

---

## **Installation**  

Ensure Python (>=3.8) is installed on your system.  

### **Step 1: Clone the Repository**  
```sh
git clone https://github.com/D-i-vyansh/seo-blog_generator.git
cd seo-blog_generator
```

### **Step 2: Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **Step 3: Run the Blog Generation Pipeline**  
```sh
python main.py
```

---

## **Execution Flow**  

1. The script starts with `main.py`, triggering the pipeline.  
2. Research agent fetches trending topics and extracts content.  
3. Planning agent structures the information into a blog outline.  
4. Content generation agent drafts and refines the blog.  
5. SEO optimization agent improves the blog for better ranking.  
6. Review agent corrects grammatical and readability issues.  
7. Sentiment analysis agent evaluates the blog’s tone.  
8. The final blog is generated and saved as a file.  

---

## **Future Enhancements**  
- Support for multiple topics beyond HR.  
- Integration with AI-powered fact-checking.  
- Advanced keyword and NLP-based trend analysis.  

---

This AI-powered system automates content creation efficiently, ensuring high-quality, SEO-friendly, and engaging blog posts. 
