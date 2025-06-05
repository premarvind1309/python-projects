def build_resume():
    print("Enter your details to build your resume\n")

    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    address = input("Address: ")

    print("\n--- Education ---")
    education = input("Enter your highest qualification (e.g. B.Sc in Computer Science): ")

    print("\n--- Skills ---")
    skills = input("List your skills separated by commas: ")

    print("\n--- Experience ---")
    experience = input("Briefly describe your work experience: ")

    resume_text = f"""
    ===============================
                RESUME
    ===============================

    Name: {name}
    Email: {email}
    Phone: {phone}
    Address: {address}

    Education:
    {education}

    Skills:
    {skills}

    Experience:
    {experience}

    ===============================
    """

    with open("resume.txt", "w") as file:
        file.write(resume_text.strip())

    print("\nYour resume has been generated and saved as 'resume.txt'.")

if __name__ == "__main__":
    build_resume()
