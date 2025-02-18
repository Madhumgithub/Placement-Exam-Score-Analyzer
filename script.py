
### **🐍 script.py**
```python
import statistics

scores = list(map(int, input("Enter your last 5 test scores (comma-separated): ").split(",")))

avg_score = statistics.mean(scores)
improvement = "📈 Improving" if scores[-1] > scores[-2] else "📉 Declining"

print(f"\n📊 Average Score: {avg_score}")
print(f"📌 Performance Trend: {improvement}")
