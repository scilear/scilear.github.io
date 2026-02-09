# AGENTS.md - AlphAngel Website

This is a static GitHub Pages website for AlphAngel financial consulting.

## Project Structure

```
scilear.github.io/
├── index.html                    # Homepage
├── reports.html                  # Reports listing with password protection
├── wendyai-privacy.html          # Privacy policy
├── reports/                      # Report files
│   ├── morning-digestYYYYMMDD.html
│   └── investment_report-YYYY-MM-DD.html
├── CNAME                         # Custom domain config
├── SETUP.md                      # Setup instructions
└── readme.md                     # Project readme
```

## Technology Stack

- **Static HTML5** - No build system
- **Inline CSS** - Styles embedded in `<style>` tags
- **Vanilla JavaScript** - No frameworks
- **GitHub Pages** - Hosting

## Report File Naming Convention

Report files must follow these patterns:

```
reports/{name}{date}.html

Examples:
- morning-digest20260209.html    (YYYYMMDD format)
- investment_report-2026-02-04.html  (YYYY-MM-DD format)
```

## Code Style Guidelines

### HTML
- Use semantic HTML5 elements (`<header>`, `<main>`, `<section>`, `<footer>`)
- Include meta tags: charset, viewport, description, keywords
- Use double quotes for attributes
- Indent with 4 spaces
- Add comments for major sections: `<!-- Section Name -->`

### CSS
- Inline styles in `<style>` tags within `<head>`
- Use CSS custom properties for colors (defined at `:root`)
- Prefer `rem` units for spacing, `px` for borders
- Use kebab-case for class names: `.report-card`, `.password-overlay`
- Mobile-first responsive design with `@media (max-width: 768px)`
- Color scheme: `#13585b` (primary), `#0c8389` (secondary)

### JavaScript
- Use ES6+ features (const/let, arrow functions, async/await)
- Indent with 4 spaces
- Use single quotes for strings
- Handle errors with try/catch blocks
- Use `sessionStorage` for authentication state
- Hash passwords with SHA-256 before comparison

### Security
- Never commit plaintext passwords
- Store SHA-256 hashes for password verification
- Use `sessionStorage` (not `localStorage`) for auth tokens
- Hash: `655eeee212cf8682e419f524b66e07cdd2d56306399f7f615f9cfb7dba2ad37d`

## Git Workflow

```bash
# Make changes
git add <files>
git commit -m "Description of changes"
git push origin main

# GitHub Pages auto-deploys from main branch
```

## Adding New Reports

1. Create report HTML file following naming convention
2. Add to `/reports/` directory
3. Include password protection script at bottom:

```html
<script>
const CORRECT_HASH = "655eeee212cf8682e419f524b66e07cdd2d56306399f7f615f9cfb7dba2ad37d";
async function sha256(message) {
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest("SHA-256", msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
}
if (sessionStorage.getItem("reportsAuthenticated") !== CORRECT_HASH) {
    const password = prompt("This report is password protected. Enter password:");
    if (password) {
        sha256(password).then(inputHash => {
            if (inputHash === CORRECT_HASH) {
                sessionStorage.setItem("reportsAuthenticated", CORRECT_HASH);
            } else {
                alert("Incorrect password");
                window.location.href = "../reports.html";
            }
        });
    } else {
        window.location.href = "../reports.html";
    }
}
</script>
```

4. Commit and push - reports.html auto-detects new files

## Testing

No automated tests. Manual testing:

1. Open files in browser
2. Test responsive design (resize window)
3. Test password protection flow
4. Verify reports load in reports.html

## SEO Requirements

- Include `<meta name="description">` (max 160 chars)
- Include `<meta name="keywords">`
- Use semantic heading hierarchy (h1 > h2 > h3)
- Add alt text to all images
- Use descriptive link text

## External Dependencies

Allowed external resources:
- Logo images from `https://solvefortime.com/`
- Google Fonts (if needed)
- GitHub API for dynamic report listing

No npm packages or build tools required.
