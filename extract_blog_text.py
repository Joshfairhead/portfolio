#!/usr/bin/env python3
"""Extract exact text from blog post HTML and update markdown files."""

import re
from html.parser import HTMLParser
import subprocess

# URLs and corresponding markdown files
BLOG_POSTS = [
    ("https://fishkarmatea.blogspot.com/2011/09/whittards-125th-anniversary-blend.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2011-09-14-whittards-125th-anniversary-blend/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/11/fortnum-mason-royal-blend-assamcelyon.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-11-29-fortnum-mason-royal-blend/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/11/whittards-mango-tea.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-11-29-whittards-mango-tea/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/11/whittards-darjeeling.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-11-29-whittards-darjeeling/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/11/mohokutie-second-flush-assam.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-11-29-mohokutie-second-flush-assam/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/11/bannockburn-ftgfop1-darjeeling.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-11-24-bannockburn-ftgfop1-darjeeling/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/08/margrets-hope-ftgfop.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-08-22-margrets-hope-ftgfop/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/08/lingia-ftgfop1.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-08-12-lingia-ftgfop1/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/06/passion-fruit-tea.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-06-06-passion-fruit-tea/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/06/blue-lady-chinease-black-teacitrus.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-06-06-blue-lady/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/06/harmutty-tippy-golden-assam.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-06-06-harmutty-tippy-golden-assam/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/03/pettiagalla-op-celyon.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-03-15-pettiagalla-op-ceylon/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/02/china-black-tea.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-02-25-china-black-tea/index.md"),
    ("https://fishkarmatea.blogspot.com/2010/02/arabian-tea.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2010-02-20-arabian-tea/index.md"),
    ("https://fishkarmatea.blogspot.com/2009/12/english-breakfast-blend.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2009-12-05-english-breakfast-blend/index.md"),
    ("https://fishkarmatea.blogspot.com/2009/12/ceylon-op.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2009-12-05-ceylon-op/index.md"),
    ("https://fishkarmatea.blogspot.com/2009/12/ceylon-silver-tips.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2009-12-05-ceylon-silver-tips/index.md"),
    ("https://fishkarmatea.blogspot.com/2009/12/assam-tgfop_05.html",
     "/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog/2009-12-05-assam-tgfop/index.md"),
]


class BlogTextExtractor(HTMLParser):
    """Extract text content from blog post HTML."""
    def __init__(self):
        super().__init__()
        self.in_post_body = False
        self.text = []
        self.skip_tags = 0

    def handle_starttag(self, tag, attrs):
        # Look for post-body div
        for attr, value in attrs:
            if attr == 'id' and 'post-body' in value:
                self.in_post_body = True
                return

        # Skip script, style, and comments
        if tag in ['script', 'style', 'noscript']:
            self.skip_tags += 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_post_body:
            # Check if we've reached the end of post content
            pass
        if tag in ['script', 'style', 'noscript']:
            self.skip_tags = max(0, self.skip_tags - 1)

    def handle_data(self, data):
        if self.in_post_body and self.skip_tags == 0:
            text = data.strip()
            if text and not text.startswith('<'):
                self.text.append(text)

    def get_text(self):
        return ' '.join(self.text).strip()


def fetch_url(url):
    """Fetch HTML content from URL."""
    result = subprocess.run(['curl', '-s', url], capture_output=True, text=True)
    return result.stdout


def extract_post_text(html):
    """Extract the main blog post text from HTML."""
    # Find the post-body content
    match = re.search(r'<div class=[\'"]post-body[^>]*>(.*?)<div class=[\'"]post-footer', html, re.DOTALL)
    if not match:
        return ""

    content = match.group(1)

    # Remove image tags and links
    content = re.sub(r'<a[^>]*><img[^>]*></a>', '', content)
    content = re.sub(r'<img[^>]*>', '', content)
    content = re.sub(r'<a[^>]*>', '', content)
    content = re.sub(r'</a>', '', content)

    # Remove divs but keep their content
    content = re.sub(r'<div[^>]*>', '\n', content)
    content = re.sub(r'</div>', '\n', content)

    # Remove br tags
    content = re.sub(r'<br\s*/?>', '\n', content)

    # Remove style tags and their content
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<title[^>]*>.*?</title>', '', content, flags=re.DOTALL)

    # Remove other HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Decode HTML entities
    content = content.replace('&nbsp;', ' ')
    content = content.replace('&amp;', '&')
    content = content.replace('&quot;', '"')
    content = content.replace('&#163;', '£')
    content = content.replace('&#8364;', '€')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')

    # Clean up whitespace
    lines = [line.strip() for line in content.split('\n') if line.strip()]
    content = '\n'.join(lines)

    return content.strip()


def read_markdown_file(filepath):
    """Read markdown file and return content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def update_markdown_file(filepath, new_text):
    """Update markdown file with new review text."""
    content = read_markdown_file(filepath)

    # Add banner if not present in [extra] section
    # Insert right after [extra] line
    if 'banner =' not in content:
        content = re.sub(
            r'(\[extra\]\s*\n)',
            r'\1banner = "image1.jpg"\n',
            content
        )

    # Fix malformed image lines (lines like "!banner = ..." or "[text](image)" without !)
    # Remove lines that look like "!banner = "image1.jpg""
    content = re.sub(r'^!banner = ".*?"\s*\n', '', content, flags=re.MULTILINE)
    # Fix lines like "[text](image.jpg)" to be "![text](image.jpg)"
    content = re.sub(r'^(\[(?![^\]]*\]\([^\)]*\))[^\]]+\]\([^\)]+\))$', r'!\1', content, flags=re.MULTILINE)

    # Find where to insert the review text (after +++\n\nimages, before \n## Tea Details)
    # Pattern: find all images after frontmatter, then the content section, then ## Tea Details
    # Match the closing +++, then newlines, then multiple image lines, then content, then Tea Details
    pattern = r'(^\+\+\+\s*\n\n(?:!\[.*?\]\(.*?\)\s*\n)+)(.*?)(\n## Tea Details)'

    def replace_content(match):
        return f'{match.group(1)}\n{new_text}\n{match.group(3)}'

    new_content = re.sub(pattern, replace_content, content, flags=re.DOTALL | re.MULTILINE)

    # If the pattern didn't match (no Tea Details section), try alternative pattern
    if new_content == content:
        # Just place after images if Tea Details section doesn't exist
        pattern2 = r'(^\+\+\+\s*\n\n(?:!\[.*?\]\(.*?\)\s*\n)+)(.*?)$'
        new_content = re.sub(pattern2, replace_content, content, flags=re.DOTALL | re.MULTILINE)

    content = new_content

    # Remove ## Images section at the end if it exists
    content = re.sub(r'\n## Images\n.*$', '', content, flags=re.DOTALL)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    """Main processing function."""
    print("Fetching and processing blog posts...")

    for url, md_file in BLOG_POSTS:
        print(f"\nProcessing: {url}")

        # Fetch HTML
        html = fetch_url(url)
        if not html:
            print(f"  ERROR: Could not fetch {url}")
            continue

        # Extract text
        text = extract_post_text(html)
        if not text:
            print(f"  ERROR: Could not extract text from {url}")
            continue

        print(f"  Extracted {len(text)} characters")
        print(f"  Preview: {text[:100]}...")

        # Update markdown file
        try:
            update_markdown_file(md_file, text)
            print(f"  SUCCESS: Updated {md_file}")
        except Exception as e:
            print(f"  ERROR: Failed to update {md_file}: {e}")

    print("\nDone!")


if __name__ == '__main__':
    main()
