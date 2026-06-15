# Spam Email Detection Using Machine Learning

## Overview

This project classifies email messages as **Spam** or **Ham (Not Spam)** using Machine Learning and Natural Language Processing (NLP).

The model analyzes the content of an email and predicts whether it is spam or legitimate.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes

---

## Machine Learning Algorithm

### Multinomial Naive Bayes

Multinomial Naive Bayes is a popular classification algorithm used for text classification problems such as:

- Spam Detection
- Sentiment Analysis
- News Classification
- Document Categorization

---

## Features

- Spam Email Detection
- Text Preprocessing
- TF-IDF Vectorization
- Email Classification
- Accuracy Evaluation
- Real-Time User Prediction

---

## Dataset Features

| Column | Description |
|----------|------------|
| label | Spam or Ham |
| message | Email Message Content |

---

## Project Structure

```text
spam-email-detection/
│
├── spam_email_detection.py
├── spam.csv
├── requirements.txt
├── README.md
└── Output.png
```

---

## How to Run

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python spam_email_detection.py
```

---

## Sample Input

```text
Congratulations! You won a free iPhone
```

---

## Sample Output

```text
Accuracy: 100.0 %

===== SPAM EMAIL DETECTOR =====

Result: SPAM EMAIL
```

---

## Output Screenshot

![Output](Output.png)

---

## Applications

- Email Filtering Systems
- Cybersecurity Solutions
- Fraud Detection
- Messaging Platforms
- Enterprise Communication Systems

---

## Future Enhancements

- GUI using Tkinter
- Flask Web Application
- Larger Dataset Integration
- Deep Learning Models
- Real Email Dataset Support

---

## Author

**SUBASH P**  
B.E Computer Science and Engineering (AI & ML)

---

## GitHub Topics

```text
python
machine-learning
spam-detection
email-classification
nlp
naive-bayes
scikit-learn
artificial-intelligence
```