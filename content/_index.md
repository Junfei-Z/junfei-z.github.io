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
              <span class="news-mo">Aug</span>
              <span class="news-day">21</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-paper">Paper accepted</span>
                <span class="news-venue">EMNLP 2026</span>
              </div>
              <p class="news-title">"Trains but Doesn’t Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers" was accepted to <em>The 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026)</em>.</p>
              <p class="news-meta">With <b>Weihang Ding</b>. Sincere thanks to Weihang for his tremendous effort on this work.</p>
            </div>
          </li>

          <li class="news-item itm-paper">
            <div class="news-date">
              <span class="news-mo">Jul</span>
              <span class="news-day">10</span>
              <span class="news-yr">2026</span>
            </div>
            <div class="news-body">
              <div class="news-tags">
                <span class="news-tag t-paper">Paper accepted</span>
                <span class="news-venue">ACM MM 2026</span>
              </div>
              <p class="news-title">"Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference" was accepted to <em>The 34th ACM International Conference on Multimedia (ACM MM 2026)</em>.</p>
              <p class="news-meta">With <b>Haoxun Shen</b>, <b>Mingang Guo</b>, <b>Zixuan Huang</b>, and <b>Prof. Tengjiao He</b>. Sincere thanks to Prof. He for his guidance.</p>
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
                <span class="news-tag t-journal">Journal accepted</span>
                <span class="news-venue">IEEE Internet of Things Journal</span>
              </div>
              <p class="news-title">"Orchestrating Data Collection and Computation in Green IoT Networks" was accepted by the <em>IEEE Internet of Things Journal</em>.</p>
              <p class="news-meta">With <b>Prof. Fei Song</b>, <b>Prof. Tengjiao He</b>, <b>Prof. Kwan-Wu Chin</b>, and <b>Benyu Chen</b>. Sincere thanks to Prof. He and Prof. Chin for their guidance.</p>
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
              <p class="news-meta">With <b>Prof. Tengjiao He</b>. Sincere thanks to Prof. He for his close guidance throughout, and <b>Benyu</b> for all the support.</p>
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
      title: Publications
      text: |
        <div class="pub-block">
        <ul class="pub-list">

          <li class="pub-item">
            <div class="pub-side">
              <span class="pub-badge pb-conf">EMNLP</span>
              <span class="pub-year">2026</span>
            </div>
            <div class="pub-main">
              <p class="pub-title">Trains but Doesn’t Learn: A Post-Training Delivery Benchmark for LLM Agents as Forward-Deployed Engineers</p>
              <p class="pub-authors">W. Ding, <b>J. Zhan</b></p>
              <p class="pub-venue">Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP), 2026. To appear</p>
            </div>
          </li>

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
        <p class="pub-more">For the latest publications, please follow my <a href="https://scholar.google.com/citations?user=v2doypQAAAAJ&hl=en" target="_blank">Google Scholar</a>.</p>
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
