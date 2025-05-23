import pandas as pd

def check_duplicate_emails(csv_file):
    """
    Checks for duplicate emails in a CSV file and returns the duplicates if found.
    
    Args:
        csv_file (str): Path to the CSV file
        
    Returns:
        dict: A dictionary with duplicate emails and their counts, or a message if no duplicates found
    """
    try:
        # Read the CSV file
        df = pd.read_csv(csv_file)
        
        # Check if 'email' column exists (case insensitive)
        email_columns = [col for col in df.columns if col.lower() == 'email']
        
        if not email_columns:
            return "No 'email' column found in the CSV file."
        
        email_column = email_columns[0]
        
        # Find duplicate emails
        duplicate_emails = df[email_column].duplicated(keep=False)
        
        if duplicate_emails.any():
            # Get duplicate emails with counts
            duplicates = df[email_column].value_counts()
            duplicates = duplicates[duplicates > 1].to_dict()
            
            # Get all rows with duplicate emails
            duplicate_rows = df[df[email_column].isin(duplicates.keys())]
            
            return {
                'message': 'Duplicate emails found',
                'duplicate_count': len(duplicates),
                'duplicate_emails': duplicates,
                'duplicate_rows': duplicate_rows.to_dict('records')
            }
        else:
            return "No duplicate emails found."
            
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    csv_file = 'utd_students_all_20250523_065622.csv'
    result = check_duplicate_emails(csv_file)
    
    if isinstance(result, dict):
        print(f"Found {result['duplicate_count']} duplicate emails:")
        for email, count in result['duplicate_emails'].items():
            print(f"- {email}: {count} occurrences")
        print("\nDuplicate entries:")
        for row in result['duplicate_rows']:
            print(row)
    else:
        print(result)