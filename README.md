# Property Snaps Website

Official Property Snaps website source for propertysnaps.com.au and www.propertysnaps.com.au.

- **Market:** Casey and Cardinia, south-east Melbourne, Victoria
- **Netlify site:** `propertysnaps` (existing project)
- **Platform:** Static HTML/CSS/JavaScript, no Node build required
- **Content:** Service pages, industry pages, suburb pages, portfolio galleries, enquiry forms and downloadable PDF guides
- **Public pricing:** None

## Deploy with GitHub and Netlify

1. Create a GitHub repository named `propertysnaps-website` (do not initialise with a README or `.gitignore`).
2. Push this site's `main` branch to that repository.
3. Open **Netlify → propertysnaps → Project configuration → Build & deploy → Continuous deployment → Link repository**.
4. Select the new `propertysnaps-website` repository and branch `main`.
5. Set publish directory to `.` (or let Netlify read `netlify.toml`); leave build command blank.
6. Verify the deploy is **Published**, then check https://www.propertysnaps.com.au, gallery, contact form and PDF downloads.

**Note:** Do not create a second Netlify project. Link the new repository to the existing `propertysnaps` project.

## Forms

The built pages include forms that are configured for Netlify Forms. After first successful production deployment, check the **Forms** section in Netlify and submit a test enquiry.

## Before launch

Confirm the current business phone number and email, as some historical source details are from older marketing collateral. Replace generated gallery images with verified project photography when available. Keep pages free of public pricing.
