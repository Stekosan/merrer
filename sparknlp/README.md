# 📊 Report on Gender Bias in Pronoun Usage in classic Japanese Masterpiece Literature


## 🔍 Introduction

This report investigates potential gender bias in pronoun usage within a corpus. We aim to determine if there's a statistically significant difference between subject and object frequencies for feminine and masculine personal pronouns (e.g., "she/her" vs. "he/him"). Additionally, we'll explore whether the distribution of genders among corpus authors influences these pronoun frequencies.

I am working with three distinct text files:

- The Tale of Genji by Lady Murasaki: A classic work of Japanese literature, often considered the world's first novel. Known for its intricate portrayal of court life and relationships.
- Japanese Fairy Tales by Grace James: A collection of traditional Japanese folktales, often characterized by supernatural elements and moral lessons.
- Diaries of Court Ladies of Old Japan translated by Annie Shepley Omori and Kochi Doi: A compilation of personal writings by women from the Japanese imperial court, providing insights into their daily lives, thoughts, and feelings.

This corpus offers a rich tapestry of Japanese culture and language, spanning different genres and time periods. It's particularly interesting for your analysis as it provides a comparison between historical, fictional, and potentially more contemporary language styles.
## 🛠️ Methodology

### 📚 Datasets

- **Target Corpus**: A corpus containing text data relevant to the analysis, such as Wikipedia articles, news articles, or fiction categorized by author gender (if available).
- **Author Gender Data (Optional)**: If the corpus doesn't have author gender information, a separate dataset mapping author names to genders may be needed, either manually or using gender inference tools.

### 🖥️ Technologies

- **Apache Spark**: For large-scale data processing.
- **Spark NLP**: For natural language processing tasks (tokenization, sentence detection, named entity recognition, etc.).

### 🔄 Spark NLP Pipeline

1. **📥 Data Loading**: Load the corpus text data into a Spark DataFrame.
2. **📝 Preprocessing**:
   - Tokenize the text into individual words using a tokenizer like DocumentAssembler.
   - Optionally, perform additional preprocessing steps like sentence detection, part-of-speech tagging, or named entity recognition if needed for the analysis.
3. **🔍 Pronoun Identification**: Use a rule-based or machine learning approach to identify pronoun tokens (e.g., "she," "her," "he," "him"). Consider using Lemmatizer or a custom rule-based approach for accurate pronoun detection.
4. **🏷️ Subject/Object Distinction**: Employ dependency parsing or part-of-speech tagging to differentiate subject and object pronouns within sentences. Techniques like DependencyParser or StanfordCoreNLP (if integrated with Spark NLP) could be helpful.
5. **🧩 Gender Labeling**: Assign gender labels (masculine, feminine) to the identified pronouns based on their lemmas.
6. **📊 Frequency Counting**: Aggregate pronoun counts by gender (masculine, feminine) and subject/object category using `groupBy` and `count` operations in Spark DataFrame.

## ❓ Hypothesis

- **H1**: There is a statistically significant difference between the frequencies of subject and object pronouns for masculine and feminine personal pronouns in the corpus.
- **H2 (Bonus)**: The distribution of genders among corpus authors meaningfully impacts the observed pronoun frequencies.

## 🧪 Evaluation

- **📉 Statistical Tests**: Conduct chi-square tests or similar statistical tests to assess whether the observed pronoun frequencies deviate significantly from what would be expected if there were no gender bias. Spark's built-in statistical functions or libraries like `statsmodels` in Python can be used.
- **📈 Visualization**: Create a bar chart or other visualization to depict the distribution of pronoun frequencies across gender and subject/object categories. Libraries like `matplotlib` or `seaborn` in Python can be used for visualization within Jupyter Notebook.

