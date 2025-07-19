def send_notification(message, recipient="team_lead@company.com"):
    """
    Simulates sending an email notification with a default recipient.
    
    Args:
        message (str): The notification message to send
        recipient (str, optional): Email address of the recipient. Defaults to "team_lead@company.com"
    
    Returns:
        str: Confirmation of the notification sent
    """
    return f"Notification sent to {recipient}: {message}"

# Example usage
task_update = "Task #123 has been completed."

# Using default recipient
print(send_notification(task_update))  
# Output: Notification sent to team_lead@company.com: Task #123 has been completed.

# Using custom recipient
print(send_notification(task_update, recipient="manager@company.com"))  
# Output: Notification sent to manager@company.com: Task #123 has been completed.