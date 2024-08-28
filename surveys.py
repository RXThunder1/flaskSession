class Question:
    def __init__(self, text, choices, allow_comments=False):
        self.text = text
        self.choices = choices
        self.allow_comments = allow_comments

class Survey:
    def __init__(self, title, instructions, questions):
        self.title = title
        self.instructions = instructions
        self.questions = questions

# Example of satisfaction_survey initialization
satisfaction_survey = Survey(
    title="Customer Satisfaction Survey",
    instructions="Please answer the following questions about your experience.",
    questions=[
        Question(
            text="How satisfied are you with our product?",
            choices=["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"]
        ),
        Question(
            text="Would you recommend our product to others?",
            choices=["Yes", "No"]
        ),
        Question(
            text="What is your annual income?",
            choices=["Less than $10,000", "$10,000 - $50,000", "$50,000 - $100,000", "Over $100,000"]
        ),
        Question(
            text="Do you have any other comments or suggestions?",
            choices=["Yes", "No"]
        )
    ]
)