import numpy as np

class FuzzyController:
    """A robust Mamdani-style Fuzzy Logic Controller for Speed Control"""
    
    def __init__(self):
        print("⚙️ Optimized Fuzzy Logic Engine Initialized...")

    def get_membership(self, x, a, b, c):
        """Triangular Membership Function with zero-division protection"""
        # پایداری عددی برای جلوگیری از تقسیم بر صفر
        if x <= a or x >= c:
            return 0.0
        if a < x <= b:
            return (x - a) / float(b - a) if b > a else 1.0
        if b < x < c:
            return (c - x) / float(c - b) if c > b else 1.0
        return 0.0

    def process(self, distance):
        """Rule: If distance is small, speed is low. If distance is large, speed is high."""
        # Fuzzification
        # تعریف توابع عضویت برای مسافت کم و زیاد
        low_dist = self.get_membership(distance, -1, 0, 50) # شروع از کمی قبل صفر برای پایداری
        high_dist = self.get_membership(distance, 30, 100, 150)
        
        print(f"🔍 Input Distance: {distance}m")
        print(f"📊 Membership - Low: {low_dist:.2f}, High: {high_dist:.2f}")
        
        # Rule Base & Defuzzification (Simple Weighted Average)
        # Low distance -> 20 km/h | High distance -> 80 km/h
        speed = (low_dist * 20 + high_dist * 80) / (low_dist + high_dist + 1e-9)
        return speed

if __name__ == "__main__":
    controller = FuzzyController()
    # تست با مقادیر مختلف مسافت
    test_values = [0, 25, 50, 75, 100]
    
    print("--- Starting Fuzzy Inference Test ---")
    for d in test_values:
        calculated_speed = controller.process(d)
        print(f"🚀 Recommended Speed for {d}m: {calculated_speed:.2f} km/h\n")