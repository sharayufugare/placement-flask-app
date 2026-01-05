# College-Placement-Prediction
```
📌 Key Features

Predicts Placed / Not Placed using Machine Learning
Uses real student attributes like:
  CGPA
  Internships
  Coding practice (LeetCode, HackerRank)
  Certifications
  Soft Skill score
  Aptitude score
Separate Soft Skill Test and Aptitude Test
Randomized questions on every test attempt
ML model trained using historical placement data
User-friendly web interface built with Flask & HTML

🧠 Machine Learning Approach

Problem Type: Classification
Algorithm Used: Decision Tree Classifier
Dataset: Student academic & skill-based data
Target Variable: PlacementStatus
1 → Placed
0 → Not Placed
The trained model is saved as model.pkl and used in real-time predictions through the Flask backend.

🛠 Technologies Used

Python
Flask (Web Framework)
Scikit-learn (Machine Learning)
Pandas & NumPy
HTML / CSS (Frontend)

📂 Project Structure

placement_prediction_project/
│
├── data/
│   └── student_placement_data.csv
│
├── model/
│   └── model.pkl
│
├── templates/
│   ├── index.html
│   ├── softskill_test.html
│   ├── aptitude_test.html
│   └── result.html
│
├── train_model.py
├── app.py
└── requirements.txt

🚀 How It Works

Student enters academic and skill details.
Student completes Soft Skill & Aptitude tests.
Test scores are combined with profile data.
ML model predicts placement result.
Final result is displayed on the screen.
```
