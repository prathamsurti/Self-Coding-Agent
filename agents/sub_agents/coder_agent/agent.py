from google.adk.agents import LlmAgent
from .log_parser import parse_log_file

root_agent = LlmAgent(
    name="root_coder_agent",
    model="gemini-2.0-flash",
    description=(
        "An intelligent agent that takes a log file path as input, "
        "parses and structures the errors found, and then generates corrected code snippets along with example usage."
    ),
    instruction=(
        "You are a professional log analyzer and software engineer.\n"
        "Follow these steps strictly:\n"
        "\n"
        "Step 1: Use the provided 'parse_log_file' tool to analyze the given file_path (log file).\n"
        "Step 2: Extract and present all errors, warnings, or critical issues in a structured format.\n"
        "    - Prefer JSON format if possible.\n"
        "    - Include fields like: 'Error Type', 'Cause', 'File Name', 'Line Number', and 'Additional Context'.\n"
        "    - If no errors are found, explicitly mention it.\n"
        "\n"
        "Step 3: Based on the structured errors identified:\n"
        "    - Analyze the root cause(s).\n"
        "    - Write the corrected code snippets that would fix these issues.\n"
        "    - Provide a brief but complete example showing how the corrected code should be used.\n"
        "\n"
        "Make sure:\n"
        "- Your structured error report is clear and properly formatted.\n"
        "- Your code is clean, efficient, and well-documented.\n"
        "- Separate the structured error report and code solution clearly with headings like '## Error Report' and '## Code Solution'."
    ),
    tools=[parse_log_file]
)
