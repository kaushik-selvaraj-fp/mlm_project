# Data Collection Guide
## Smart Campus Security System

This guide helps you collect suitable images for the project.

---

## 📸 Enrollment Images (5+ people)

### Requirements:
- **Count:** At least 5 different people
- **Photos per person:** 2-3 photos minimum
- **Total:** Minimum 10-15 enrollment photos
- **Quality:** Clear face, well-lit, recognizable

### How to Collect:

**Step 1: Prepare**
- Use a smartphone or webcam
- Find a well-lit area (natural light is best)
- Have dark or neutral background

**Step 2: For Each Person**
1. Face front-facing camera
2. Take 2-3 photos from slightly different angles:
   - Straight on (90° face to camera)
   - Slight left angle (~45°)
   - Slight right angle (~45°)
3. Ensure face is clearly visible (no heavy occlusion)

**Step 3: Save**
- Save with clear naming: `enrolled_faces/[person_name].jpg`
- Examples: `enrolled_faces/alice.jpg`, `enrolled_faces/bob.jpg`
- Format: JPG or PNG, minimum 400x400 pixels

### Example People to Enroll:
- Student A (yourself or team member)
- Student B (team member)
- Student C (team member)
- Professor / TA
- Staff member or visitor

### ✅ Good Practices:
- ✅ Clear face visibility
- ✅ Good lighting (no harsh shadows)
- ✅ Front-facing angle preferred
- ✅ Multiple angles for robustness
- ✅ High resolution pictures

### ❌ Avoid:
- ❌ Blurry images
- ❌ Extreme angles (profile only)
- ❌ Face partially occluded
- ❌ Very dark or backlighting
- ❌ Sunglasses or hats covering face

---

## 🎬 Scenario Images (10+ diverse scenarios)

### Requirements:
- **Count:** At least 10 different scenarios
- **Diversity:** Mix of authorized & unauthorized activities
- **Realism:** Actual lab/classroom environments
- **Resolution:** Minimum 640x480 pixels

### Scenario Checklist:

#### Authorized Activities (5-6 images):
- [ ] **Lab Work:** Person at computer, typing, working on project
- [ ] **Whiteboard Discussion:** Person writing on whiteboard / pointing
- [ ] **Group Collaboration:** Multiple people discussing project together
- [ ] **Reading:** Person reading technical book or document
- [ ] **Experiment:** Person conducting lab experiment / handling equipment
- [ ] **Equipment Setup:** Person arranging lab equipment

<img src="placeholder" alt="Authorized activity: Lab work">

#### Unauthorized Activities (3-4 images):
- [ ] **Eating in Lab:** Person eating food at desk or in lab
- [ ] **Sleeping:** Person sleeping or head down at desk
- [ ] **Photography:** Person taking photos of equipment with camera/phone
- [ ] **Tampering:** Person touching restricted equipment without authorization

<img src="placeholder" alt="Unauthorized activity: Photography">

#### Edge Cases (2-3 images):
- [ ] **Empty Room:** No people, just lab/classroom setup
- [ ] **Multiple People:** 2+ people in different activities
- [ ] **Partial View:** Person partially visible/entering

### How to Collect:

**Step 1: Plan**
- List all 10+ scenarios
- Decide location (lab, classroom, etc.)
- Get permission if needed

**Step 2: Capture Each Scenario**
- Use smartphone or camera
- Frame to show the activity clearly
- Capture from different angles if possible
- Get good lighting

**Step 3: Save and Label**
```
scenario_images/
├── scenario_01_lab_work.jpg
├── scenario_02_whiteboard.jpg
├── scenario_03_collaboration.jpg
├── scenario_04_reading.jpg
├── scenario_05_experiment.jpg
├── scenario_06_eating.jpg
├── scenario_07_sleeping.jpg
├── scenario_08_photography.jpg
├── scenario_09_empty_lab.jpg
└── scenario_10_multiple_people.jpg
```

### ✅ Quality Tips:
- ✅ Good lighting (avoid shadows on face)
- ✅ Clear activity visibility
- ✅ Include context (lab equipment, desk, etc.)
- ✅ Different camera angles (wide, medium, close)
- ✅ Natural postures (not staged unnaturally)

---

## 🧪 Test Images (10+ new images)

### Requirements:
- **Count:** At least 10 new photos
- **Distinctness:** Different from both enrollment and scenarios
- **Mix:** Authorized + unauthorized + edge cases
- **Quality:** Same as scenario images

### How to Collect:

**Step 1: Use Different Conditions**
- Different time of day
- Different lighting
- Different angles
- Different clothing/appearance (for enrolled people)

**Step 2: Mix Activities**
- Some with enrolled people doing authorized activities
- Some with enrolled people doing suspicious activities
- Some with unknown people
- Some edge cases

**Step 3: Save**
```
test_images/
├── test_01.jpg
├── test_02.jpg
├── test_03.jpg
├── ...
└── test_10_plus.jpg
```

### Expected Results:

Your system should output:
- **Green alerts:** Enrolled person doing authorized activity
- **Yellow alerts:** Enrolled person doing suspicious activity / Unknown person
- **Red alerts:** Unknown person in lab

---

## 📋 Data Checklist Before Running

Before executing the notebook, verify:

```
□ Directory structure created:
   □ enrolled_faces/
   □ scenario_images/
   □ test_images/
   □ outputs/
   □ outputs/visualizations/
   □ outputs/results/

□ Enrollment images (5+ people):
   □ At least 5 people with photos
   □ 2-3 photos per person minimum
   □ Total 10-15+ enrollment images
   □ Clear face visibility
   □ Good lighting

□ Scenario images (10+ scenarios):
   □ 10+ diverse campus scenarios
   □ Mix of authorized & unauthorized
   □ High quality, well-lit
   □ Different angles/contexts
   □ Named consistently (scenario_01, scenario_02, etc.)

□ Test images (10+ new images):
   □ 10+ new images NOT in enrollment
   □ Different conditions/lighting/angles
   □ Mix of enrolled + unknown people
   □ Mix of authorized + unauthorized activities

□ File naming conventions followed:
   □ enrolled_faces/[person_name].jpg
   □ scenario_images/scenario_[number].jpg  
   □ test_images/test_[number].jpg
```

---

## 🚨 Common Issues & Solutions

### Issue: "No face detected by InsightFace"
**Cause:** Poor lighting, extreme angle, or face too small
**Solution:**
- Increase lighting (move closer to light source)
- Use front-facing angle (90° to camera)
- Ensure face takes up at least 20% of image
- High resolution image

### Issue: "All enrollments look too similar"
**Cause:** All photos are too similar (same lighting, angle, etc.)
**Solution:**
- Take photos at different times/lighting
- Vary angles (straight, left, right)
- Different facial expressions
- Different clothing

### Issue: "CLIP scores are similar for allowed & disallowed"
**Cause:** Activity labels are too vague or similar
**Solution:**
- Make activity labels more specific
- Use different activities for different roles
- Give more context in labels
- Example: Instead of "working", use "working on computer in lab"

### Issue: "Wrong face identification"
**Cause:** Enrollment photos too similar or of poor quality
**Solution:**
- Re-enroll with better quality photos
- Use different angles and lighting
- Ensure person is clearly recognizable
- Remove glasses/hats during enrollment if possible

---

## 📸 Sample Activity Descriptions

Use these as inspiration for your activity labels:

### ALLOWED Activities:
1. "a student working on a desktop computer"
2. "a person writing mathematics on a whiteboard"
3. "a group of students collaborating on a project"
4. "a person reading a technical textbook"
5. "a person conducting a chemistry experiment in the lab"
6. "students discussing in the laboratory"
7. "a person taking notes at the desk"
8. "a person using lab equipment appropriately"

### DISALLOWED Activities:
1. "a person eating or drinking in the restricted lab area"
2. "a person sleeping or napping at the desk"
3. "a person taking photographs of restricted equipment"
4. "someone recording video without authorization"
5. "a person tampering with expensive lab instruments"
6. "an unidentified person in the secure lab"
7. "a person using a mobile phone in restricted areas"
8. "someone stealing or removing lab equipment"

---

## 📊 Data Statistics Template

After collecting, fill this out:

```
ENROLLMENT DATA:
- Number of people enrolled: ___
- Total enrollment images: ___
- Average images per person: ___
- Image resolution range: ___ to ___
- Storage size: ___

SCENARIO DATA:
- Total scenario images: ___
- Authorized scenarios: ___
- Unauthorized scenarios: ___
- Edge case scenarios: ___
- Average image size: ___
- Total storage: ___

TEST DATA:
- Total test images: ___
- New people (not enrolled): ___
- Images with enrolled people: ___
- Average resolution: ___
- Storage size: ___

TOTAL PROJECT DATA:
- Total images: ___
- Total storage used: ___
- Ready for processing: YES / NO
```

---

## ✅ Final Verification

Before running the notebook:

1. **Count images:**
   ```bash
   ls enrolled_faces/ | wc -l    # Should be ≥ 5
   ls scenario_images/ | wc -l   # Should be ≥ 10
   ls test_images/ | wc -l       # Should be ≥ 10
   ```

2. **Check image quality:**
   - Open each image in viewer
   - Verify face clarity, lighting, resolution
   - Ensure diverse angles and conditions

3. **Verify directory structure:**
   ```
   mlm_project/
   ├── SCS_main.ipynb
   ├── enrolled_faces/          (5+ images)
   ├── scenario_images/         (10+ images)
   ├── test_images/             (10+ images)
   └── outputs/                 (will be created by notebook)
   ```

4. **Run the notebook:**
   - Open Jupyter: `jupyter notebook`
   - Open `SCS_main.ipynb`
   - Execute all cells: Kernel → Restart & Run All
   - Wait for outputs (~5-10 minutes)
   - Verify results in `outputs/` directory

---

## 🎬 Privacy & Consent

- Ensure you have permission to collect photos of people
- Use team members for enrollment (easier consent)
- Don't use others' photos without permission
- This is for educational purposes only
- Data should be deleted after project submission

---

**Ready to collect images? Follow this guide and you'll have great data! 📸**
