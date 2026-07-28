"""Download the remaining failed PDFs with correct URLs and SSL bypass."""
import requests, urllib3
urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'
}

remaining_pdfs = {
    # Real URLs found by scraping Nepal Bank downloads page
    "nepalbank_fonepay_merchant_form": "https://www.nepalbank.com.np/storage/download/1626761457_fonepay_merchant_registration_form.pdf",
    "nepalbank_pos_merchant_application": "https://www.nepalbank.com.np/storage/download/1626761820_POS_Merchant_Application_Form1.pdf",
    "nepalbank_pos_merchant_agreement": "https://www.nepalbank.com.np/storage/download/1626761592_POS_Merchant_agreement.pdf",
}

for name, url in remaining_pdfs.items():
    dest = f"data/fonepay/pdf/{name}.pdf"
    try:
        r = requests.get(url, headers=headers, timeout=30, verify=False)
        r.raise_for_status()
        with open(dest, 'wb') as f:
            f.write(r.content)
        print(f"[OK]   {name}.pdf  ({len(r.content)//1024} KB)")
    except Exception as e:
        print(f"[FAIL] {name} — {e}")
