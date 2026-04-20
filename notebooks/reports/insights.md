## Customer Churn Analysis — Key Findings & Recommendations
**Date:** [Your date] | **Analyst:** [Your name] | **Dataset:** IBM Telco (7,043 customers)

---

### Executive Summary
26.5% of customers churned in the observed period. At an average monthly
charge of $64.76, this represents approximately $1.88M in annualised
revenue risk across the customer base.

### Finding 1: Contract type is the strongest churn driver
- Month-to-month customers churn at 42.7% vs 2.8% for 2-year contracts
- 55% of the base (3,875 customers) are on monthly contracts
- Action: Introduce a 3-month free discount to convert monthly → annual

### Finding 2: The first 6 months are the critical retention window
- 47.4% of customers with tenure < 6 months churned
- This suggests an onboarding failure, not a pricing problem
- Action: Assign a customer success touchpoint at Day 7, 30, and 90

### Finding 3: Fiber optic internet has the highest churn rate
- Fiber optic customers churn at 41.9% vs 19.0% for DSL customers
- They also pay $20/month more on average
- Action: Audit Fiber optic service quality and NPS scores

### Revenue At Risk by Priority Tier
| Segment       | Customers | Revenue at risk | Priority |
|---------------|-----------|-----------------|----------|
| High (60-100%)| 206       | $201,156        | Immediate|
| Medium (30-60%)| 312      | $128,441        | This qtr |
| Low (0-30%)   | 891       | $46,832         | Monitor  |

### Model Performance
| Metric    | Logistic Regression | XGBoost  |
|-----------|---------------------|----------|
| AUC-ROC   | 0.844               | 0.871    |
| F1 Score  | 0.612               | 0.641    |
| Precision | 0.68                | 0.71     |
| Recall    | 0.56                | 0.58     |

XGBoost selected as production model (higher AUC-ROC).
