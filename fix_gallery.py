import re

with open('c:/Users/Administrator/Downloads/paintball.web.id/gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove onclick and style from portfolio-wrap
html = re.sub(r'onclick="this\.querySelector\(\'a\.glightbox\'\)\.click\(\)"\s*style="cursor:\s*pointer;"', '', html)

# Replace <a ... class="glightbox d-none"></a> with <a ... class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a>
html = re.sub(r'(<a\s+href="[^"]+"\s+data-gallery="[^"]+"\s+class="glightbox)\s+d-none(">) *(</a>)', r'\1 preview-link\2<i class="bi bi-zoom-in"></i>\3', html)

with open('c:/Users/Administrator/Downloads/paintball.web.id/gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Gallery HTML fixed.")
