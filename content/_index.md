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
      title: ""
      text: |
        <div style="text-align: center; padding: 40px 0;">
          <a href="https://clustrmaps.com/site/1c1r7" title="Visit tracker">
            <img src="//www.clustrmaps.com/map_v2.png?d=Jt8x0LRoUsM3933STN7ojMVodayS1v9s5VQdU-YmKa4&cl=ffffff" alt="Visitor Map" style="border: 0px;" />
          </a>
        </div>
    design:
      columns: '1'
  
---
