from pathlib import Path
import re, json

root = Path('/mnt/data/seo_work')
base = 'https://narjesrohani.com/'

pages = {
    'index.html': {
        'title': 'Dr. Narjes Rohani | Brain Genomics & Precision Medicine | University of Oxford',
        'description': 'Dr. Narjes Rohani is a computational genomics researcher at the University of Oxford studying the molecular mechanisms of brain disorders using developmental brain multi-omics, regulatory genomics and machine learning to identify therapeutic targets and advance precision medicine.',
        'canonical': base,
        'og_image': 'assets/images/personal/profile.jpg',
    },
    'pages/projects.html': {
        'title': 'Research | Dr. Narjes Rohani | Brain Disorders, Multi-omics & Regulatory Genomics',
        'description': 'Research by Dr. Narjes Rohani on brain-disorder mechanisms, developmental multi-omics, regulatory genomics, common and rare neurodevelopmental and psychiatric disorders, cis-regulatory elements and therapeutic target discovery.',
        'canonical': base + 'pages/projects.html',
        'og_image': 'assets/images/personal/profile.jpg',
    },
    'pages/publications.html': {
        'title': 'Publications | Dr. Narjes Rohani | Genomics, Brain Disorders & Health Data Science',
        'description': 'Publications and preprints by Dr. Narjes Rohani covering brain genomics, developmental neurobiology, regulatory mechanisms, rare disease, health data science and computational biology.',
        'canonical': base + 'pages/publications.html',
        'og_image': 'assets/images/personal/profile.jpg',
    },
    'pages/news.html': {
        'title': 'News & Updates | Dr. Narjes Rohani | University of Oxford',
        'description': 'News, research updates, public engagement, talks, publications and milestones from Dr. Narjes Rohani at the University of Oxford.',
        'canonical': base + 'pages/news.html',
        'og_image': 'assets/images/personal/profile.jpg',
    },
    'pages/teaching.html': {
        'title': 'Teaching & Mentoring | Dr. Narjes Rohani | Health Data Science',
        'description': 'Teaching, mentoring and education research by Dr. Narjes Rohani, including health data science, artificial intelligence and how people learn complex biomedical concepts.',
        'canonical': base + 'pages/teaching.html',
        'og_image': 'assets/images/personal/profile.jpg',
    },
    'pages/engagement.html': {
        'title': 'Public Engagement | Dr. Narjes Rohani | Genes, Brains & Breakthroughs',
        'description': 'Public engagement and science communication by Dr. Narjes Rohani, including Genes, Brains & Breakthroughs, an animated series explaining genomics and neurodevelopmental disorders to patients, families and the public.',
        'canonical': base + 'pages/engagement.html',
        'og_image': 'assets/images/personal/profile.jpg',
    },
    'pages/cv.html': {
        'title': 'CV | Dr. Narjes Rohani | University of Oxford',
        'description': 'Curriculum vitae of Dr. Narjes Rohani, computational genomics researcher at the University of Oxford.',
        'canonical': base + 'pages/cv.html',
        'og_image': 'assets/images/personal/profile.jpg',
    },
    'pages/images.html': {
        'title': 'Research & Conference Images | Dr. Narjes Rohani',
        'description': 'Selected research, conference and public engagement photographs from Dr. Narjes Rohani.',
        'canonical': base + 'pages/images.html',
        'og_image': 'assets/images/personal/fens-poster.jpg',
    },
    'pages/contact.html': {
        'title': 'Contact | Dr. Narjes Rohani | University of Oxford',
        'description': 'Contact Dr. Narjes Rohani at the University of Oxford for research, collaboration, speaking and public engagement enquiries.',
        'canonical': base + 'pages/contact.html',
        'og_image': 'assets/images/personal/profile.jpg',
    },
}

person_schema = {
    '@context': 'https://schema.org',
    '@type': 'Person',
    'name': 'Dr. Narjes Rohani',
    'url': base,
    'image': base + 'assets/images/personal/profile.jpg',
    'jobTitle': 'Postdoctoral Research Associate',
    'worksFor': {
        '@type': 'Organization',
        'name': 'University of Oxford',
        'url': 'https://www.ox.ac.uk/'
    },
    'affiliation': {
        '@type': 'Organization',
        'name': 'Institute of Developmental and Regenerative Medicine, University of Oxford',
        'url': 'https://www.idrm.ox.ac.uk/'
    },
    'email': 'mailto:narjes.rohani@paediatrics.ox.ac.uk',
    'sameAs': [
        'https://scholar.google.com/citations?user=2zoKXHUAAAAJ&hl=en',
        'https://github.com/nrohani',
        'https://www.linkedin.com/in/narjes-rohani-153b0b168/',
        'https://www.idrm.ox.ac.uk/people/research-groups/sanders-group/narjes-rohani'
    ],
    'knowsAbout': [
        'Computational genomics',
        'Brain disorders',
        'Neurodevelopmental disorders',
        'Psychiatric disorders',
        'Developmental brain multi-omics',
        'Regulatory genomics',
        'Cis-regulatory elements',
        'Machine learning',
        'Precision medicine',
        'CRISPRa/i'
    ]
}

website_schema = {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    'name': 'Dr. Narjes Rohani',
    'url': base,
    'description': pages['index.html']['description'],
    'publisher': {'@type': 'Person', 'name': 'Dr. Narjes Rohani'}
}

for rel, meta in pages.items():
    path = root / rel
    text = path.read_text(encoding='utf-8')
    # remove existing title + description, canonical, robots and social tags if rerun
    text = re.sub(r'<title>.*?</title>', '', text, flags=re.S)
    text = re.sub(r'\s*<meta name="description"[^>]*>', '', text)
    text = re.sub(r'\s*<meta name="robots"[^>]*>', '', text)
    text = re.sub(r'\s*<link rel="canonical"[^>]*>', '', text)
    text = re.sub(r'\s*<meta property="og:[^"]+"[^>]*>', '', text)
    text = re.sub(r'\s*<meta name="twitter:[^"]+"[^>]*>', '', text)
    text = re.sub(r'\s*<script type="application/ld\+json">.*?</script>', '', text, flags=re.S)

    prefix = '' if rel == 'index.html' else '../'
    icon_prefix = '' if rel == 'index.html' else '../'
    social_image = base + meta['og_image']
    head_add = f'''\n  <title>{meta['title']}</title>\n  <meta name="description" content="{meta['description']}">\n  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">\n  <link rel="canonical" href="{meta['canonical']}">\n  <meta property="og:type" content="website">\n  <meta property="og:title" content="{meta['title']}">\n  <meta property="og:description" content="{meta['description']}">\n  <meta property="og:url" content="{meta['canonical']}">\n  <meta property="og:image" content="{social_image}">\n  <meta property="og:site_name" content="Dr. Narjes Rohani">\n  <meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:title" content="{meta['title']}">\n  <meta name="twitter:description" content="{meta['description']}">\n  <meta name="twitter:image" content="{social_image}">\n'''
    if rel == 'index.html':
        schema = [person_schema, website_schema]
    else:
        schema = [{'@context':'https://schema.org','@type':'WebPage','name':meta['title'],'url':meta['canonical'],'description':meta['description'],'isPartOf':{'@type':'WebSite','name':'Dr. Narjes Rohani','url':base},'about':{'@type':'Person','name':'Dr. Narjes Rohani','url':base}}]
    head_add += '  <script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, indent=2) + '\n  </script>\n'
    # insert title and SEO immediately after viewport meta
    marker = '<meta name="viewport" content="width=device-width, initial-scale=1">'
    text = text.replace(marker, marker + head_add, 1)
    path.write_text(text, encoding='utf-8')

# Update README dash styling to avoid em dash.
readme = root / 'README.md'
readme.write_text(readme.read_text(encoding='utf-8').replace('Narjes Rohani  Academic Website', 'Narjes Rohani Academic Website'), encoding='utf-8')

# Fix a couple of remaining visible name inconsistencies in footer/brand while preserving publication author emphasis.
for rel in ['pages/publications.html']:
    path = root / rel
    t = path.read_text(encoding='utf-8')
    t = t.replace('class="brand" href="../index.html"><span class="mark"></span>Narjes Rohani', 'class="brand" href="../index.html"><span class="mark"></span>Dr. Narjes Rohani')
    t = re.sub(r'<strong>Narjes Rohani</strong>\s*<div class="footer-links">', 'Dr. Narjes Rohani<div class="footer-links">', t)
    path.write_text(t, encoding='utf-8')
