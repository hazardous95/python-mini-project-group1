import sys #importing sys to exit the program
import random #importing random to generate random numbers for contact numbers

attempts = 0
max_attempts = 3 
def print_menu(questionnaire_done, traits_done): # Function to print the menu
    print("\n=== Job Matchmaker Menu ===")
    if not questionnaire_done: 
        print("1. Complete Questionnaire")
    else:
        print("1. Questionnaire: ✅ Completed")
    if questionnaire_done and not traits_done: 
        print("2. Select Your Traits")
    elif traits_done:
        print("2. Traits: ✅ Selected")
    else:
        print("2. Select Your Traits (locked until questionnaire is done)")
    if questionnaire_done and traits_done: 
        print("3. Browse Jobs")
    else:
        print("3. Browse Jobs (locked until questionnaire & traits are done)")
    print("4. Exit")
    print("===========================\n")

def questionnaire(user_profile): # Function to collect user profile information
    global attempts
    print("\n--- Questionnaire ---")
    while True:
        gender = input("What is your gender?: ").strip().lower()
        if gender in ["male", "female", "m", "f"]:
            break
        else:
            print("Invalid input. Please enter 'male', 'female', 'm', or 'f'.")

    while True:
        try:
            age = int(input("How old are you? ").strip())
            if age < 0:
                print("You haven't born yet!")
                attempts += 1 
            elif age < 18:
                print("Finish school first!")
                print("Come back when you're older!")
                sys.exit() # Exit the program if the user is under 18
            else:
                break 
        except ValueError:
            print("Please enter a valid non-negative integer for your age.")
            attempts += 1 
        if attempts >= max_attempts: 
            print("Too many attempts. Exiting the program.")
            sys.exit() # Exit the program

    levels = { 
        "1": "associates",
        "2": "bachelors",
        "3": "masters"
    }
    print("\nWhat is your highest level of education?") 
    for key, lvl in levels.items():
        print(f"{key}. {lvl.title()}")# # Print the education levels
    while True:# # Loop until a valid input is received
        choice = input("Enter the number of your education level: ").strip()
        if choice in levels:
            education = levels[choice]
            break
        print("Please choose a valid option (1–3).")

    user_profile.update({ # Update the user profile with the collected information
        "gender": gender,
        "age": age,
        "education": education
    })
    print("Questionnaire completed!")

    print("\nProfile Summary:") # Print the user's profile summary
    print(f"- Gender: {user_profile['gender'].capitalize()}")
    print(f"- Age: {user_profile['age']}")
    print(f"- Education Level: {user_profile['education'].capitalize()}")
    print("\nLet's continue!\n")

def select_traits(traits_list):
    print("\n--- Select Your Traits ---")
    print("Pick at least 5 and at most 7 traits that best describe you.\n")
    selected = set()
    index = 0

    while index < len(traits_list): 
        batch = traits_list[index:index+20] 
        half = len(batch) // 2
        left = batch[:half]
        right = batch[half:]

        for i in range(half): 
            left_num = index + i + 1
            right_num = index + i + half + 1
            left_text = f"{left_num}. {left[i]}" if i < len(left) else ""
            right_text = f"{right_num}. {right[i]}" if i < len(right) else ""
            print(f"{left_text:<30}{right_text}")

        choices = input("\nEnter trait numbers separated by commas (or type 'done' to finish): ").strip().lower()
        if choices == "done":
            if 5 <= len(selected) <= 7:
                break
            else:
                print("You must select between 5 and 7 traits before finishing.")
                continue

        try:
            picked = sorted(set(int(c.strip()) for c in choices.split(",")))
        except ValueError:
            print("Please enter only valid numbers separated by commas.")
            continue

        if any(c < 1 or c > len(traits_list) for c in picked):
            print("One or more numbers are out of range.")
            continue

        for p in picked:
            selected.add(traits_list[p-1])

        if len(selected) >= 7:
            print("You have selected the maximum number of traits allowed.")
            break

        more = input("\nWould you like to see more available traits? (yes/no): ").strip().lower()
        if more not in ["yes", "y"]:
            if 5 <= len(selected) <= 7:
                break
            else:
                print("You must select at least 5 traits.")
                continue

        index += 20

    print(f"\nYou selected: {', '.join(selected)}")
    return list(selected)

def choose_jobs(user_profile, jobs):
    print("\n--- Job Matches ---")
    edu = user_profile["education"]
    available = jobs.get(edu, [])

    if not available:
        print("No jobs available for your education level. Exiting.")
        sys.exit()

    shown_jobs = []
    selected_jobs = []
    index = 0

    while index < len(available):
        batch = available[index:index+5]
        for idx, job in enumerate(batch, start=len(shown_jobs)+1):
            print(f"{idx}. {job['name']}: {job['description']}")
        shown_jobs.extend(batch)

        choices = input("\nEnter the numbers of the jobs you are interested in (comma separated): ").strip()
        try:
            picked = sorted(set(int(c.strip()) for c in choices.split(",")))
            for p in picked:
                if 1 <= p <= len(shown_jobs):
                    selected_jobs.append(shown_jobs[p-1])
                else:
                    print(f"Job number {p} is out of range.")
        except ValueError:
            print("Please enter valid numbers separated by commas.")

        if index + 5 >= len(available):
            break

        more = input("\nWould you like to see more options? (yes/no): ").strip().lower()
        if more not in ["yes", "y"]:
            break
        index += 5

    return selected_jobs

def show_selected_jobs(selected_jobs):
    if not selected_jobs:
        print("\nNo jobs were selected.")
        return

    print("\nCongratulations! You now have clearer options on where to work!\n")
    for idx, job in enumerate(selected_jobs, start=1):
        contact_number = random.randint(10000, 99999)
        print(f"{idx}. {job['name']} - Contact: {contact_number}")
        print(f"   ➔ {job['description']}\n")
    print("Best of luck with your applications!\n")

def main(): 
    jobs = { 
        "associates": [
            {"name": "Dental Hygienist", "description": "Clean teeth and educate patients on oral hygiene."},
            {"name": "Paralegal", "description": "Assist lawyers with research and document preparation."},
            {"name": "Web Developer", "description": "Design and maintain websites."},
            {"name": "HVAC Technician", "description": "Install and repair heating and cooling systems."},
            {"name": "Computer Programmer", "description": "Write and test code for software."},
            {"name": "Graphic Designer", "description": "Create visual concepts to communicate ideas."},
            {"name": "Electrician", "description": "Install and maintain electrical systems."},
            {"name": "Medical Assistant", "description": "Assist doctors with patient care."},
            {"name": "Architectural Drafter", "description": "Prepare technical drawings for buildings."},
            {"name": "Respiratory Therapist", "description": "Assist patients with breathing disorders."}
        ],
        "bachelors": [
            {"name": "Software Engineer", "description": "Design and develop software applications."},
            {"name": "Financial Analyst", "description": "Analyze financial data and market trends."},
            {"name": "Mechanical Engineer", "description": "Design mechanical devices and systems."},
            {"name": "Civil Engineer", "description": "Plan and oversee construction projects."},
            {"name": "Business Analyst", "description": "Evaluate business processes and recommend improvements."},
            {"name": "Marketing Manager", "description": "Develop marketing strategies and campaigns."},
            {"name": "Accountant", "description": "Manage financial records and tax reports."},
            {"name": "Project Manager", "description": "Lead project teams and deliver projects successfully."},
            {"name": "Biologist", "description": "Study living organisms and ecosystems."},
            {"name": "Teacher", "description": "Educate students in various subjects."}
        ],
        "masters": [
            {"name": "Data Scientist", "description": "Analyze large datasets to extract insights."},
            {"name": "Nurse Practitioner", "description": "Provide advanced nursing care."},
            {"name": "Research Scientist", "description": "Conduct experiments and publish findings."},
            {"name": "Policy Analyst", "description": "Research and develop public policies."},
            {"name": "Hospital Administrator", "description": "Oversee hospital operations."},
            {"name": "Economist", "description": "Study economic data and trends."},
            {"name": "Clinical Psychologist", "description": "Diagnose and treat mental health issues."},
            {"name": "University Professor", "description": "Teach and research at the university level."},
            {"name": "Urban Planner", "description": "Develop plans for land use and infrastructure."},
            {"name": "Pharmacist", "description": "Prepare and dispense medications."}
        ]
    }

    traits_list = [
        "Adaptable", "Analytical", "Artistic", "Assertive", "Attentive", "Ambitious",
        "Cautious", "Charismatic", "Collaborative", "Compassionate", "Committed",
        "Confident", "Creative", "Curious", "Dedicated", "Detail-oriented",
        "Determined", "Disciplined", "Energetic", "Enthusiastic", "Ethical",
        "Flexible", "Hardworking", "Honest", "Innovative", "Leadership", "Logical",
        "Motivated", "Organized", "Outgoing", "Patient", "Persistent", "Problem-solver",
        "Professional", "Reliable", "Resourceful", "Responsible", "Self-disciplined",
        "Strategic", "Supportive", "Team player", "Technical", "Thorough",
        "Visionary", "Willing to learn", "Good communicator", "Time management"
    ]

    user_profile = {} 
    traits_selected = [] 
    questionnaire_done = False 
    traits_done = False 

    print("Welcome to Job Matchmaker!")
    print("Helping you find your dream career!\n")
    searching = input("Are you looking for a job? (yes/no): ").strip().lower()
    if searching not in ["yes", "y"]:
        print("Thank you for using Job Matchmaker. Goodbye!")
        sys.exit()

    while True: 
        print_menu(questionnaire_done, traits_done)
        choice = input("Enter step: ").strip() 
        if choice == "1":
            if not questionnaire_done:
                questionnaire(user_profile)
                questionnaire_done = True
            else:
                print("You've already completed the questionnaire.")
        elif choice == "2":
            if not questionnaire_done:
                print("Please complete the questionnaire first.")
            elif not traits_done:
                traits_selected = select_traits(traits_list)
                traits_done = True
            else:
                print("You've already selected your traits.")
        elif choice == "3":
            if not questionnaire_done or not traits_done:
                print("Please finish both the questionnaire and trait selection first.")
            else:
                selected_jobs = choose_jobs(user_profile, jobs)
                show_selected_jobs(selected_jobs)
                break
        elif choice == "4":
            print("Thank you for using Job Matchmaker. Goodbye!")
            break
        else:
            print("Invalid selection. Please enter a number from the menu.")

if __name__ == "__main__":
    main()