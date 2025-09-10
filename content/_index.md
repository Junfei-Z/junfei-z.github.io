---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
    design:
      css_class: system
      background:
        image:
          # Add your image background to `assets/media/`.
          filename: 
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  
  - block: markdown
    content:
      title: Visitor Map
      text: |
        <div style="text-align: center; margin: 40px 0;">
          <script type="text/javascript" src="//rf.revolvermaps.com/0/0/8.js?i=5x3ebj080sx&amp;m=0&amp;c=ff0000&amp;cr1=ffffff&amp;f=arial&amp;l=33" async="async"></script>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['20px', '0', '20px', '0']
---
