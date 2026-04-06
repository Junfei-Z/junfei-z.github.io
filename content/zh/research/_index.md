---
title: Research
summary: My research
type: landing

cascade:
  - _target:
      kind: page
    params:
      show_breadcrumb: true

sections:
  - block: collection
    id: research
    content:
      title: Research
      filters:
        folders:
          - research
      count: 0            # 0=展示全部，解决只显示5个的问题
      exclude_featured: false
      exclude_past: false
      exclude_future: false
    design:
      view: article-grid
      columns: 3
      show_button: false  # 去掉“See all”按钮
---
