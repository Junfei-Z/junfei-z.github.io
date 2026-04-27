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
      title: News
      text: |
        <div class="news-block">
        <ul class="news-list">

          <li class="news-item itm-paper">
            <div class="news-date">
              <span class="news-mo">Apr</span>
              <span class="news-day">27</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-paper">Paper accepted</span>
                <span class="news-venue">MobiSys '26 Posters</span>
              </div>
              <p class="news-title">"Graph Learning-based Update Manipulation Attack on Federated Fine-Tuning of LLMs over Wireless Networks" was accepted to <em>The 24th ACM International Conference on Mobile Systems, Applications, and Services (MobiSys '26 Posters)</em>.</p>
              <p class="news-meta">With <b>Hanlin Cai</b> (Cambridge), <b>Zheng Lin</b> (HKU), and <b>Xinyi Cai</b> (Cambridge). Many thanks to Hanlin for leading the collaboration.</p>
            </div>
          </li>

          <li class="news-item itm-award">
            <div class="news-date">
              <span class="news-mo">Apr</span>
              <span class="news-day">24</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-award">Award</span>
                <span class="news-venue">University of Pennsylvania · ESE Department</span>
              </div>
              <p class="news-title">Received the <b>2026 ESE Department Master's Top 10% GPA Award</b> for outstanding academic performance.</p>
            </div>
          </li>

          <li class="news-item itm-journal">
            <div class="news-date">
              <span class="news-mo">Feb</span>
              <span class="news-day">13</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-journal">Journal accepted</span>
                <span class="news-venue">IEEE Internet of Things Journal</span>
              </div>
              <p class="news-title">"Joint Function Configuration and Multislot Offloading in Solar-Powered Serverless Edge Computing" was accepted by the <em>IEEE Internet of Things Journal</em>.</p>
              <p class="news-meta">With <b>Prof. Tengjiao He</b>. Sincere thanks to Prof. He and <b>Benyu</b> for their close guidance throughout.</p>
            </div>
          </li>

          <li class="news-item itm-oral">
            <div class="news-date">
              <span class="news-mo">Jan</span>
              <span class="news-day">16</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-oral">Oral</span>
                <span class="news-venue">IEEE ICASSP 2026</span>
              </div>
              <p class="news-title">"SpikeBP: Efficient Spike-Driven Transformer for Blood Pressure Waveform Generation with Frequency Knowledge Distillation" was selected for <b>oral presentation</b> at IEEE ICASSP 2026.</p>
              <p class="news-meta">Many thanks to <b>Zixuan</b> for leading this work.</p>
            </div>
          </li>

        </ul>
        </div>
    design:
      columns: '1'

  - block: markdown
    content:
      title: ""
      text: |
        {{< visitor-globe >}}
    design:
      columns: '1'
  
---
