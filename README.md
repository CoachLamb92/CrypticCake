# CrypticCake
A self-learning collaborative piece based around NLP and linguistic modelling

## To create the database locally
psql -f clues_db.sql

Training an AI to better solve cryptic crosswords is a fascinating challenge that sits at the intersection of natural language understanding, linguistic pattern recognition, and logic/puzzle solving. Here’s a breakdown of how you could approach this:

### 1. Understand the Structure of Cryptic Clues
Cryptic clues typically consist of:

A definition (usually at the beginning or end)
A wordplay component (anagram, hidden word, homophone, container, charade, etc.)

The AI must:

Recognize clue structure
Identify clue types
Map clue components to word construction techniques

### 2. Dataset Collection
You’ll need a training corpus of cryptic clues with annotated solutions and explanations. Some options:

Openly available crosswords (Guardian, Independent, Times — some are accessible via archives or web scraping)

Use forums like 15² for annotated solutions

Create a dataset in the format:

{
  "clue": "Lift former partner, endlessly, for praise (6)",
  "answer": "extol",
  "definition": "praise",
  "wordplay": {
    "explanation": "EX (former partner) + TOL (TOL(D), endlessly)",
    "type": ["charade", "deletion"]
  }
^ This example is incorrect, but for now, the template is sound.

### 3. Model Approaches
There are a few promising routes here:

a. Fine-tune an LLM (like GPT) on cryptic data

Use a GPT-style model trained on general language tasks

Fine-tune with cryptic clue-answer-explanation triplets

Encourage reasoning with chain-of-thought supervision

b. Train a dual-system model

One sub-model identifies clue structure (e.g., classify wordplay type)

Another constructs or verifies potential answers using rules

c. Use retrieval + reasoning

Use a retrieval system to fetch similar solved clues

Use a transformer to map the current clue to those patterns

Apply a rule-based generator to propose candidate answers

### 4. Training Tasks
Train your model to do the following:

Clue segmentation: Break a clue into [definition] + [wordplay]

Clue type classification: Is it anagram, hidden word, homophone, container, etc.?

Wordplay resolution: Convert clue elements into construction steps

Candidate ranking: Given a clue and a list of answer candidates, rank the best match

### 5. Evaluation
Evaluate performance by:

Accuracy of final answer

Precision of parsing (definition vs. wordplay)

Correct identification of clue mechanism

Use datasets like:

Guardian/Times cryptics with solutions

Custom benchmarks with known clue types

### 6. Tools & Libraries
NLP: Hugging Face Transformers, spaCy, NLTK

Fine-tuning: PyTorch/Transformers or OpenAI's fine-tuning endpoints

Wordplay tools: Use libraries like XWordInfo (for American-style), or write custom regex/anagram solvers

### Bonus: Train with Explanations
One novel approach is to supervise with explanations, not just answers — training the model to generate a breakdown of clue mechanics. This aligns with how humans actually learn to solve cryptics.
