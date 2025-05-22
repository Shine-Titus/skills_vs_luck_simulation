#  Skill vs Luck: A Statistical Simulation

> *"Skills are important. But luck can make or break your success."*  
> — This simulation explores that idea through Python and data visualization.

---

#  Overview

Why do some highly skilled people never get the success they deserve?  
Why do others, seemingly less qualified, win big?

We often chalk it up to **luck** — but can we **quantify** how much luck impacts success compared to skill?

This project is a Python-based simulation that explores the relationship between **skill, success, and luck**, and how **luck variance** can drastically affect outcomes — sometimes even overriding skill entirely.

---

#  Concept

Each individual is assigned a **skill level** (between 0 and 100).  
They undergo multiple "attempts" at success, but each attempt is influenced by a random factor — **luck noise**.

We simulate thousands of individuals and analyze how increasing the **variance of luck** affects the **correlation between true skill and actual success**.

---

# Simulation Details

- **N** = number of individuals (default: 1000)
- **M** = number of trials per person (default: 10)
- **Skill** = constant value per individual, randomly assigned
- **Luck Noise** = sampled from a normal distribution with:
  - Mean = 0
  - Standard Deviation = √(luck variance)
- **Success** = Skill + Luck Noise (clipped between 0 and 100)
- Correlation between Skill and Average Success is calculated across different levels of **luck variance**

---

# Key Insight

- When **luck variance is low**, skill is a strong predictor of success (correlation ≈ 1).
- As **luck variance increases**, the correlation drops — meaning skill no longer guarantees good outcomes.
- At high luck variance, even low-skilled individuals can outperform high-skilled ones purely by chance.

# Skill gives consistency  
# Luck introduces chaos

---
