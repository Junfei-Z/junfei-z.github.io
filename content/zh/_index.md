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
      title: 动态
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
                <span class="news-tag t-paper">论文录用</span>
                <span class="news-venue">MobiSys '26 Posters</span>
              </div>
              <p class="news-title">合作论文「Graph Learning-based Update Manipulation Attack on Federated Fine-Tuning of LLMs over Wireless Networks」被 <em>The 24th ACM International Conference on Mobile Systems, Applications, and Services (MobiSys '26 Posters)</em> 录用。</p>
              <p class="news-meta">合作者：<b>Hanlin Cai</b>（剑桥大学）、<b>Zheng Lin</b>（香港大学）、<b>Xinyi Cai</b>（剑桥大学）。特别感谢 Hanlin 牵头这次合作。</p>
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
                <span class="news-tag t-award">奖项</span>
                <span class="news-venue">宾夕法尼亚大学 · ESE 系</span>
              </div>
              <p class="news-title">获 <b>2026 ESE Department Master's Top 10% GPA Award</b>，表彰在硕士阶段的学术表现。</p>
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
                <span class="news-tag t-oral">口头报告</span>
                <span class="news-venue">IEEE ICASSP 2026</span>
              </div>
              <p class="news-title">合作论文「SpikeBP: Efficient Spike-Driven Transformer for Blood Pressure Waveform Generation with Frequency Knowledge Distillation」被 IEEE ICASSP 2026 选为 <b>口头报告（Oral）</b>。</p>
              <p class="news-meta">特别感谢 <b>Zixuan</b> 牵头主导这项工作。</p>
            </div>
          </li>

          <li class="news-item itm-journal">
            <div class="news-date">
              <span class="news-mo">Jan</span>
              <span class="news-day">07</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-journal">期刊</span>
                <span class="news-venue">IEEE Internet of Things Journal</span>
              </div>
              <p class="news-title">合作论文「Orchestrating Data Collection and Computation in Green IoT Networks」进入 <em>IEEE Internet of Things Journal</em> 评审环节（稿件号 IoT-59139-2025）。</p>
              <p class="news-meta">合作者：宋飞 教授、<b>Tengjiao He</b>、Kwan-Wu Chin、Benyu Chen。诚挚感谢 何老师 一直以来的细致指导。</p>
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
