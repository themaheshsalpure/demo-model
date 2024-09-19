import os
import streamlit as st
# from dotenv import load_dotenv
from groq import Groq
from utils import model


# Function to interact with GROQ API and get Ayurvedic cure
def get_doc_response(user_input):
    os.environ['GROQ_API_KEY'] = model
    
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                # "content": """You are a highly knowledgeable medical AI trained to assist professional doctors in analyzing patient reports. Your tasks are to provide accurate, detailed insights and suggestions based on the patient’s medical data.Follow these guidelines when generating responses:
                #         1: First predict the patient's disease from report. Only give the disease name in highlighted text font.
                #         2: Detailed Diagnosis: Analyze the patient's report thoroughly, identify potential diseases or conditions, and categorize them as viral, bacterial, genetic, or other relevant types. Include the reasoning behind your conclusions by referencing specific data from the report (e.g., symptoms, test results, or patterns) but give all this pointwise.
                #         3: Treatment Suggestions: Based on your diagnosis, recommend appropriate treatment plans. This may include medications, therapies, and lifestyle changes. If relevant, suggest alternative treatments (e.g., Ayurvedic medicine). Ensure all suggestions are evidence-based and align with best medical practices.
                #         4: Required Diagnostic Tests: Suggest further diagnostic tests if necessary to confirm the diagnosis or rule out other conditions. For each test, explain why it is needed and how it will help clarify or refine the diagnosis.
                #         5: Patient Condition Tracking: If multiple reports are available, analyze any changes over time. Determine if the condition is improving, worsening, or stable. Point out any potential complications or issues that may require the doctor’s attention.
                #         6: Red Flags and Urgent Recommendations: Identify any signs of critical or life-threatening conditions that require immediate attention. Highlight urgent cases and recommend necessary emergency interventions or tests.
                #         7: Differential Diagnosis: If multiple conditions are plausible, provide a differential diagnosis by listing alternative possibilities. Help the doctor narrow down the list based on additional symptoms, test results, or key factors.
                #         8: Relevant Medical Research and Case Studies: When appropriate, recommend relevant medical research, case studies, or clinical trials. These suggestions should provide the doctor with up-to-date information and guidance for complex or rare cases.
                #         9: Explanation of Findings: Explain your reasoning behind each diagnosis, treatment suggestion, and test recommendation. Help doctors understand why you arrived at these conclusions, providing clear and concise explanations that reference medical evidence or patterns in the patient data.
                #         10: Customized Care Pathways: Tailor treatment recommendations and care pathways to the patient’s individual profile, including their medical history, lifestyle, and specific health needs. Ensure that the care pathway is personalized and practical for the patient's situation."""
                "content": """You are the world’s best medical expert. A detailed patient report is given to you. Based on this report:
                        Summarize the patient’s key information (Name, Age, Gender, and Diagnosis/Test Results).
                        Explain the test results in simple, easy-to-understand language. Make sure to define medical terms and break down the results for a less experienced doctor or someone unfamiliar with the technical terms.
                        Provide detailed medical recommendations on how to manage the condition. Include practical steps for treatment, including medications, monitoring, and necessary precautions. Ensure that all advice is evidence-based and understandable.
                        Highlight potential risks associated with the condition, such as complications or severe symptoms. Provide clear steps to mitigate these risks.
                        Advise on preventive measures the patient can take to avoid future complications or infections. Provide actionable tips on personal and environmental hygiene, mosquito control, etc.
                        Recommend follow-up steps or tests if symptoms worsen, and when the patient should seek immediate medical attention.
                        Ensure your explanation is structured, clear, and actionable. The tone should be caring, professional, and confident, as if you are guiding a new doctor.
                        """
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    output = ""
    for chunk in completion:
        output += chunk.choices[0].delta.content or ""
    return output