import json

# Read the contents of qa.txt
with open('qa.txt', 'r', encoding='utf-8') as file:
    data = file.read()

# Split the data by "ĐÁP ÁN:"
blocks = data.split('ĐÁP ÁN:')

# Initialize arrays for questions
questions = []
unsuccessful_blocks = []

# Function to parse a question block
def parse_question_block(block, answer_key):
    lines = block.strip().split('\n')
    if len(lines) < 5:
        return None
    
    try:
        # Extract the question and choices
        question = lines[-5].strip()
        choices = [
            lines[-4].strip(),
            lines[-3].strip(),
            lines[-2].strip(),
            lines[-1].strip()
        ]

        # Ensure answer_key contains only one character
        if len(answer_key) == 1 and answer_key in 'ABCD':
            answer_index = ord(answer_key) - ord('A')  # Tính chỉ số dựa trên đáp án
            answer = choices[answer_index] if 0 <= answer_index < len(choices) else None
        else:
            # If answer_key is not valid, skip this block
            print(f"Invalid answer key at block: {block}")
            return None

        return {
            'question': question,
            'choices': choices,
            'answer': answer
        }
    except IndexError:
        return None

# Parse the blocks into question objects
for i in range(len(blocks) - 1):
    block = blocks[i].strip()
    answer_key = blocks[i + 1].strip()[0]  # Get the answer key from the next block
    question_block = parse_question_block(block, answer_key)
    if question_block:
        questions.append(question_block)
    else:
        print(f"Unsuccessful block at index {i}")
        unsuccessful_blocks.append(i)

# Output the JavaScript code
with open('QnA.txt', 'w', encoding='utf-8') as file:
    file.write('const questions = ' + json.dumps(questions, indent=4, ensure_ascii=False) + ';\n')

# Print unsuccessful blocks
if unsuccessful_blocks:
    print("Unsuccessful question blocks at indices:", unsuccessful_blocks)
else:
    print("All question blocks processed successfully.")