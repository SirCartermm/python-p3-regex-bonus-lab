import re

def find_pattern(pattern, text):
  """Finds all occurrences of a pattern in a text."""
  return re.findall(pattern, text)

def main():
  """Runs the main program."""

  # Define the regular expression pattern.
  pattern = r"\w+ \w+"

  # Define the text to search.
  text = "It's such a lovely day today."

  # Find all occurrences of the pattern in the text.
  matches = find_pattern(pattern, text)

  # Print the matches.
  print(matches)

if __name__ == "__main__":
  main()
