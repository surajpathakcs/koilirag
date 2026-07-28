"""Find the real PDF links from Nepal Bank downloads page."""
import requests, re, urllib3
urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
}

r = requests.get('https://www.nepalbank.com.np/pages/downloads', headers=headers, timeout=15, verify=False)
pdfs = re.findall(r'href=["\']([^"\']*?\.pdf)["\']', r.text, re.IGNORECASE)

print(f'Total PDFs on page: {len(pdfs)}')
print('\nFonepay/QR/Merchant matches:')
for p in pdfs:
    if any(k in p.lower() for k in ['fonepay', 'merchant', 'qr']):
        print(f'  MATCH: {p}')

print('\nAll PDFs:')
for p in pdfs[:30]:
    print(f'  {p}')
