# Baguio City Public Transportation

**CS 415 Intelligent Systems — Laboratory Session 1**

A jeepney route finder and passenger demand prediction system for tourists
and local residents of Baguio City.

---

## 👥 Team and Roles

| Name | Role | Owns |
|---|---|---|
| Sophia Sumahit | Project Manager | Planning, task board |
| Chris Dayrit | Data Lead | Data sources, data quality |
| Lairee Cachero | Model Lead | Models, results |
| Lyn Leishly Gamay | Documentation & Testing Lead | Documents, tests |

---

## 📋 Problem Statement

Our project aims to help tourists and local residents who have difficulty
commuting via jeepney because they are unfamiliar with jeepney routes and
staging areas leading to their desired destinations. As a result, many choose
more expensive transportation options, such as taxis. The system will use
jeepney routes, staging areas, passenger demand, and destination information
to recommend the correct jeepney routes and predict passenger demand. Its
success will be measured by the accuracy of route recommendations and
passenger demand predictions, as well as its ability to help commuters save
time and transportation costs.

**Data needed:** jeepney routes and destinations, staging areas and terminals,
passenger counts, popular tourist destinations, schedules and waiting times,
commuter travel preferences, common pickup/drop-off locations.

**What it predicts/decides:**
- Predicts passenger demand on jeepney routes during specific times of day.
- Recommends the correct jeepney route and staging area for a destination.

**How success is measured:**
- Accuracy of route and staging-area recommendations.
- Accuracy of passenger demand predictions.
- Reduction in commuters' travel time and unnecessary costs.
- Number of users successfully reaching their destinations by jeepney.

---

## 🧪 Environment Verification (Hello-Data Test)

Verified in Google Colab:

- Python 3.13.18
- pandas 2.2.3
- scikit-learn 1.6.1
- Iris dataset loaded successfully: **(150, 5)** ✅

**Screenshot:** [`data/hello_data.png`](data/hello_data.png)

**Notebook:** [`notebooks/CS415_Hello_Data.ipynb`](notebooks/CS415_Hello_Data.ipynb)

---
