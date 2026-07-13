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
              <span class="news-mo">Jul</span>
              <span class="news-day">10</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-paper">论文录用</span>
                <span class="news-venue">ACM MM 2026</span>
              </div>
              <p class="news-title">论文「Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference」被 <em>The 34th ACM International Conference on Multimedia (ACM MM 2026)</em> 录用。</p>
              <p class="news-meta">合作者：<b>Haoxun Shen</b>、<b>Mingang Guo</b>、<b>Zixuan Huang</b>、<b>Prof. Tengjiao He</b>。诚挚感谢何老师的悉心指导。</p>
            </div>
          </li>

          <li class="news-item itm-journal">
            <div class="news-date">
              <span class="news-mo">May</span>
              <span class="news-day">10</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-journal">期刊录用</span>
                <span class="news-venue">IEEE Internet of Things Journal</span>
              </div>
              <p class="news-title">论文「Orchestrating Data Collection and Computation in Green IoT Networks」被 <em>IEEE Internet of Things Journal</em> 录用。</p>
              <p class="news-meta">合作者：<b>Prof. Fei Song</b>、<b>Prof. Tengjiao He</b>、<b>Prof. Kwan-Wu Chin</b>、<b>Benyu Chen</b>。诚挚感谢何老师与 Chin 老师的悉心指导。</p>
            </div>
          </li>

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

          <li class="news-item itm-journal">
            <div class="news-date">
              <span class="news-mo">Feb</span>
              <span class="news-day">13</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-journal">期刊录用</span>
                <span class="news-venue">IEEE Internet of Things Journal</span>
              </div>
              <p class="news-title">合作论文「Joint Function Configuration and Multislot Offloading in Solar-Powered Serverless Edge Computing」被 <em>IEEE Internet of Things Journal</em> 录用。</p>
              <p class="news-meta">合作者：<b>Prof. Tengjiao He</b>。诚挚感谢何老师一直以来的细致指导和 <b>Benyu</b>的支持。</p>
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

        </ul>
        </div>
    design:
      columns: '1'

  - block: markdown
    content:
      title: 论文发表
      text: |
        <div class="pub-block">
        <ul class="pub-list">

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-conf">ACM MM</span>
              <span class="pub-year">2026</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference</p>
              <p class="pub-authors"><b>J. Zhan</b>, H. Shen, M. Guo, Z. Huang, T. He</p>
              <p class="pub-venue">Proceedings of the 34th ACM International Conference on Multimedia (ACM MM), 2026. To appear · arXiv:2607.09520</p>
            </div>
          </li>

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-conf">AAAI</span>
              <span class="pub-year">2026</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">PRISM: Privacy-Aware Routing for Adaptive Cloud&ndash;Edge LLM Inference via Semantic Sketch Collaboration</p>
              <p class="pub-authors"><b>J. Zhan</b>, H. Shen, Z. Lin, T. He</p>
              <p class="pub-venue">Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), 2026</p>
            </div>
          </li>

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-journal">IoT-J</span>
              <span class="pub-year">2026</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">Orchestrating Data Collection and Computation in Green IoT Networks</p>
              <p class="pub-authors"><b>J. Zhan</b>, T. He, K.-W. Chin, B. Chen, F. Song</p>
              <p class="pub-venue">IEEE Internet of Things Journal, 2026</p>
            </div>
          </li>

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-journal">IoT-J</span>
              <span class="pub-year">2026</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">Joint Function Configuration and Multi-Slot Offloading in Solar-Powered Serverless Edge Computing</p>
              <p class="pub-authors">B. Chen, T. He, M. Zheng, <b>J. Zhan</b>, B. He</p>
              <p class="pub-venue">IEEE Internet of Things Journal, 2026</p>
            </div>
          </li>

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-conf">ICASSP</span>
              <span class="pub-year">2026</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">SpikeBP: Efficient Spike-Driven Transformer for Blood Pressure Waveform Generation with Frequency Knowledge Distillation</p>
              <p class="pub-authors">Z. Huang, Z. Wang, W. Qiu, <b>J. Zhan</b>, S. Zou, Y. Li, F. Miao</p>
              <p class="pub-venue">IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2026 · Oral</p>
            </div>
          </li>

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-poster">MobiSys</span>
              <span class="pub-year">2026</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">Poster: Graph Learning-based Update Manipulation Attack on Federated Fine-Tuning of LLMs over Wireless Networks</p>
              <p class="pub-authors">H. Cai, <b>J. Zhan</b>, Z. Lin, X. Cai</p>
              <p class="pub-venue">Proceedings of the 24th ACM International Conference on Mobile Systems, Applications, and Services (MobiSys Posters), 2026</p>
            </div>
          </li>

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-conf">SMC</span>
              <span class="pub-year">2025</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">RL-Enhanced Disturbance-Aware MPC for Fast and Robust UAV Trajectory Tracking</p>
              <p class="pub-authors">H. Shen, <b>J. Zhan</b>, T. He</p>
              <p class="pub-venue">IEEE International Conference on Systems, Man, and Cybernetics (SMC), 2025</p>
            </div>
          </li>

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-journal">IEEE LNET</span>
              <span class="pub-year">2024</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">Task Offloading and Approximate Computing in Solar Powered IoT Networks</p>
              <p class="pub-authors"><b>J. Zhan</b>, J. Wu, T. He, K.-W. Chin</p>
              <p class="pub-venue">IEEE Networking Letters, 6(1), 26&ndash;30, 2024</p>
            </div>
          </li>

        </ul>
        <p class="pub-more">最新的具体出版物，请关注我的<a href="https://scholar.google.com/citations?user=v2doypQAAAAJ&hl=en" target="_blank">谷歌学术主页</a>。</p>
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
