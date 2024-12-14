import os
from datetime import datetime

def create_custom_instruction_files(name, project_folder="CustomInstructions"):
    """Method: create_custom_instruction_files"""
    # Define the path for the specific name
    name_folder = os.path.join(project_folder, name)
    os.makedirs(name_folder, exist_ok=True)
    print(f"Created directory: {name_folder}")

    # Define file names
    custom_instruction_filename = f"{name}CustomInstruction.md"
    test_prompts_filename = f"{name}TestPrompts.md"

    # Define full file paths
    custom_instruction_path = os.path.join(name_folder, custom_instruction_filename)
    test_prompts_path = os.path.join(name_folder, test_prompts_filename)

    # Get current date and time
    now = datetime.now()
    date_now = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    # Define content for CustomInstruction.md
    custom_instruction_content = f"""Developer name: Franz Phillip G. Domingo
{date_now}
{time_now}
Description
"""

    # Define content for TestPrompts.md
    test_prompts_content = f"""Developer name: Franz Phillip G. Domingo
{date_now}
{time_now}
Description
"""

    # Create and write to CustomInstruction.md
    with open(custom_instruction_path, 'w') as ci_file:
        ci_file.write(custom_instruction_content)
    print(f"Created file: {custom_instruction_path}")

    # Create and write to TestPrompts.md
    with open(test_prompts_path, 'w') as tp_file:
        tp_file.write(test_prompts_content)
    print(f"Created file: {test_prompts_path}")

def main():
    """Method: main"""
    project_folder = "CustomInstructions"
    os.makedirs(project_folder, exist_ok=True)
    print(f"Project directory ensured at {project_folder}")

    names = []
    print("Enter names to generate custom instruction files. Type 'done' when finished.")

    while True:
        name = input("Enter name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break
        if name:
            names.append(name)
            print(f"Name '{name}' added.")

    if not names:
        print("No names entered. Exiting.")
        return

    for name in names:
        create_custom_instruction_files(name, project_folder)

    print("All files have been created successfully.")

if __name__ == "__main__":
    main()