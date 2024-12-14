import os
from datetime import datetime

def create_custom_instruction_files(name, project_folder="CustomInstructions"):
    """Method: create_custom_instruction_files"""
    # Remove spaces from the name
    sanitized_name = name.replace(" ", "_")
    
    # Define the path for the specific name
    name_folder = os.path.join(project_folder, sanitized_name)
    os.makedirs(name_folder, exist_ok=True)
    print(f"Created directory: {name_folder}")

    # Define file names
    custom_instruction_filename = f"{sanitized_name}CustomInstruction.md"
    test_prompts_filename = f"{sanitized_name}TestPrompts.md"

    # Define full file paths
    custom_instruction_path = os.path.join(name_folder, custom_instruction_filename)
    test_prompts_path = os.path.join(name_folder, test_prompts_filename)

    # Get current date and time
    now = datetime.now()
    date_now = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    # Define content for CustomInstruction.md
    custom_instruction_content = f"""Developer name: Franz Phillip G. Domingo
Date: {date_now}
Time: {time_now}
Description:
"""

    # Define content for TestPrompts.md
    test_prompts_content = f"""Developer name: Franz Phillip G. Domingo
Date: {date_now}
Time: {time_now}
Description:
"""

    # Create and write to CustomInstruction.md
    with open(custom_instruction_path, 'w') as ci_file:
        ci_file.write(custom_instruction_content)
    print(f"Created file: {custom_instruction_path}")

    # Create and write to TestPrompts.md
    with open(test_prompts_path, 'w') as tp_file:
        tp_file.write(test_prompts_content)
    print(f"Created file: {test_prompts_path}")

    # Create Version folder inside the name folder
    version_folder = os.path.join(name_folder, "Version")
    os.makedirs(version_folder, exist_ok=True)
    print(f"Created directory: {version_folder}")

    # Determine the next version number
    existing_versions = [
        int(fname.split('-v')[-1].split('.')[0])
        for fname in os.listdir(version_folder)
        if fname.startswith(sanitized_name) and '-v' in fname
    ]
    next_version = max(existing_versions, default=0) + 1

    # Define versioned file names
    versioned_custom_instruction_filename = f"{sanitized_name}CustomInstruction-version-{next_version}.md"
    versioned_test_prompts_filename = f"{sanitized_name}TestPrompts-version-{next_version}.md"

    # Define full paths for versioned files
    versioned_custom_instruction_path = os.path.join(version_folder, versioned_custom_instruction_filename)
    versioned_test_prompts_path = os.path.join(version_folder, versioned_test_prompts_filename)

    # Define content for versioned CustomInstruction.md
    versioned_custom_instruction_content = f"""Developer name: Franz Phillip G. Domingo
Date: {date_now}
Time: {time_now}
Version: {next_version}
Description:
"""

    # Define content for versioned TestPrompts.md
    versioned_test_prompts_content = f"""Developer name: Franz Phillip G. Domingo
Date: {date_now}
Time: {time_now}
Version: {next_version}
Description:
"""

    # Create and write to versioned CustomInstruction.md
    with open(versioned_custom_instruction_path, 'w') as vci_file:
        vci_file.write(versioned_custom_instruction_content)
    print(f"Created versioned file: {versioned_custom_instruction_path}")

    # Create and write to versioned TestPrompts.md
    with open(versioned_test_prompts_path, 'w') as vtp_file:
        vtp_file.write(versioned_test_prompts_content)
    print(f"Created versioned file: {versioned_test_prompts_path}")

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