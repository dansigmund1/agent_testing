#!/usr/bin/env python3

import anthropic
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()
    
def review_data_quality(file_content, constraints):
    """
    Use Claude to review data quality based on constraints
    
    Args:
         file_content: The content of the data file
         constraints: Dictionary of quality constraints
    """

    constraints_text = "\n".join([f"- {k}: {v}" for k, v in constraints.items()])
    prompt = f"""Please review the following data file for quality issues based on these constraints:
{constraints_text}

Data File Content:
{file_content}

Please Provide:
1. A summary of overall data quality
2. Specific issues found with row/column references
3. Severity of each issue (Critical, Warning, Info)
4. Recommendations for fixing the issues
5. A quality score out of 100

Format your response as structured JSON."""
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[
            {"role":"user", "content":prompt}
        ]
    )
    return message.content[0].text

def main():
    constraints = {
        "Mising Values":"No null or empty values allowed in required columns",
        "Data Types":"Email must be valid format, Age must be numeric",
        "Range Checks":"Age should be between 0-120, Salary should be positive",
        "Uniqueness":"ID column must have unique values",
        "Consistency":"Date formats should be consistent (YYYY-MM-DD)",
        "Completeness":"All required columns must be present"
    }

    file_path = "name_of_file.csv"
    file_content = read_file(file_path)

    print("Reviewing data quality with Claude...\n")

    review = review_data_quality(file_content, constraints)

    
    print("=" * 80)
    print("DATA QUALITY REVIEW")
    print("=" * 80)
    print(review)
    print("=" * 80)

if __name__=="__main__":
    main()