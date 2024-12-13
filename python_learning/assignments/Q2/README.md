## OPEN AI API Parameters

### 1. **Messages**

- A list of all messages in the conversation.
- Each message has two parts:
  - `role`: Who is talking (e.g., user, assistant, or system).
  - `content`: What they said.

### 2. **Model**

- The version of AI we want to use (e.g., `gpt-4`, `gpt-3.5-turbo`...).
- Some models are faster or more advanced than others.

### 3. **Max Completion Tokens**

- Sets the limit on how much text the AI can generate.
- Helps keep responses short and control costs.

### 4. **n**

- Decides how many responses the AI should give for the same question.
- For example, if `n=2`, we’ll get two different answers.

### 5. **Stream**

- If `true`, the AI sends its response piece by piece as it writes.
- Useful for long answers because we don’t have to wait for the whole thing.

### 6. **Temperature**

- Controls how creative or random the AI’s answers are:
  - Low numbers (like 0.2) make answers more focused and predictable.
  - High numbers (like 0.8) make answers more creative and varied.

### 7. **Top_p**

- Another way to control randomness.
- It only picks from the most likely words that add up to a certain probability.
- Example: `top_p=0.9` means the AI considers only the top 90% most likely words.

### 8. **Tools**

- Allows the AI to use extra apps or plugins to do specific tasks.
- Example: A calculator or a search engine.
