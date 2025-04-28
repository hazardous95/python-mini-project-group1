# python-mini-project-group1
1. **Onboarding Questionnaire**  
   - Gender, age, and education level  
   - Enforces age restrictions (must be ≥ 18 years old)  
   - Limits invalid attempts

2. **Trait Selection**  
   - Presents a curated list of 45+ traits  
   - Users pick **5–7** traits  
   - Page-through large lists in batches

3. **Job Matching**  
   - Pre-populated job listings by education level (`associates`, `bachelors`, `masters`)  
   - Browse in pages of 5 jobs at a time  
   - Select multiple jobs to view contact info

4. **Final Summary**  
   - Displays chosen jobs with randomly generated “contact number”

---

## Prerequisites

- Python 3.6 or higher
- Standard library only (no external dependencies)

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/yourusername/job-matchmaker.git
   cd job-matchmaker
(Optional) Create & activate a virtual environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
Usage
Run the main script:

bash
Copy code
python matchmaker.py
You will be prompted:

Looking for a job?

Enter yes/no

Menu Navigation

1. Complete Questionnaire

Gender (m/f), age (must be ≥ 18), education level

2. Select Your Traits (unlocked after questionnaire)

Pick 5–7 traits by number; can browse in pages

3. Browse Jobs (unlocked after traits)

Browse, choose jobs, and view contact listings

4. Exit




