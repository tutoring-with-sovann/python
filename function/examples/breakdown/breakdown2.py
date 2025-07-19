def find_anagrams(word_list, target):
    """
    Returns a list of strings from word_list that are anagrams of the target word.
    
    Args(Arguments):
        word_list (list): List of strings to check
        target (str): Target word to find anagrams for
        
    Returns:
        list: List of strings that are anagrams of the target word
    """
    # Convert target word to sorted lowercase characters for comparison
    target_sorted = sorted(target.lower())
    
    # Filter words that have same sorted characters as target
    result = []
    # Iterate through the list of word using 'word' as variable
    for word in word_list:
      # Condition check if all lowercase of 'word' is sorted equal to the target sorted word
      # And the lowercase of 'word' is not equal to taget lower case(avoid to count the target word)
      if(sorted(word.lower()) == target_sorted and word.lower() != target.lower()):
        # If condition is match, add this 'word' to the 'result' list.
        result.append(word);

    return result

# Example usage
word_list = ["listen", "silent", "hello", "enlist", "world", "inlets"]
target = "listen"
print(find_anagrams(word_list, target))
# Output
# ✅ ['silent', 'enlist', 'inlets']
# ❌ ['listen', 'silent', 'enlist', 'inlets'] - 'listen' doesn't count because we don't want the actual match


