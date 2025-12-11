#!/usr/bin/env python3
"""Fix tea blog posts to add missing images and banners."""

import os
import re

TEA_BLOG_DIR = '/Users/joshfairhead/dev/portfolio/.conductor/doha/content/tea-blog'

def fix_post(md_file_path):
    """Fix a single blog post."""
    post_dir = os.path.dirname(md_file_path)

    # Read content
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count actual image files
    image_files = sorted([f for f in os.listdir(post_dir) if f.startswith('image') and f.endswith('.jpg')])
    num_images = len(image_files)

    if num_images == 0:
        # No images, just add banner if missing
        if 'banner =' not in content:
            content = re.sub(
                r'(\[extra\]\s*\n)',
                r'\1banner = "image1.jpg"\n',
                content
            )
        return content

    # Add banner if not present
    if 'banner =' not in content:
        content = re.sub(
            r'(\[extra\]\s*\n)',
            r'\1banner = "image1.jpg"\n',
            content
        )

    # Find frontmatter end
    matches = list(re.finditer(r'^\+\+\+$', content, re.MULTILINE))
    if len(matches) < 2:
        return content

    frontmatter_end = matches[1].end()

    # Find existing images section
    after_frontmatter = content[frontmatter_end:]
    image_pattern = r'^\s*\n((?:!\[.*?\]\(image\d+\.jpg\)\s*\n)+)'
    image_match = re.match(image_pattern, after_frontmatter, re.MULTILINE)

    # Create proper image markdown
    image_labels = ['packet', 'close-up', 'brewed tea', 'detail']
    new_images = []
    for i, img_file in enumerate(image_files):
        label = image_labels[i] if i < len(image_labels) else f'image {i+1}'
        post_title = os.path.basename(post_dir).split('-', 3)[-1].replace('-', ' ').title()
        if i == 0:
            new_images.append(f'![{post_title} {label}]({img_file})')
        else:
            new_images.append(f'![Tea {label}]({img_file})')

    new_images_text = '\n'.join(new_images) + '\n'

    # Replace or insert images
    if image_match:
        # Replace existing images
        old_images = image_match.group(1)
        content = content[:frontmatter_end] + '\n\n' + new_images_text + after_frontmatter[image_match.end():]
    else:
        # Insert images after frontmatter
        content = content[:frontmatter_end] + '\n\n' + new_images_text + after_frontmatter

    return content


def main():
    """Process all tea blog posts."""
    dirs = [d for d in os.listdir(TEA_BLOG_DIR)
            if os.path.isdir(os.path.join(TEA_BLOG_DIR, d)) and d.startswith('20')]

    for dir_name in sorted(dirs):
        md_file = os.path.join(TEA_BLOG_DIR, dir_name, 'index.md')
        if os.path.exists(md_file):
            print(f'Processing {dir_name}...')
            try:
                fixed_content = fix_post(md_file)
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f'  ✓ Fixed {dir_name}')
            except Exception as e:
                print(f'  ✗ Error fixing {dir_name}: {e}')

    print('\nDone!')


if __name__ == '__main__':
    main()
