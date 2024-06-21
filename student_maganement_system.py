import re

# Dictionary to store student records
students = {}

def get_valid_name(prompt, allow_empty=True):
    """
    Check whether a name is valid.
    :param prompt:
    :param allow_empty (default = True):
    :return name:
    """
    while True:
        is_valid = True
        user_input = input(prompt)
        if allow_empty and user_input == "":
            return None


        for char in user_input:
            if (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z')):
                continue
            else:
                is_valid = False

        if is_valid:
            return user_input

        else:
            print("Incorrect input. Please, enter a valid name.")

def get_valid_input(prompt, valid_type=str, allow_empty=True):
    """
    Check the validity of a prompt.
    :param prompt: Message for the user
    :param valid_type: expected data type (str by default)
    :param allow_empty: True by default
    :return: True or False
    """
    while True:
        user_input = input(prompt)
        if allow_empty and user_input == "":
            return None
        try:
            return valid_type(user_input)
        except ValueError:
            print(f"Value Error. Please enter value of type: {valid_type.__name__}.")


def get_valid_subjects(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "":
            return []
        if re.match(r'^(\w+)(, \w+)*$', user_input):
            return user_input.split(', ')
        else:
            print("Invalid input. Please, enter the subjects separated by comma and space (eg: 'Math, Science, History').")


def add_student(name, age, grade, subjects):
    """
    Add a new student record.
    Args:
    - name (str): The name of the student.
    - age (int): The age of the student.
    - grade (float): The grade of the student.
    - subjects (list of str): The subjects the student is enrolled in.
    """
    # Code to add a new student record
    students[name] = {'age': age, 'grade': grade, 'subjects': subjects}
    print(f'\n{name} added.')
    return students



def update_student(name):
    """
    Update an existing student record.
    Args:
    - name (str): The name of the student whose record is to be updated.
    """
    # Check if the student exists
    # Prompt the user to update fields and keep current values if fields are empty
    # Code to update the student's record
    new_subjects = []

    if name in students.keys():
        print('\nEnter the values that you want to update (press enter, if you don\'t want to update the current value):')

        new_name = get_valid_name('Enter the name of the student whose record is to be updated: ')
        if new_name is None:
            new_name = name

        new_age = get_valid_input('Enter the age of the student whose record is to be updated: ', int)
        if new_age is None:
            new_age = students[name]['age']

        new_grade = get_valid_input('Enter the grade of the student whose record is to be updated: ', float)
        if new_grade is None:
            new_grade = students[name]['grade']

        new_subjects = get_valid_subjects('Enter the subjects of the student whose record is to be updated (comma separated): ')
        if not new_subjects:
            new_subjects = students[name]['subjects']

        del students[name]
        students[new_name] = {'age': new_age, 'grade': new_grade, 'subjects': new_subjects}

        print('\nSuccessfully updated student record.')

    else:
        print('\nThe student with that name does not exist.')

    return students


def delete_student(name):
    """
    Delete a student record based on the student's name.
    Args:
    - name (str): The name of the student to delete.
    """
    # Check if the student exists
    # Code to delete the student's record

    if name in students.keys():
        del students[name]
        print('\nSuccessfully deleted student record.')

    else:
        print('\nThe student with that name does not exist.')

    return students


def search_student(name):
    """
    Search for a student by name and return their record.
    Args:
    - name (str): The name of the student to search for.
    """
    # Check if the student exists
    # Code to return the student's record

    if name in students.keys():
        result = (f'\n----------Student----------\n'
                  f'Name: {name}\n'
                  f'Age: {students[name]["age"]}\n'
                  f'Grade: {students[name]["grade"]}\n'
                  f'Subjects: {", ".join(students[name]["subjects"])}')

    else:
        result = '\nThe student with that name does not exist.'

    print(result)
    return result


def list_all_students():
    """
    List all student records.
    """
    # Check if there are any student records
    # Code to list all students

    result_list_of_students = ('\n---------- List of Student Records ----------\n')
    empty_list = result_list_of_students
    counter = 0

    for student in students:
        counter += 1
        result_list_of_students += (f'\nStudent #{counter}\n'
                                    f'Name: {student}\n'
                                    f'Age: {students[student]["age"]}\n'
                                    f'Grade: {students[student]["grade"]}\n'
                                    f'Subjects: {", ".join(students[student]["subjects"])}\n')

    if result_list_of_students != empty_list:
        print(result_list_of_students)

    else:
        print('\nThere are no student records.')

    return result_list_of_students

def main():
    """
    Main function to provide user interaction.
    """
    while True:
        # Display menu options
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. List All Students")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for student details
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            grade = float(input("Enter student's grade: "))
            subjects = input("Enter student's subjects (comma-separated): ").split(',')
            # Call the add_student function
            add_student(name, age, grade, subjects)
        elif choice == '2':
            # Prompt for student name to update
            name = input("Enter student's name to update: ")
            # Call the update_student function
            update_student(name)
        elif choice == '3':
            # Prompt for student name to delete
            name = input("Enter student's name to delete: ")
            # Call the delete_student function
            delete_student(name)
        elif choice == '4':
            # Prompt for student name to search
            name = input("Enter student's name to search: ")
            # Call the search_student function
            search_student(name)
        elif choice == '5':
            # Call the list_all_students function
            list_all_students()
        elif choice == '6':
            # Exit the program
            break
        else:
            print("\nInvalid choice, please try again.")


if __name__ == "__main__":
    main()