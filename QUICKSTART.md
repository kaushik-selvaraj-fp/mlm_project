# Smart Campus Security System - Quick Reference

## 🎯 Project At a Glance

**Course:** Multimodal Machine Learning (21AIE541T)  
**Team Size:** 2-3 students  
**Workload:** ~20-30 hours  
**Max Score:** 100 marks

---

## 📦 What You Get

### Files Created:
- **SCS_main.ipynb** - Main executable notebook (600+ lines)
- **README.md** - Comprehensive guide with setup instructions
- **DATA_COLLECTION_GUIDE.md** - Image collection instructions
- **setup.py** - Automated setup script
- **QUICKSTART.md** - This file

### Generated Outputs:
- Visualizations (heatmaps, charts)
- Results table (CSV)
- System report (TXT)

---

## ⚡ Quick Start (5 minutes)

### 1. Setup Project
```bash
# Navigate to project directory
cd c:\mycode\mlm_project

# Run setup script
python setup.py

# Creates directories and checks dependencies
```

### 2. Collect Images (30 minutes)
- **Enrollment:** 5+ people × 2-3 photos = 10-15 images
- **Scenarios:** 10+ diverse campus activities
- **Test:** 10+ new images (different from enrollment)

See [DATA_COLLECTION_GUIDE.md](DATA_COLLECTION_GUIDE.md) for details.

### 3. Run Notebook (10 minutes execution)
```bash
# Start Jupyter
jupyter notebook

# Open SCS_main.ipynb
# Update team info at the top
# Execute: Kernel → Restart & Run All
# Wait for outputs
```

### 4. Review Results (5 minutes)
- Check console output for logs
- View images in `outputs/visualizations/`
- Review table in `outputs/results/security_results.csv`

---

## 📊 Project Modules

| Module | Task | Model | Score | Lines |
|--------|------|-------|-------|-------|
| **1** | Face Recognition | InsightFace | 15 | ~80 |
| **2** | Scene Captioning | BLIP | 15 | ~60 |
| **3** | Activity Check | CLIP | 15 | ~70 |
| **4** | Fusion & Alert | Hard-coded | 20 | ~100 |
| **Analysis** | Failure cases + improvements | - | 15 | ~50 |
| **Code Quality** | Comments, visualization, organization | - | 10 | ~600 |
| **Creativity** | Bonus extensions | - | 10 | Variable |

---

## 📸 Data Requirements

### Enrollment (Minimum)
```
enrolled_faces/
├── person_1.jpg
├── person_2.jpg
├── person_3.jpg
├── person_4.jpg
└── person_5.jpg
```
- **Count:** 5+ people, 2-3 photos each
- **Quality:** Clear face, well-lit, good resolution
- **Naming:** [person_name].jpg

### Scenarios (Minimum)
```
scenario_images/
├── scenario_01.jpg  → lab work
├── scenario_02.jpg  → whiteboard
├── scenario_03.jpg  → collaboration
├── scenario_04.jpg  → reading
├── scenario_05.jpg  → eating (unauth)
├── scenario_06.jpg  → sleeping (unauth)
├── scenario_07.jpg  → photography (unauth)
├── scenario_08.jpg  → phone use
├── scenario_09.jpg  → empty lab
└── scenario_10.jpg  → multiple people
```
- **Count:** 10+ diverse scenarios
- **Mix:** Authorized + Unauthorized + Edge cases
- **Naming:** scenario_XX.jpg (any format)

### Test (Minimum)
```
test_images/
├── test_01.jpg
├── test_02.jpg
├── test_03.jpg
└── test_10_plus.jpg
```
- **Count:** 10+ new images (NOT in enrollment)
- **Mix:** Enrolled + Unknown, Authorized + Unauthorized
- **Quality:** Same as scenario images

---

## 🔑 Key Code Classes

```python
# Module 1
face_module = FaceIdentityModule()
enrolled = face_module.enroll_faces('enrolled_faces')
identity, confidence = face_module.identify_face(image, enrolled)

# Module 2
caption_module = SceneCaptioningModule()
caption = caption_module.generate_caption(image)

# Module 3
activity_module = ActivityAuthorizationModule()
allowed, disallowed = activity_module.define_activities()
status, score, dict, label = activity_module.classify_activity(
    image, allowed, disallowed
)

# Module 4
fusion_module = FusionAlertModule()
alert, message = fusion_module.security_decision(
    identity, conf, caption, status, score
)
result = fusion_module.end_to_end_pipeline(image_path, ...)
```

---

## 📈 Expected Results

### Similarity Matrix (Module 1)
- Shows face distances between enrolled people
- Diagonal = 1.0 (distance to self)
- Off-diagonal = cosine similarity scores
- **Good:** High diagonal, low off-diagonal

### CLIP Scores (Module 3)
- Allowed activities: Higher scores for authorized activities
- Disallowed activities: Lower scores for unauthorized activities
- **Good:** Clear separation between allowed/disallowed

### Alert Distribution (Module 4)
- **GREEN:** Known person + Authorized activity (majority)
- **YELLOW:** Known person + Suspicious OR Uncertain identity
- **RED:** Unknown person (security alert)
- **Expected:** ~50% GREEN, ~40% YELLOW, ~10% RED (varies)

### Results Table
```
Image            | Identity    | Confidence | Scene Caption              | Activity Status | Alert
scenario_01.jpg  | student_A   | 0.876     | person working on computer | AUTHORIZED     | GREEN
scenario_05.jpg  | student_B   | 0.823     | person eating food in lab  | UNAUTHORIZED   | YELLOW
scenario_07.jpg  | UNKNOWN     | 0.189     | person taking photos       | UNAUTHORIZED   | RED
```

---

## ✅ Submission Checklist

Before submitting, verify:

- [ ] **Notebook Execution**
  - [ ] All cells executed
  - [ ] All outputs visible
  - [ ] No errors in console

- [ ] **Data**
  - [ ] 5+ people enrolled
  - [ ] 10+ scenario images
  - [ ] 10+ test images
  - [ ] All images in correct directories

- [ ] **Modules**
  - [ ] Module 1: Face similarity matrix shown
  - [ ] Module 2: Captions for all scenarios shown
  - [ ] Module 3: CLIP scores and bar charts shown
  - [ ] Module 4: Results table with alerting shown

- [ ] **Analysis**
  - [ ] Identified 3+ failure cases
  - [ ] Explained why each failed
  - [ ] Proposed improvements
  - [ ] Written in clear language

- [ ] **Code Quality**
  - [ ] Well-organized sections
  - [ ] Functions documented with docstrings
  - [ ] Proper variable naming
  - [ ] Comments for complex logic

- [ ] **Team Info**
  - [ ] Team name at top
  - [ ] Member names and roll numbers
  - [ ] All members' contributions noted

- [ ] **Files**
  - [ ] SCS_main.ipynb (single notebook file)
  - [ ] All outputs generated
  - [ ] Results saved to CSV

---

## 🛠️ Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| InsightFace not loading | Model download failed | Internet connection + disk space |
| Out of Memory (OOM) | Model too large | Use CPU or smaller batch sizes |
| Face not detected | Poor lighting/angle | Take better enrollment photos |
| CLIP scores random | Labels too vague | Make activity descriptions more specific |
| Python package errors | Missing/conflicting versions | Run `python setup.py` again |
| Notebook won't run | Kernel crashed | Restart kernel (Kernel → Restart & Clear) |

---

## 📚 Important Concepts

### Late Fusion (Module 4)
```
Decision based on: identity_score + activity_status
If identity_score > 0.4 AND activity=='AUTHORIZED' → GREEN
If identity_score > 0.4 AND activity=='UNAUTHORIZED' → YELLOW
If identity_score < 0.3 → RED (unknown)
```

### Activity Labels (Module 3)
- **Specific > Generic:** "person typing on keyboard" better than "working"
- **Context matters:** "working on computer" vs "taking photos"
- **7-8 label pairs:** Enough coverage, manageable complexity

### Face Embeddings (Module 1)
- **512-dim vector** representing unique facial features
- **Cosine similarity** measures distance: 0 (different) to 1 (identical)
- **Threshold ~0.4-0.5** for matching (depends on images)

---

## 🎓 Learning Outcomes

After completing this project, you will understand:

1. ✓ How to use CLIP for zero-shot classification
2. ✓ How BLIP generates image captions
3. ✓ How InsightFace extracts face embeddings
4. ✓ How to combine multiple ML models in a pipeline
5. ✓ Late fusion strategy for multimodal learning
6. ✓ Building end-to-end ML systems
7. ✓ Evaluating and improving ML systems

---

## 📞 Support Resources

### In Notebook:
- Docstrings in every class/function
- Detailed comments explaining logic
- Regular print statements showing progress

### External:
- README.md - Comprehensive guide
- DATA_COLLECTION_GUIDE.md - Image collection
- setup.py - Dependency installation

### If Stuck:
1. Check console error messages
2. Verify image directories have correct files
3. Ensure image quality is good
4. Check internet connection (for model downloads)
5. Try installing packages manually: `pip install [package]`

---

## ⏱️ Time Estimate

| Task | Time |
|------|------|
| Setup & reading | 15 min |
| Collecting images | 30-45 min |
| Running notebook | 10-20 min |
| Analyzing results | 15-20 min |
| Writing failure cases | 20-30 min |
| Total | 90-150 min |

**Recommended:** Start early, collect good quality images, iterate on improvements.

---

## 💡 Tips for Success

1. **Image Quality:** Good lighting and clear faces = better results
2. **Diverse Scenarios:** Mix authorized + unauthorized for evaluation
3. **Clear Labels:** Specific activity descriptions > generic ones
4. **Analyze Failures:** That's where real learning happens
5. **Document Everything:** Comments help grading + your understanding
6. **Bonus Extensions:** Shows deeper understanding (extra 10 points)

---

## 🚀 Next Steps

1. **NOW:** Run `python setup.py` to initialize project
2. **SOON:** Read DATA_COLLECTION_GUIDE.md
3. **THEN:** Collect your images
4. **FINALLY:** Open browser to notebook and press "Run All"

**Questions?** Check README.md or your course materials.

**Good luck! Build something impressive! 🎯**

---

Last Updated: March 28, 2026  
Course: 21AIE541T - Multimodal Machine Learning  
Institution: VIT Chennai
