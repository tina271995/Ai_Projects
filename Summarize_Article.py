import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# Download NLTK data
nltk.download('punkt')

def summarize():
    url = utext.get("1.0", "end").strip()
    if not url:
        return  # Do nothing if URL is empty
    
    article = Article(url)
    try:
        article.download()
        article.parse()
        article.nlp()

        # Enable text boxes to insert content
        title.config(state='normal')
        author.config(state='normal')
        publication.config(state='normal')
        summary.config(state='normal')
        sentiment.config(state='normal')

        # Insert article data into text boxes
        title.delete('1.0', 'end')
        title.insert('1.0', article.title)

        author.delete('1.0', 'end')
        author.insert('1.0', ', '.join(article.authors))

        publication.delete('1.0', 'end')
        publication.insert('1.0', str(article.publish_date))

        summary.delete('1.0', 'end')
        summary.insert('1.0', article.summary)

        analysis = TextBlob(article.text)
        sentiment.delete('1.0', 'end')
        sentiment.insert(
            '1.0',
            f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'
        )

        # Disable text boxes after inserting content
        title.config(state='disabled')
        author.config(state='disabled')
        publication.config(state='disabled')
        summary.config(state='disabled')
        sentiment.config(state='disabled')
    except Exception as e:
        # Handle exceptions gracefully
        summary.config(state='normal')
        summary.delete('1.0', 'end')
        summary.insert('1.0', f"Error: {e}")
        summary.config(state='disabled')


# Create Tkinter GUI
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

# URL Input
ulabel = tk.Label(root, text="Enter URL:")
ulabel.pack()
utext = tk.Text(root, height=2, width=140)
utext.pack()

# Title
tlabel = tk.Label(root, text="Title")
tlabel.pack()
title = tk.Text(root, height=1, width=140, bg='#dddddd')
title.config(state='disabled')
title.pack()

# Author
alabel = tk.Label(root, text="Author(s)")
alabel.pack()
author = tk.Text(root, height=1, width=140, bg='#dddddd')
author.config(state='disabled')
author.pack()

# Publication Date
plabel = tk.Label(root, text="Publication Date")
plabel.pack()
publication = tk.Text(root, height=1, width=140, bg='#dddddd')
publication.config(state='disabled')
publication.pack()

# Summary
slabel = tk.Label(root, text="Summary")
slabel.pack()
summary = tk.Text(root, height=10, width=140, bg='#dddddd')
summary.config(state='disabled')
summary.pack()

# Sentiment Analysis
selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()
sentiment = tk.Text(root, height=2, width=140, bg='#dddddd')
sentiment.config(state='disabled')
sentiment.pack()

# Summarize Button
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

# Run the application
root.mainloop()
