#!/usr/bin/env python3
"""
EXECUTION GUIDE: Smart Campus Security System
Complete step-by-step instructions to run the project
"""

print("""
╔════════════════════════════════════════════════════════════════════════╗
║               SMART CAMPUS SECURITY SYSTEM                            ║
║               COMPLETE EXECUTION GUIDE                                ║
║                                                                        ║
║               Course: Multimodal Machine Learning (21AIE541T)          ║
║               Institution: VIT Chennai                                ║
╚════════════════════════════════════════════════════════════════════════╝

===============================================================================
OVERVIEW
===============================================================================

This project implements a 4-module security pipeline:
  1. Face Recognition (InsightFace) → WHO is this?
  2. Scene Captioning (BLIP) → WHAT is happening?
  3. Activity Authorization (CLIP) → Is this AUTHORIZED?
  4. Late Fusion & Alert → FINAL DECISION

Total Effort: ~90-150 minutes
Max Score: 100 marks

===============================================================================
STEP 1: ENVIRONMENT SETUP (10 minutes)
===============================================================================

1a. Verify Python Installation
    └─ Python version should be 3.8 or higher
    
    Command: python --version
    Expected: Python 3.8.x or higher

1b. Navigate to Project Directory
    
    Command: cd c:\\mycode\\mlm_project
    Expected: You should be in the mlm_project folder

1c. Install Dependencies (Method 1 - Automated)
    
    Command: python setup.py
    Expected: 
      • Project structure created
      • Dependencies installed (may take 10-20 minutes)
      • All packages verified

    Alternative (Method 2 - Manual):
    
    Command: pip install -r requirements.txt
    Expected: All packages from requirements.txt installed

1d. Verify Installation
    
    Command: python -c "import torch; print('PyTorch:', torch.__version__)"
    Expected: PyTorch: 1.9.0 or higher
    
    Also check:
    - import insightface
    - import transformers
    - import cv2
    
    If any fail, run: pip install [package_name]

===============================================================================
STEP 2: DATA COLLECTION (30-45 minutes)
===============================================================================

2a. Read Data Collection Guide
    
    File: DATA_COLLECTION_GUIDE.md
    Time: 5 minutes
    
    What: Instructions on collecting enrollment, scenario, and test images

2b. Collect Enrollment Images (5+ people)
    
    Location: enrolled_faces/
    Requirement: 5+ people × 2-3 photos each = 10-15 total images
    Quality: Clear face, well-lit, recognizable
    Format: [person_name].jpg (e.g., alice.jpg, bob.jpg, etc.)
    
    Time: 10-15 minutes
    
    Checklist:
      ☐ at least 5 different people enrolled
      ☐ 2-3 photos per person
      ☐ Good lighting (no harsh shadows)
      ☐ Front-facing angle preferred
      ☐ High resolution (400x400 minimum)

2c. Collect Campus Scenario Images (10+ scenarios)
    
    Location: scenario_images/
    Requirement: 10+ diverse scenarios
    Mix: Authorized (5-6) + Unauthorized (3-4) + Edge (2-3)
    Format: scenario_01.jpg, scenario_02.jpg, ... scenario_10.jpg
    
    Time: 15-20 minutes
    
    Authorized Scenarios:
      - Person working on computer
      - Writing on whiteboard
      - Group collaboration
      - Reading
      - Conducting experiment
    
    Unauthorized Scenarios:
      - Eating in lab
      - Sleeping at desk
      - Taking photos of equipment
      - Tampering with equipment
    
    Edge Cases:
      - Empty room
      - Multiple people
      - Partial view

2d. Collect Test Images (10+ new images)
    
    Location: test_images/
    Requirement: 10+ new images NOT in enrollment set
    Quality: Same as scenario images
    Format: test_01.jpg, test_02.jpg, ... test_10.jpg
    
    Time: 10 minutes
    
    Mix:
      ☐ Some with enrolled people (authorized activities)
      ☐ Some with enrolled people (suspicious activities)
      ☐ Some with unknown/new people
      ☐ Different lighting/angles/conditions
      ☐ Different clothing/appearance changes

2e. Verify Data Collection
    
    Check directories:
    └─ enrolled_faces/    (5+ images)
    └─ scenario_images/   (10+ images)
    └─ test_images/       (10+ images)
    
    Count images: ls [directory] | wc -l
    
    Expected:
      - enrolled_faces/ ≥ 5 images
      - scenario_images/ ≥ 10 images
      - test_images/ ≥ 10 images

===============================================================================
STEP 3: UPDATE TEAM INFORMATION (2 minutes)
===============================================================================

3a. Open the Notebook
    
    Command: jupyter notebook SCS_main.ipynb
    Expected: Notebook opens in browser

3b. Update Team Info (First Cell)
    
    Find and update:
    ```
    Team Info:
    - Team Name: [Your Team Name]
    - Members: [Name 1], [Name 2], [Name 3]
    - Roll Numbers: [Roll Numbers]
    ```
    
    Save after editing: Ctrl+S

===============================================================================
STEP 4: EXECUTE THE NOTEBOOK (10-20 minutes)
===============================================================================

4a. Run All Cells
    
    Method 1 (Best): Kernel → Restart & Run All
    Method 2 (Alternative): Run each section manually (Shift+Enter)
    
    Expected: All cells execute without errors
    Time: 10-20 minutes (depends on model sizes and GPU)

4b. Monitor Execution
    
    Watch for:
      ✓ Initialization messages (modules loading)
      ✓ Enrollment logs (faces detected)
      ✓ Scenario processing (captions generated)
      ✓ Activity classification (CLIP scores)
      ✓ Pipeline results (alerts generated)
      ✓ Visualization generation (charts created)
    
    If errors occur:
      1. Read error message carefully
      2. Check if image directory has data
      3. Verify image quality
      4. Check internet connection (for model downloads)
      5. Try restarting kernel: Kernel → Restart

4c. Expected Outputs in Console
    
    ```
    ======================================================================
    INITIALIZING SMART CAMPUS SECURITY SYSTEM
    ======================================================================
    
    [1/4] Initializing Face Recognition Module...
    [2/4] Initializing Scene Captioning Module...
    [3/4] Initializing Activity Authorization Module...
    [4/4] Initializing Fusion & Alert Module...
    
    ======================================================================
    ALL MODULES INITIALIZED SUCCESSFULLY
    ======================================================================
    
    ======================================================================
    PHASE 1: FACE ENROLLMENT
    ======================================================================
    ...
    [Processing continues...]
    ...
    ======================================================================
    RESULTS SUMMARY TABLE
    ======================================================================
    [Results displayed in table format]
    ...
    ======================================================================
    ALL PROCESSES COMPLETED SUCCESSFULLY
    ======================================================================
    ```

===============================================================================
STEP 5: REVIEW GENERATED OUTPUTS (10 minutes)
===============================================================================

5a. Check Generated Files
    
    outputs/visualizations/
      ├── similarity_matrix.png     (Face enrollment quality heatmap)
      ├── activity_scores.png       (CLIP score distributions)
      └── alert_distribution.png    (Security alert statistics)
    
    outputs/results/
      ├── security_results.csv      (Results table - exportable)
      └── system_report.txt         (System summary report)

5b. Review Results Table
    
    Open: outputs/results/security_results.csv
    
    Expected columns:
    | Image | Identity | Confidence | Scene Caption | Activity Status | Alert Level |
    
    Example:
    | test_01.jpg | student_A | 0.876 | person working on computer | AUTHORIZED | GREEN |
    | test_02.jpg | unknown | 0.189 | person eating in lab | UNAUTHORIZED | RED |
    | test_03.jpg | student_B | 0.834 | person sleeping at desk | UNAUTHORIZED | YELLOW |

5c. Review Visualizations
    
    Open each PNG file and verify:
      ✓ similarity_matrix.png - Shows face distances
      ✓ activity_scores.png - Shows CLIP scores for activities
      ✓ alert_distribution.png - Shows alert levels pie chart

===============================================================================
STEP 6: ANALYSIS & DOCUMENTATION (20-30 minutes)
===============================================================================

6a. Write Failure Case Analysis
    
    Analyze 3+ failure cases from your results:
    
    For each case, document:
      1. What was the scenario?
      2. What did the system predict?
      3. Why was it wrong? (technical reason)
      4. How could we improve it?
    
    Examples:
      • Unknown person triggering false alarm
      • Activity misclassification
      • Low-light face detection failures
      • Edge cases not covered

6b. Document Performance Metrics
    
    Calculate:
      - Correct identifications: count green alerts
      - Activity accuracy: compare predictions vs actual
      - Unknown person detection rate
      - False positive/negative rates

6c. Suggest Improvements
    
    Propose concrete improvements:
      - Better enrollment strategies
      - Refined activity labels
      - Hybrid fusion instead of late fusion
      - Additional biometrics (voice, gait)
      - Contextual rules (time of day, location)

6d. Add Comments to Code
    
    Ensure code has:
      ✓ Function/class docstrings
      ✓ Inline comments for complex logic
      ✓ Clear variable names
      ✓ Organized sections

===============================================================================
STEP 7: FINAL VERIFICATION (5 minutes)
===============================================================================

Checklist before submission:

Code & Structure:
  ☐ Notebook file: SCS_main.ipynb
  ☐ All cells executed with outputs visible
  ☐ No missing outputs or error messages
  ☐ Code is clean and well-commented

Data:
  ☐ 5+ people enrolled with face photos
  ☐ 10+ campus scenario images
  ☐ 10+ test images (not in enrollment)
  ☐ All images in correct directories

Modules:
  ☐ Module 1: Face similarity matrix displayed
  ☐ Module 2: Scene captions for all scenarios shown
  ☐ Module 3: CLIP scores and bar charts shown
  ☐ Module 4: Results table showing all test images

Results:
  ☐ Summary table with columns: Image, Identity, Confidence, 
     Scene Caption, Activity Status, Alert Level
  ☐ At least 10 test images in results table
  ☐ Results saved to CSV
  ☐ Visualizations generated and saved

Analysis:
  ☐ 3+ failure cases identified and analyzed
  ☐ Explanations provided for each failure
  ☐ Improvement suggestions documented
  ☐ Written in clear, professional language

Team Info:
  ☐ Team name at top of notebook
  ☐ Team member names listed
  ☐ Roll numbers included
  ☐ All members' roles described

Marks Breakdown:
  ☐ Module 1: Face Recognition (15 marks) - Complete
  ☐ Module 2: Scene Captioning (15 marks) - Complete
  ☐ Module 3: Activity Classification (15 marks) - Complete
  ☐ Module 4: Fusion & Alert (20 marks) - Complete
  ☐ Analysis & Discussion (15 marks) - Complete
  ☐ Code Quality (10 marks) - Complete
  ☐ Creativity/Bonus (10 marks) - Optional

===============================================================================
STEP 8: OPTIONAL BONUS EXTENSIONS (Variable time)
===============================================================================

Each worth +10 marks (if implemented well):

Extension 1: Hindi Alert Messages
  • Use MarianMT for English→Hindi translation
  • Integrate with alert system
  • Test with multiple messages

Extension 2: Attention Visualization
  • Extract BLIP cross-attention weights
  • Create attention heatmaps
  • Show which image regions model focuses on

Extension 3: Video Processing
  • Process video frame-by-frame
  • Apply full pipeline to each frame
  • Show continuous monitoring

Extension 4: Multiple Fusion Strategies
  • Implement Early Fusion
  • Implement Hybrid Fusion
  • Compare results with Late Fusion

Extension 5: VLM Fine-tuning
  • Fine-tune Qwen VL on campus data
  • Use Unsloth + QLoRA
  • Show performance improvement

===============================================================================
TROUBLESHOOTING COMMON ISSUES
===============================================================================

Issue: "Python: command not found"
Solution: Use full path: C:\\Python314\\python.exe setup.py

Issue: "pip: command not found"
Solution: Use: python -m pip install [package]

Issue: "InsightFace model download fails"
Solution: 
  - Check internet connection
  - Ensure disk space (≥ 2GB)
  - Try manual download and setup

Issue: "Out of Memory (OOM) error"
Solution:
  - Process fewer images at a time
  - Use CPU instead of GPU (slower)
  - Reduce image resolution

Issue: "Face not detected in image"
Solution:
  - Check image lighting (ensure well-lit)
  - Verify face is clearly visible
  - Try front-facing angles
  - Higher resolution images

Issue: "CLIP scores all similar"
Solution:
  - Refine activity label descriptions
  - Make them more specific
  - Separate similar activities
  - Add contextual information

Issue: "Inconsistent face identification"
Solution:
  - Re-enroll with better quality photos
  - Use different angles and lighting
  - Higher resolution images
  - Multiple enrollment samples

Issue: "Notebook won't run"
Solution:
  - Restart kernel: Kernel → Restart & Clear
  - Install missing packages: pip install -r requirements.txt
  - Check error messages carefully
  - Re-run from scratch

===============================================================================
ESTIMATED TIMELINE
===============================================================================

Task                        Time Estimate    Cumulative
─────────────────────────────────────────────────────
1. Setup & Environment        10 min            10 min
2. Read Documentation         5 min             15 min
3. Collect Images           30-45 min          45-60 min
4. Update Notebook            2 min             47-62 min
5. Run Notebook            10-20 min           57-82 min
6. Review Results             5 min             62-87 min
7. Write Analysis          20-30 min           82-117 min
8. Final Verification         5 min             87-122 min
9. Optional: Bonus Ext.   10-30 min (optional) 97-152 min
─────────────────────────────────────────────────────
TOTAL                      87-152 min        (1.5-2.5 hours)

Recommendation: Start early, don't rush image collection, 
iterate on improvements. Quality > Speed.

===============================================================================
FINAL NOTES
===============================================================================

✓ This project brings together everything from Unit 3 & 4
✓ A realistic multimodal ML pipeline
✓ Excellent portfolio piece for ML jobs
✓ Shows understanding of face recognition, vision-language models, and fusion

Good luck! 🚀

═══════════════════════════════════════════════════════════════════════════════
Project: Smart Campus Security System
Course: 21AIE541T - Multimodal Machine Learning
Institution: VIT Chennai
Last Updated: March 28, 2026
═══════════════════════════════════════════════════════════════════════════════
""")

if __name__ == "__main__":
    print("\nThis is an informational guide. For automated setup, run: python setup.py")
