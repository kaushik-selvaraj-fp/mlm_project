# Smart Campus Security System
## Multimodal Machine Learning (21AIE541T)

A comprehensive security system combining **Face Recognition**, **Scene Understanding**, **Activity Detection**, using multimodal fusion techniques.

---

## 📋 Project Overview

**Objective:** Build a smart campus security pipeline that:
1. **Identifies WHO** - Recognizes authorized personnel via face recognition (InsightFace)
2. **Understands WHAT** - Generates scene descriptions (BLIP/Qwen VL)
3. **Determines IF AUTHORIZED** - Checks activities against policies (CLIP)
4. **Makes FINAL DECISION** - Combines all signals via late fusion + alerts

**Architecture:**
```
Camera Image
    ↓
┌─────────────────────────────────┐
│ Module 1: Face Recognition      │
│ (InsightFace/ArcFace)           │
│ → Output: Identity + Confidence │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Module 2: Scene Captioning      │
│ (BLIP/Qwen VL)                  │
│ → Output: Scene Description     │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Module 3: Activity Check        │
│ (CLIP)                          │
│ → Output: Authorized/Not        │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ Module 4: Fusion & Alert        │
│ (Late Fusion)                   │
│ → Output: Alert Level + Message │
└─────────────────────────────────┘
```

---

## 📦  Project Structure

```
mlm_project/
├── SCS_main.ipynb                 # Main notebook (RUN THIS!)
├── README.md                       # This file
├── enrolled_faces/                 # Directory for enrollment photos (5+ people)
│   ├── student_A.jpg              # Example: your photos here
│   ├── student_B.jpg
│   ├── professor_X.jpg
│   ├── staff_Y.jpg
│   └── visitor_Z.jpg
├── scenario_images/               # Directory for campus scenario photos (10+)
│   ├── scenario_01.jpg            # Lab work
│   ├── scenario_02.jpg            # Whiteboa rd discussion
│   ├── scenario_03.jpg            # Group project
│   ├── scenario_04.jpg            # Unauthorized eating
│   ├── scenario_05.jpg            # Person sleeping
│   ├── scenario_06.jpg            # Photography
│   ├── scenario_07.jpg            # Phone usage
│   ├── scenario_08.jpg            # Empty lab
│   ├── scenario_09.jpg            # Two people talking
│   └── scenario_10.jpg            # Additional scenario
├── test_images/                   # Directory for test images (10+)
│   ├── test_01.jpg                # New test images (not in enrollment)
│   ├── test_02.jpg
│   └── ...
└── outputs/                       # Generated outputs
    ├── visualizations/
    │   ├── similarity_matrix.png   # Face enrollment heatmap
    │   ├── activity_scores.png     # CLIP score distributions
    │   └── alert_distribution.png  # Alert statistics
    └── results/
        ├── security_results.csv    # Final results table
        └── system_report.txt       # System summary report
```

---

## 🚀 Quick Start

### Step 1: Install Dependencies

```bash
# Install required packages
pip install jupyter insightface torch torchvision transformers pillow opencv-python scikit-learn pandas numpy matplotlib scipy requests

# Or for conda users:
conda install -c conda-forge insightface pytorch::pytorch pytorch::torchvision transformers pillow opencv pandas scikit-learn matplotlib scipy
```

### Step 2: Collect Data

#### 2a. Enrollment Images (5+ people)
- Create directory: `enrolled_faces/`
- Collect **2-3 photos per person** (clear face, different angles/lighting)
- Save as: `enrolled_faces/[person_name].jpg`
- Example:
  ```
  enrolled_faces/
  ├── student_A.jpg
  ├── student_B.jpg
  ├── professor_X.jpg
  ├── staff_Y.jpg
  └── visitor_Z.jpg
  ```

#### 2b. Campus Scenario Images (10+ diverse scenarios)
- Create directory: `scenario_images/`
- Capture different activities in your lab/classroom:
  - ✓ Person working on computer
  - ✓ Person writing on whiteboard
  - ✓ Group discussion/collaboration
  - ✓ Person reading
  - ✓ Person eating (unauthorized)
  - ✓ Person sleeping (unauthorized)
  - ✓ Person taking photos (unauthorized)
  - ✓ Person using phone
  - ✓ Empty lab
  - ✓ Two people talking
- Save as: `scenario_images/scenario_01.jpg`, `scenario_images/scenario_02.jpg`, etc.

#### 2c. Test Images (10+ new images)
- Create directory: `test_images/`
- Collect **new photos NOT in enrollment set**
- Different scenarios, angles, lighting conditions
- Save as: `test_images/test_01.jpg`, `test_images/test_02.jpg`, etc.

### Step 3: Run the Notebook

```bash
# Start Jupyter
jupyter notebook

# Open SCS_main.ipynb
# Execute all cells (Kernel → Restart & Run All)
# Wait for all outputs to generate (~5-10 minutes depending on GPU)
```

### Step 4: Review Results

After execution, check:
- **Console output** - Real-time processing logs
- **Visualizations** - `outputs/visualizations/`
  - Face similarity heatmap
  - CLIP activity scores
  - Alert distribution charts
- **Results Table** - `outputs/results/security_results.csv`
  - Image, Identity, Confidence, Caption, Activity Status, Alert Level

---

## 📊 Evaluation Criteria (100 marks)

| Component | Marks | Requirements |
|-----------|-------|--------------|
| **Module 1: Face Recognition** | 15 | ✓ Correct enrollment ✓ Similarity matrix ✓ Identification accuracy |
| **Module 2: Scene Captioning** | 15 | ✓ BLIP/Qwen VL used ✓ Meaningful captions ✓ 10+ scenarios |
| **Module 3: Activity Classification** | 15 | ✓ CLIP scoring ✓ Well-designed labels ✓ Bar charts |
| **Module 4: Fusion & Alert** | 20 | ✓ Fusion logic ✓ Alert levels ✓ End-to-end demo |
| **Analysis & Discussion** | 15 | ✓ 3+ failure cases ✓ Why they failed ✓ Improvements |
| **Code Quality & Presentation** | 10 | ✓ Clean code ✓ Comments ✓ Visualizations ✓ Organization |
| **Creativity/Extensions** | 10 | ✓ Bonus features (optional) |
| **TOTAL** | **100** | - |

---

## 📝 Submission Checklist

Before submitting, ensure:

- [ ] Team info filled at top of notebook (Team Name, Members, Roll Numbers)
- [ ] At least 5 people enrolled with face photos
- [ ] At least 10 campus scenario images processed
- [ ] At least 10 test images processed with results
- [ ] All cells executed with visible outputs
- [ ] Results table shows: Image, Identity, Confidence, Caption, Activity, Alert
- [ ] 3+ failure cases analyzed with explanations
- [ ] Visualizations generated (similarity matrix, activity scores, alerts)
- [ ] Code is clean and well-commented
- [ ] Results saved to `outputs/results/security_results.csv`

---

## 🔧 Notebook Sections Explained

### Section 1: Imports & Setup
- Install and import all required libraries
- Check GPU availability
- Set up paths

### Section 2: Utility Functions
- Image loading/saving functions
- Visualization helpers
- Project directory creation

### Section 3: Module 1 - Face Recognition
- Initialize InsightFace model
- Define `FaceIdentityModule` class
- Methods: `get_face_embedding()`, `enroll_faces()`, `identify_face()`, `similarity_matrix()`

### Section 4: Module 2 - Scene Understanding
- Initialize BLIP model
- Define `SceneCaptioningModule` class
- Methods: `generate_caption()`, `caption_batch()`, `caption_from_directory()`

### Section 5: Module 3 - Activity Authorization
- Initialize CLIP model
- Define `ActivityAuthorizationModule` class
- Methods: `define_activities()`, `classify_activity()`, `plot_activity_scores()`

### Section 6: Module 4 - Fusion & Alert
- Define `FusionAlertModule` class
- Methods: `security_decision()`, `end_to_end_pipeline()`, `batch_process()`
- Implements late fusion logic with 4 decision cases

### Sections 7-11: System Execution
- Initialize all modules
- Enroll faces + show similarity matrix
- Generate scene captions
- Classify activities
- Run end-to-end pipeline on test images
- Display results table

### Sections 12-15: Analysis & Conclusions
- Analyze 3+ failure cases
- Discuss improvements
- Document bonus extensions
- Generate final report

---

## 🎯 Key Features

### ✅ Multi-Module Architecture
- **Modular design** - Each module independent, can swap models
- **Graceful degradation** - Works even if some models fail
- **Mock implementations** - Demo mode when models unavailable

### ✅ Late Fusion Strategy
```python
if identity_score > 0.4 and activity_status == 'AUTHORIZED':
    alert = 'GREEN'  # ✓ Known person, authorized activity
elif identity_score > 0.4 and activity_status == 'UNAUTHORIZED':
    alert = 'YELLOW'  # ⚠ Known person, suspicious activity
elif identity_score < 0.3:
    alert = 'RED'  # 🚨 Unknown person
else:
    alert = 'YELLOW'  # ⚠ Uncertain identity
```

### ✅ Comprehensive Testing
- Similarity matrix for enrollment quality
- CLIP score distributions for activity classification
- Alert distribution statistics
- End-to-end pipeline on 10+ test images

### ✅ Failure Case Analysis
- Identifies where system fails
- Explains why (technical reasons)
- Proposes concrete improvements

---

## 🔍 Understanding Model Outputs

### Face Recognition Output
```python
identity = "student_A"
confidence_score = 0.876  # Range: 0.0-1.0, higher = better match
# Interpretation: 87.6% confident this is student_A
```

### Scene Captioning Output
```python
caption = "a person working on a desktop computer in a laboratory"
# Generated by BLIP - describes what's in the image
```

### Activity Classification Output
```python
activity_status = "AUTHORIZED"  # or "UNAUTHORIZED"
activity_score = 0.85  # CLIP confidence, range: 0.0-1.0
best_label = "a person working on a computer"  # Which activity matched
```

### Final Alert Output
```python
alert_level = "GREEN"  # "GREEN", "YELLOW", or "RED"
message = "✓ student_A is in the lab. Activity: working on computer. All clear."
```

---

## 🛠️ Troubleshooting

### Issue: Model fails to load
**Solution:** Notebook includes mock implementations. System will still work in demo mode with synthetic data.

### Issue: Out of Memory (OOM)
**Solution:** 
- Use smaller batch sizes
- Process images one at a time
- Consider using GPU with sufficient VRAM (8GB+ recommended)

### Issue: Face not detected
**Reason:** Poor lighting, obscured face, or extreme angle
**Solution:** 
- Ensure good lighting conditions
- Clear face visibility (front-facing better than profile)
- Use higher resolution images

### Issue: CLIP scores seem random
**Reason:** Activity labels might not match image well
**Solution:**
- Refine activity label descriptions
- Use more specific activity descriptions
- Add more activity labels for edge cases

---

## 📚 Model Information

| Module | Model | Purpose | Paper |
|--------|-------|---------|-------|
| **1** | InsightFace (ArcFace) | Face embedding extraction | [ArcFace: Additive Angular Margin Loss](https://arxiv.org/abs/1801.07698) |
| **2** | BLIP | Image captioning | [BLIP: Bootstrapping Language-Image Pre-training](https://arxiv.org/abs/2201.12086) |
| **3** | CLIP (text-image matching) | Activity classification | [Learning Transferable Models for Vision Tasks](https://arxiv.org/abs/2103.14030) |
| **4** | Late Fusion | Decision fusion | Custom implementation |

---

## 🎓 Learning Concepts Covered

- **Unit 3:**
  - CLIP zero-shot classification
  - BLIP encoder-decoder architecture
  - Attention mechanisms in VLMs
  - Vision-language pretraining

- **Unit 4:**
  - Face recognition & biometric systems
  - Late fusion for multimodal learning
  - Similarity-based matching
  - Score normalization & thresholding

- **Integration:**
  - End-to-end multimodal pipeline
  - Decision making with multiple modalities
  - Combining visual + biometric information

---

## 📞 Support

For issues or questions:
1. Check troubleshooting section above
2. Review notebook comments and docstrings
3. Check console output for error messages
4. Verify data is in correct directories

---

## 📄 License & Citation

This is an academic project for VIT Chennai - Multimodal Machine Learning Course (21AIE541T).

---

**Happy Building! Create something impressive. 🚀**
