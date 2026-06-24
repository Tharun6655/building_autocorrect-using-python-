# NLP Autocorrect System

A simple Python-based Autocorrect system built using Natural Language Processing (NLP) techniques. This project uses word probability distributions and edit distance algorithms to identify misspelled words and suggest the most likely corrections based on a text dataset.

## 🚀 Features
* **Text Preprocessing:** Reads and cleans raw text from `final.txt` to build a vocabulary dictionary.
* **Word Probability Calculation:** Computes the likelihood of words based on their frequency in the data.
* **Edit Distance Operations:** Generates candidate corrections using standard string manipulations:
  * **Inserts:** Adding a letter (e.g., `at` -> `cat`)
  * **Deletes:** Removing a letter (e.g., `carte` -> `cart`)
  * **Replaces:** Swapping a letter (e.g., `loke` -> `like`)
  * **Swaps:** Switching adjacent letters (e.g., `baet` -> `beat`)
* **Ranking:** Selects the most probable correct word from the generated candidates.

---

## 🛠️ Project Structure

Since this is a lightweight implementation, the project consists of just two main files:
```text
├── final.txt          # The text corpus used to train word frequencies
├── model.py           # The Python script containing the NLP logic and execution
├── .gitignore         # Ignores venv/ and temporary files
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies
