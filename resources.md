# Fonepay RAG Corpus — Data Sources

> All links below are real, publicly accessible URLs sourced from fonepay.com's HTML, NRB, NCHL, and partner banks.
> Save all downloaded files into the `data/fonepay/` folder. Your existing processor handles PDF, HTML, DOCX, and TXT.

---

## Pillar 1: Merchant App & Product (User-Facing)

### Fonepay Website Pages (Save as .html)

| Description | URL |
|---|---|
| Business/Merchant Home | https://fonepay.com/business |
| Fonepay Business App | https://fonepay.com/business/app |
| Request Fonepay QR (Merchant Enrollment) | https://fonepay.com/business/merchant-enrollment |
| QR Payments (Customer) | https://fonepay.com/customers/qr-payment |
| Fonepay Direct (Fund Transfer) | https://fonepay.com/customers/fonepay-direct |
| Fonepay Bills | https://fonepay.com/customers/fonepay-bills |
| Fonepay App (Customer) | https://fonepay.com/customers/fonepay-app |
| FoneTAG (Tap & Pay) | https://fonepay.com/customers/fonetag |
| Fonepay Credit Card | https://fonepay.com/customers/fonepay-credit-card |
| Checkout by Fonepay | https://fonepay.com/customers/checkout-by-fonepay |
| Become a Partner | https://fonepay.com/partner |
| Business Academy | https://fonepay.com/partner/business-academy |
| About Fonepay | https://fonepay.com/about |
| Contact Us | https://fonepay.com/contact-us |
| FAQs | https://fonepay.com/faqs |

---

## Pillar 2: Legal, Policies & Fees (Business Operations)

### Fonepay Official Policy Pages (Save as .html)

| Description | URL |
|---|---|
| Terms and Conditions | https://fonepay.com/terms-and-conditions |
| Fees & Charges | https://fonepay.com/content/fees-and-charges |
| Information Security Policy | https://fonepay.com/content/information-security-policy |
| Settlement Options Terms | https://fonepay.com/content/settlement-options-terms |
| Cross Border Payments Terms | https://fonepay.com/content/cross-border-payments-terms-of-use |
| Fonepay Business App Privacy Policy | https://fonepay.com/content/business-app-privacy-policy |
| Fonepay App Privacy Policy | https://fonepay.com/content/privacy-policy |
| ESG Initiatives | https://fonepay.com/esg-initiatives |
| Publications | https://fonepay.com/publications |
| Downloads Page | https://fonepay.com/downloads |
| Reports (Investor Relations) | https://fonepay.com/reports |
| Notices | https://fonepay.com/notices |
| Blogs (all) | https://fonepay.com/blogs |

### Fonepay Official PDF Documents

| Description | URL |
|---|---|
| PCI-DSS Certification Document | https://fonepay.com/files/fonepay-pcidss.pdf |

---

## Pillar 3: Regulatory & Compliance (Banks / NRB / NCHL)

### Nepal Rastra Bank (NRB) — nrb.org.np

| Description | URL |
|---|---|
| NRB Payment Systems Department (browse for PDFs) | https://www.nrb.org.np/payment-systems-department/ |
| NRB NepalQR Standardization Framework 2021 | https://www.nrb.org.np/contents/uploads/2021/02/Nepal-QR-Standardization-Framework-and-Guideline-2021.pdf |
| NRB Gunaso (Complaint Portal) | https://gunaso.nrb.org.np/ |

### NCHL (Nepal Clearing House Ltd) — nchl.com.np

| Description | URL |
|---|---|
| NCHL Homepage (browse Rules & Guidelines) | https://www.nchl.com.np |
| NCHL NEPALPAY QR Operating Rules | https://www.nchl.com.np/downloads |

### Bank Merchant Registration Forms (PDF)

> These are real publicly hosted PDFs found on Nepali bank domains.

| Bank | Description | URL |
|---|---|---|
| Nepal Bank Limited | Fonepay QR Merchant Registration Form | https://www.nepalbank.com.np/uploads/downloads/Fonepay_Merchant_Registration_Form.pdf |
| Nepal Finance Ltd | QR Merchant Registration | https://www.nepalfinance.com.np/uploads/download/QR_merchant_registration_form.pdf |
| Shree Finance | Fonepay QR Merchant Registration | https://shreefinance.com.np/uploads/downloads/Fonepay_QR_merchant_registration.pdf |
| Reliance Finance Nepal | QR Merchant Registration | https://reliancenepal.com.np/uploads/downloads/qr-merchant.pdf |

---

## Bonus: Blogs (Fonepay News & Announcements)

| Description | URL |
|---|---|
| Fonepay Blog Listing | https://fonepay.com/blogs |
| Fonepay Reappoints CEO (Company News) | https://fonepay.com/blogs/fonepay-reappoints-mr-diwas-kumars-as-ceo-for-four-more-years |

---

## Instructions

1. **Download HTML pages:** Open each HTML URL in browser -> Right-click -> "Save as" -> "Webpage, HTML Only" -> save to `data/fonepay/html/`
2. **Download PDFs:** Click each PDF link -> browser will download it -> save to `data/fonepay/pdf/`
3. **Run ingestion:** `python -m app.ingestion.processor data/fonepay --wipe`

> The `--wipe` flag clears your current Qdrant collection and rebuilds it fresh from Fonepay data.
