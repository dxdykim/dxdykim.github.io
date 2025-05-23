# coding: utf-8

import pandas as pd
import os

# Load publications.tsv
publications = pd.read_csv("publications.tsv", sep="\t", header=0)

# Optional HTML escape (for YAML safety)
html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

# Loop through each row
for row, item in publications.iterrows():
    md_filename = f"{item.pub_date}-{item.url_slug}.md"
    html_filename = f"{item.pub_date}-{item.url_slug}"
    
    # Basic YAML front matter (still required for Jekyll)
    md = "---\n"
    md += f"title: \"{html_escape(item.title)}\"\n"
    md += "collection: publications\n"
    md += f"permalink: /publication/{html_filename}\n"
    md += f"date: {item.pub_date}\n"
    md += "---\n\n"

    # Title as bold text
    md += f"**{html_escape(item.title)}**  \n"

    # Venue or status (e.g. 'submitted to NeurIPS 2024')
    if isinstance(item.venue, str) and len(item.venue.strip()) > 0:
        md += f"*{html_escape(item.venue)}*  \n"

    # Paper download link
    if isinstance(item.paper_url, str) and len(item.paper_url.strip()) > 0:
        md += f"[PDF]({item.paper_url})\n"

    # Save to file
    with open(f"../_publications/{md_filename}", 'w') as f:
        f.write(md)
