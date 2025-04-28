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

Configuration
All the data lives in main() at the top of the script:

jobs:
A dict keyed by education level ("associates", "bachelors", "masters").
Each value is a list of job objects:

python
Copy code
{
  "name": "Software Engineer",
  "description": "Design and develop software applications."
}
traits_list:
A simple Python list of trait strings.

To add, remove, or edit jobs or traits, just update those lists in matchmaker.py.

Project Structure
bash
Copy code
job-matchmaker/
├── matchmaker.py     # Main script
└── README.md         # This file
Customization
Education Levels:

Extend the levels dict in questionnaire() if you need PhD or Diploma tiers.

Attempt Limits:

The global max_attempts controls how many invalid age entries a user may make.

Batch Sizes:

In select_traits(), traits are paged 20 at a time; adjust index += 20.

In choose_jobs(), jobs are paged 5 at a time; adjust index += 5.

License
This project is released under the MIT License.

pgsql
Copy code

Copy this into your project as **README.md**, and adjust any URLs or licensing details as needed.





