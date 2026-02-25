# 🧠 Fuzzy Control Library
**Autonomous Decision-Making Engine built from Scratch**

This library provides a robust Python implementation of a **Mamdani-style Fuzzy Logic Controller**. It is specifically designed to handle non-linear decision-making in **Intelligent Transportation Systems (ITS)**, such as autonomous speed regulation and adaptive traffic signaling.

## 🚀 Key Features
- **Zero-Dependency Core:** Implemented using base Python logic (NumPy for math).
- **Custom Membership Functions:** Includes triangular membership functions with zero-division protection.
- **Fuzzy Inference System:** Handles Fuzzification, Rule Evaluation, and Defuzzification (Weighted Average).

## 🛠️ Tech Stack
- **Language:** Python 3.13+
- **Mathematics:** NumPy

## 📊 Sample Execution Output
Below is the real-time output of the fuzzy engine calculating recommended speeds based on obstacle distance:

```text
⚙️ Optimized Fuzzy Logic Engine Initialized...
--- Starting Fuzzy Inference Test ---

🔍 Input Distance: 0m
📊 Membership - Low: 1.00, High: 0.00
🚀 Recommended Speed: 20.00 km/h

🔍 Input Distance: 25m
📊 Membership - Low: 0.50, High: 0.00
🚀 Recommended Speed: 20.00 km/h

🔍 Input Distance: 50m
📊 Membership - Low: 0.00, High: 0.29
🚀 Recommended Speed: 80.00 km/h

🔍 Input Distance: 100m
📊 Membership - Low: 0.00, High: 1.00
🚀 Recommended Speed: 80.00 km/h
