"""
Fonepay Corpus Downloader
Downloads all HTML pages and PDFs from resources.md into data/fonepay/
"""
import os
import time
import requests
from pathlib import Path
from urllib.parse import urlparse

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}

HTML_PAGES = {
    # Pillar 1 - Merchant & Product
    "business_home": "https://fonepay.com/business",
    "business_app": "https://fonepay.com/business/app",
    "merchant_enrollment": "https://fonepay.com/business/merchant-enrollment",
    "qr_payments": "https://fonepay.com/customers/qr-payment",
    "fonepay_direct": "https://fonepay.com/customers/fonepay-direct",
    "fonepay_bills": "https://fonepay.com/customers/fonepay-bills",
    "fonepay_app": "https://fonepay.com/customers/fonepay-app",
    "fonetag": "https://fonepay.com/customers/fonetag",
    "credit_card": "https://fonepay.com/customers/fonepay-credit-card",
    "checkout": "https://fonepay.com/customers/checkout-by-fonepay",
    "partner": "https://fonepay.com/partner",
    "business_academy": "https://fonepay.com/partner/business-academy",
    "about": "https://fonepay.com/about",
    "contact_us": "https://fonepay.com/contact-us",
    "faqs": "https://fonepay.com/faqs",
    # Pillar 2 - Legal & Policies
    "terms_and_conditions": "https://fonepay.com/terms-and-conditions",
    "fees_and_charges": "https://fonepay.com/content/fees-and-charges",
    "information_security_policy": "https://fonepay.com/content/information-security-policy",
    "settlement_options_terms": "https://fonepay.com/content/settlement-options-terms",
    "cross_border_terms": "https://fonepay.com/content/cross-border-payments-terms-of-use",
    "business_app_privacy": "https://fonepay.com/content/business-app-privacy-policy",
    "app_privacy": "https://fonepay.com/content/privacy-policy",
    "publications": "https://fonepay.com/publications",
    "downloads": "https://fonepay.com/downloads",
    "reports": "https://fonepay.com/reports",
    "notices": "https://fonepay.com/notices",
    "blogs": "https://fonepay.com/blogs",
    # Bonus
    "blog_ceo": "https://fonepay.com/blogs/fonepay-reappoints-mr-diwas-kumars-as-ceo-for-four-more-years",
}

PDF_PAGES = {
    "fonepay_pcidss": "https://fonepay.com/files/fonepay-pcidss.pdf",
    "nrb_nepalqr_framework_2021": "https://www.nrb.org.np/contents/uploads/2021/02/Nepal-QR-Standardization-Framework-and-Guideline-2021.pdf",
    "nepalbank_merchant_form": "https://www.nepalbank.com.np/uploads/downloads/Fonepay_Merchant_Registration_Form.pdf",
    "nepalfinance_merchant_form": "https://www.nepalfinance.com.np/uploads/download/QR_merchant_registration_form.pdf",
    "shreefinance_merchant_form": "https://shreefinance.com.np/uploads/downloads/Fonepay_QR_merchant_registration.pdf",
    "reliancenepal_merchant_form": "https://reliancenepal.com.np/uploads/downloads/qr-merchant.pdf",
}

HTML_DIR = Path("data/fonepay/html")
PDF_DIR = Path("data/fonepay/pdf")
HTML_DIR.mkdir(parents=True, exist_ok=True)
PDF_DIR.mkdir(parents=True, exist_ok=True)


def download_html(name, url):
    dest = HTML_DIR / f"{name}.html"
    if dest.exists():
        print(f"  [SKIP] {name}.html already exists")
        return True
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        dest.write_bytes(r.content)
        print(f"  [OK]   {name}.html  ({len(r.content)//1024} KB)")
        return True
    except Exception as e:
        print(f"  [FAIL] {name} — {e}")
        return False


def download_pdf(name, url):
    dest = PDF_DIR / f"{name}.pdf"
    if dest.exists():
        print(f"  [SKIP] {name}.pdf already exists")
        return True
    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        dest.write_bytes(r.content)
        print(f"  [OK]   {name}.pdf  ({len(r.content)//1024} KB)")
        return True
    except Exception as e:
        print(f"  [FAIL] {name} — {e}")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("Fonepay Corpus Downloader")
    print("=" * 60)

    print("\n[1/2] Downloading HTML pages...")
    ok = fail = 0
    for name, url in HTML_PAGES.items():
        result = download_html(name, url)
        if result: ok += 1
        else: fail += 1
        time.sleep(0.5)  # be polite

    print(f"\n    HTML: {ok} succeeded, {fail} failed")

    print("\n[2/2] Downloading PDFs...")
    ok2 = fail2 = 0
    for name, url in PDF_PAGES.items():
        result = download_pdf(name, url)
        if result: ok2 += 1
        else: fail2 += 1
        time.sleep(1.0)

    print(f"\n    PDFs: {ok2} succeeded, {fail2} failed")
    print("\nDone! Run ingestion with:")
    print("  python -m app.ingestion.processor data/fonepay --wipe")
